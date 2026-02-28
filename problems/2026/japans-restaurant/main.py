from functools import cache
import time

n = int(input())

for c in range(n):
    # if c != 4:
    #     continue

    num_ger, max_weight = list(map(int, input().split(" ")))
    gerechten = []
    for _ in range(num_ger):
        gew, vol, dvol = list(map(int, input().split(" ")))
        gerechten.append((gew, vol, dvol))

    # start = time.perf_counter()
    gerechten.sort(key=lambda x: (x[1]/x[0]), reverse=True)

    # if c != 4:
    #     continue

    # print(gerechten)
    # print(max_weight)

    cache = {}
    def f(curr_weight, next):
        # if time.perf_counter() - start > 0.1:
        #     return -1
        # print(f"f iter {curr_weight, curr_vol, next}")

        if curr_weight > max_weight:
            return 0
        if next >= len(gerechten):
            return 0

        k = (curr_weight, next)
        if k in cache:
            return cache[k]

        gew, vol, dvol = gerechten[next]
        best = 0

        for count in reversed(range(0, (max_weight - curr_weight) // gew + 1)):
            loop_vol = 0
            loop_ger_vol = vol
            for _ in range(count):
                loop_vol += loop_ger_vol
                loop_ger_vol -= dvol

            res = loop_vol + f(curr_weight + gew * count, next+1)
            best = max(best, res)

        cache[k] = best
        return best

    print(c+1, f(0, 0))





