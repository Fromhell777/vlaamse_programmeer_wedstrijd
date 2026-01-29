import math

cases = int(input())

for case in range(cases):
    # print(f"Case {case}")
    cost = int(input())
    _, *list_s = map(int, input().split(" "))
    _, *list_m = map(int, input().split(" "))
    _, *list_e = map(int, input().split(" "))

    coins_m = sorted(list_m)[::-1]

    dict_s = {}
    for c in list_s:
        dict_s[c] = dict_s.get(c, 0) + 1
    coins_s = sorted(dict_s.items())

    dict_e = {}
    for c in list_e:
        dict_e[c] = dict_e.get(c, 0) + 1
    coins_e = sorted(dict_e.items())[::-1]

    # print(f"  {coins_s=}")
    # print(dict_e)

    delta = sum(list_e)
    target = cost + delta

    # check if return is correct
    curr = delta
    valid = True
    for c in coins_m:
        n = curr // c
        tc = dict_e.get(c, 0)
        # print(f"iter curr={curr}, coin={c} target coin={tc}, m={n}")
        curr -= n * c
        if n != tc:
            # print("  invalid")
            valid = False
            break
    valid = valid and curr == 0

    if not valid:
        print(case + 1, "ONMOGELIJK")
        continue

    # check if we can reach the target
    def f(next_coin, curr):
        # print(f"f {next_coin} {curr} -> {target}")
        if curr == target:
            return 0
        if curr >= cost or next_coin >= len(coins_s):
            return math.inf

        best = math.inf
        for count in range(coins_s[next_coin][1] + 1):
            best = min(best, f(next_coin + 1, curr + count * coins_s[next_coin][0]) + count)
        return best

    print(case + 1, f(0, 0))