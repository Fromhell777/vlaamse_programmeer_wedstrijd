#include <algorithm>
#include <cassert>
#include <cstdint>
#include <cstdio>
#include <iostream>
#include <numeric>
#include <vector>

struct Pair1 {
    bool is_right;
    int32_t value;
    inline Pair1() {}
    inline Pair1(bool is_right, int32_t value) : is_right(is_right), value(value) {}
};
struct Pair2 {
    int32_t value_left;
    int32_t swaps;
    inline Pair2() {}
    inline Pair2(int32_t value_left, int32_t swaps) : value_left(value_left), swaps(swaps) {}
};

inline bool cmp(const Pair1& a, const Pair1& b) {
    return a.value > b.value;
}

int32_t solve(const std::vector<int32_t>& left, const std::vector<int32_t>& right) {
    int32_t total_left = accumulate(left.begin(), left.end(), 0);
    int32_t total_right = accumulate(right.begin(), right.end(), 0);

    // Note: this check will be happen instantly in the inner loop anyway
    if (total_left == total_right)
        return 0;

    int32_t total = total_left + total_right;
    if (total % 2 != 0)
        return INT32_MAX;
    int32_t target = total / 2;

    std::vector<Pair1> rem;
    for (const auto& x : left)
        rem.push_back(Pair1{false, x});
    for (const auto& x : right)
        rem.push_back(Pair1{true, x});

    sort(rem.begin(), rem.end(), cmp);

    std::vector<int32_t> max_possible_left_to_right = {0}, max_possible_right_to_left = {0};
    for (size_t i = 0; i < rem.size(); ++i) {
        bool curr_was_right = rem[i].is_right;
        int32_t curr_value = rem[i].value;
        if(curr_was_right) {
            max_possible_right_to_left.push_back(max_possible_right_to_left.back() + curr_value);
        } else {
            max_possible_left_to_right.push_back(max_possible_left_to_right.back() + curr_value);
        }
    }
    // Note: instead of repeating, clamp the index on usage
//    while(max_possible_left_to_right.size() <= left.size() + rem.size() / 2) {
//        max_possible_left_to_right.push_back(max_possible_left_to_right.back());
//    }
//    while(max_possible_right_to_left.size() <= right.size() + rem.size() / 2) {
//        max_possible_right_to_left.push_back(max_possible_right_to_left.back());
//    }

    std::vector<Pair2> min_swaps_for(1000000);
    std::vector<Pair2> next_min_swaps_for(1000000);

    for(int32_t max_swaps = 1; max_swaps <= (int32_t) rem.size() / 2; ++max_swaps) {

        int32_t rem_sum_left = total_left;
        int32_t done_left = 0;
        int32_t done_right = 0;

        size_t min_swaps_for_size = 1;
        min_swaps_for[0] = Pair2{0, 0};

        for (size_t i = 0; i < rem.size(); ++i) {
            if (min_swaps_for_size == 0)
                break;

            if(next_min_swaps_for.size() < 2 * min_swaps_for_size + 1) {
                next_min_swaps_for.resize(2 * min_swaps_for_size + 1);
            }
            size_t next_min_swaps_for_size = 0;

            bool curr_was_right = rem[i].is_right;
            int32_t curr_value = rem[i].value;

            if (curr_was_right) {
                ++done_right;
            } else {
                rem_sum_left -= curr_value;
                ++done_left;
            }

            int32_t baseline_left_to_right = max_possible_left_to_right[std::min(done_left, (int32_t) (max_possible_left_to_right.size()-1))];
            int32_t baseline_right_to_left = max_possible_right_to_left[std::min(done_right, (int32_t) (max_possible_right_to_left.size()-1))];
            int32_t relative_target = target - rem_sum_left;

            auto add = [&](int32_t value_left, int32_t swaps, bool skip1, bool skip2) {
                if (!skip1 && value_left == relative_target)
                    return true;
                // assert(!(value_left == relative_target));

                int32_t swaps_remaining = max_swaps - swaps;
                if (!skip1 && swaps_remaining <= 0)
                    return false;
                // assert(!(swaps_remaining <= 0));

                int32_t max_possible_left = value_left + (max_possible_right_to_left[std::min(done_right + swaps_remaining, (int32_t) (max_possible_right_to_left.size()-1))] - baseline_right_to_left);
                int32_t min_possible_left = value_left - (max_possible_left_to_right[std::min(done_left + swaps_remaining, (int32_t) (max_possible_left_to_right.size()-1))] - baseline_left_to_right);

                if (!skip2 && (max_possible_left < relative_target || min_possible_left > relative_target))
                    return false;
                // assert(!(max_possible_left < relative_target || min_possible_left > relative_target));

                next_min_swaps_for[next_min_swaps_for_size++] = Pair2{value_left, swaps};
                return false;
            };

            if (curr_was_right) {
                size_t a = 0, b = 0;
                for (; a < min_swaps_for_size; ++a) {
                    int32_t next_a = min_swaps_for[a].value_left;
                    int32_t next_b = min_swaps_for[b].value_left + curr_value;
                    while (next_b < next_a) {
                        int32_t swaps_b = min_swaps_for[b].swaps + 1;
                        if(add(next_b, swaps_b, false, false))
                            return max_swaps;
                        ++b;
                        next_b = min_swaps_for[b].value_left + curr_value;
                    }
                    if (next_b == next_a) {
                        int32_t swaps_a = min_swaps_for[a].swaps;
                        int32_t swaps_b = min_swaps_for[b].swaps + 1;
                        add(next_a, std::min(swaps_a, swaps_b), true, true);
                        ++b;
                    } else {
                        int32_t swaps_a = min_swaps_for[a].swaps;
                        add(next_a, swaps_a, true, false);
                    }
                }
                for (; b < min_swaps_for_size; ++b) {
                    int32_t next_b = min_swaps_for[b].value_left + curr_value;
                    int32_t swaps_b = min_swaps_for[b].swaps + 1;
                    if(add(next_b, swaps_b, false, false))
                        return max_swaps;
                }
            } else {
                size_t a = 0, b = 0;
                for (; a < min_swaps_for_size; ++a) {
                    int32_t next_a = min_swaps_for[a].value_left;
                    int32_t next_b = min_swaps_for[b].value_left + curr_value;
                    while (next_b < next_a) {
                        int32_t swaps_b = min_swaps_for[b].swaps;
                        add(next_b, swaps_b, true, false);
                        ++b;
                        next_b = min_swaps_for[b].value_left + curr_value;
                    }
                    if (next_b == next_a) {
                        int32_t swaps_a = min_swaps_for[a].swaps + 1;
                        int32_t swaps_b = min_swaps_for[b].swaps;
                        add(next_a, std::min(swaps_a, swaps_b), true, true);
                        ++b;
                    } else {
                        int32_t swaps_a = min_swaps_for[a].swaps + 1;
                        if(add(next_a, swaps_a, false, false))
                            return max_swaps;
                    }
                }
                for (; b < min_swaps_for_size; ++b) {
                    int32_t next_b = min_swaps_for[b].value_left + curr_value;
                    int32_t swaps_b = min_swaps_for[b].swaps;
                    add(next_b, swaps_b, true, false);
                }
            }

            min_swaps_for.swap(next_min_swaps_for);
            min_swaps_for_size = next_min_swaps_for_size;

        }

    }

    return INT32_MAX;
}

int main() {

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

    std::vector<int32_t> left, right;

    for(int32_t test = 0; test < numtests; ++test) {

        left.clear();
        right.clear();
        int32_t val = 0;
        for( ; ; ) {
            if(filepos >= filedata.size())
                return 1;
            char c = filedata[filepos++];
            if(c < '0') {
                if(val != 0) {
                    left.push_back(val);
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
                    right.push_back(val);
                    val = 0;
                }
                if(c == '\n')
                    break;
            } else {
                val = 10 * val + int32_t(c - '0');
            }
        }

        int32_t result = solve(left, right);
        if(result == INT32_MAX) {
            std::cout << (test + 1) << ' ' << "onmogelijk" << std::endl;
        } else {
            std::cout << (test + 1) << ' ' << result << std::endl;
        }

    }

    return 0;
}
