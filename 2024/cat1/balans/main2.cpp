#include <algorithm>
#include <cstdint>
#include <cstdio>
#include <iostream>
#include <vector>

// #include <chrono>

int main() {

    constexpr int16_t INVALID = INT16_MAX / 4;

    std::ios_base::sync_with_stdio(false);

    constexpr size_t BLOCKSIZE = 1024 * 1024;
    std::vector<char> filedata;
    for( ; ; ) {
        size_t pos = filedata.size();
        filedata.resize(pos + BLOCKSIZE);
        size_t len = fread(filedata.data() + pos, 1, BLOCKSIZE, stdin);
        if(len < BLOCKSIZE) {
            filedata.resize(pos + len);
            break;
        }
    }

    size_t filepos = 0;
    int32_t numtests = 0;
    for( ; ; ) {
        if(filepos >= filedata.size())
            return 1;
        char c = filedata[filepos++];
        if(c < '0') {
            break;
        } else {
            numtests = 10 * numtests + int32_t(c - '0');
        }
    }

    std::vector<int32_t> ww1, ww2;
    std::vector<int16_t> opt1, opt2;
    std::vector<int32_t> lb1, lb2;
    std::vector<int32_t> skip1, skip2;
    std::vector<int32_t> stop1, stop2;

    // uint64_t timers[4] = {0, 0, 0, 0};

    for(int32_t test = 0; test < numtests; ++test) {

        // auto t1 = std::chrono::high_resolution_clock::now();

        ww1.clear();
        ww2.clear();
        int32_t val = 0;
        for( ; ; ) {
            if(filepos >= filedata.size())
                return 1;
            char c = filedata[filepos++];
            if(c < '0') {
                if(val != 0) {
                    ww1.push_back(val);
                    val = 0;
                }
                if(c == '\n')
                    break;
            } else {
                val = 10 * val + int32_t(c - '0');
            }
        }
        for( ; ; ) {
            if(filepos >= filedata.size())
                return 1;
            char c = filedata[filepos++];
            if(c < '0') {
                if(val != 0) {
                    ww2.push_back(val);
                    val = 0;
                }
                if(c == '\n')
                    break;
            } else {
                val = 10 * val + int32_t(c - '0');
            }
        }

        // auto t2 = std::chrono::high_resolution_clock::now();

        std::sort(ww1.begin(), ww1.end());
        std::sort(ww2.begin(), ww2.end());

        // auto t3 = std::chrono::high_resolution_clock::now();

        int32_t total1 = 0, total2 = 0;
        for(int32_t w : ww1) {
            total1 += w;
        }
        for(int32_t w : ww2) {
            total2 += w;
        }
        if((total1 + total2) % 2 != 0) {
            std::cout << (test + 1) << ' ' << "onmogelijk" << std::endl;
            continue;
        }

        if(total1 < total2) {
            ww1.swap(ww2);
            std::swap(total1, total2);
        }

        opt1.clear();
        opt2.clear();
        opt1.resize(total1 + 1, 2 * INVALID);
        opt2.resize(total2 + 1, 2 * INVALID);
        opt1[0] = 0;
        opt2[0] = 0;

        lb1.resize(ww1.size(), 0);
        lb2.resize(ww2.size(), 0);
        skip1.resize(ww1.size() + 1, 0);
        skip2.resize(ww2.size() + 1, 0);
        stop1.resize(ww1.size() + 1, 0);
        stop2.resize(ww2.size() + 1, 0);

        {
            int32_t ref = total1;
            for(int32_t i = 0; i < (int32_t) ww1.size(); ++i) {
                opt1[ref] = (int32_t) ww1.size() - i;
                lb1[i] = (int32_t) ww1.size() - i;
                skip1[(int32_t) ww1.size() - i] = ref - ww1[i] + 1;
                stop1[(int32_t) ww1.size() - i] = ref;
                ref -= ww1[i];
            }
        }
        {
            int32_t ref = total2;
            for(int32_t i = 0; i < (int32_t) ww2.size(); ++i) {
                opt2[ref] = (int32_t) ww2.size() - i;
                lb2[i] = (int32_t) ww2.size() - i;
                skip2[(int32_t) ww2.size() - i] = ref - ww2[i] + 1;
                stop2[(int32_t) ww2.size() - i] = ref;
                ref -= ww2[i];
            }
        }

        // auto t4 = std::chrono::high_resolution_clock::now();

        int32_t i1 = 0, i2 = 0, sum1 = 0, sum2 = 0;
        int32_t bi1 = 0, bi2 = 0, bv1 = 0, bv2 = 0;
        int32_t target = (total1 - total2) / 2;
        int16_t best = INVALID;
        for(int32_t v = 0; v <= total2; ++v) {

            while(bv1 < target + v) {
                ++bi1;
                bv1 += ww1[ww1.size() - bi1];
            }
            while(bv2 < v) {
                ++bi2;
                bv2 += ww2[ww2.size() - bi2];
            }
            if(bi1 + bi2 >= best) {
                break;
            }

            while(sum1 < target + v) {
                int32_t batch = std::max(1000, target + v - sum1);
                int32_t wi = ww1[i1];
                int32_t ref = total1 - wi + 1;
                ++i1;
                for(int32_t j = i1; j < (int32_t) ww1.size(); ++j) {
                    int32_t wj = ww1[j];
                    ref -= wj;
                    if(ref + wi <= target)
                        break;
                    int32_t ref2 = std::max(ref, target);
                    int32_t lb = lb1[j];
                    int32_t k = skip1[lb];
                    if(k < ref2) {
                        k = ref2;
                        int32_t stop = std::min(ref + wi, stop1[lb]);
                        while(k < stop) {
                            opt1[k] = std::min<int16_t>(opt1[k], opt1[k + wj] - 1);
                            ++k;
                        }
                        if(k < ref + wi) {
                            ++lb;
                            k = skip1[lb];
                        }
                    }
                    while(k < ref + wi) {
                        int32_t stop = std::min(ref + wi, stop1[lb]);
                        while(k < stop) {
                            opt1[k] = std::min<int16_t>(opt1[k], opt1[k + wj] - 1);
                            if(opt1[k] != lb)
                                break;
                            ++k;
                        }
                        skip1[lb] = k;
                        ++k;
                        while(k < stop) {
                            opt1[k] = std::min<int16_t>(opt1[k], opt1[k + wj] - 1);
                            ++k;
                        }
                        if(k < ref + wi) {
                            ++lb;
                            k = skip1[lb];
                        }
                    }
                    if(wi < batch) {
                        wi += wj;
                        ++i1;
                    }
                    lb1[j] = lb;
                }
                sum1 += wi;
            }

            while(sum2 < v) {
                int32_t batch = std::max(1000, v - sum2);
                int32_t wi = ww2[i2];
                int32_t ref = total2 - wi + 1;
                ++i2;
                for(int32_t j = i2; j < (int32_t) ww2.size(); ++j) {
                    int32_t wj = ww2[j];
                    ref -= wj;
                    int32_t lb = lb2[j];
                    int32_t k = skip2[lb];
                    if(k < ref) {
                        k = ref;
                        int32_t stop = std::min(ref + wi, stop2[lb]);
                        while(k < stop) {
                            opt2[k] = std::min<int16_t>(opt2[k], opt2[k + wj] - 1);
                            ++k;
                        }
                        if(k < ref + wi) {
                            ++lb;
                            k = skip2[lb];
                        }
                    }
                    while(k < ref + wi) {
                        int32_t stop = std::min(ref + wi, stop2[lb]);
                        while(k < stop) {
                            opt2[k] = std::min<int16_t>(opt2[k], opt2[k + wj] - 1);
                            if(opt2[k] != lb)
                                break;
                            ++k;
                        }
                        skip2[lb] = k;
                        ++k;
                        while(k < stop) {
                            opt2[k] = std::min<int16_t>(opt2[k], opt2[k + wj] - 1);
                            ++k;
                        }
                        if(k < ref + wi) {
                            ++lb;
                            k = skip2[lb];
                        }
                    }
                    if(wi < batch) {
                        wi += wj;
                        ++i2;
                    }
                    lb2[j] = lb;
                }
                sum2 += wi;
            }

            if(opt1[target + v] + opt2[v] < best) {
                best = opt1[target + v] + opt2[v];
            }

        }
        if(best == INVALID) {
            std::cout << (test + 1) << ' ' << "onmogelijk" << std::endl;
        } else {
            std::cout << (test + 1) << ' ' << best << std::endl;
        }

        // auto t5 = std::chrono::high_resolution_clock::now();

        // timers[0] += std::chrono::duration_cast<std::chrono::nanoseconds>(t2 - t1).count();
        // timers[1] += std::chrono::duration_cast<std::chrono::nanoseconds>(t3 - t2).count();
        // timers[2] += std::chrono::duration_cast<std::chrono::nanoseconds>(t4 - t3).count();
        // timers[3] += std::chrono::duration_cast<std::chrono::nanoseconds>(t5 - t4).count();

    }

    // std::cerr << "TIMERS:" << std::endl;
    // std::cerr << timers[0] << std::endl;
    // std::cerr << timers[1] << std::endl;
    // std::cerr << timers[2] << std::endl;
    // std::cerr << timers[3] << std::endl;

    return 0;
}
