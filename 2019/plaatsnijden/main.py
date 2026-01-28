

def f(cache, curr):
    curr = (min(curr), max(curr))

    res = cache.get(curr, None)
    if res is not None:
        return res

    res = set()
    w, h = curr

    for cw in range(1, w):
        af = f(cache, (cw, h))
        bf = f(cache, (w - cw, h))
        for a in af:
            for b in bf:
                res.add(frozenset(a | b))

    for ch in range(1, h):
        af = f(cache, (w, ch))
        bf = f(cache, (w, h - ch))
        for a in af:
            for b in bf:
                res.add(frozenset(a | b))

    res.add(frozenset({curr}))

    res = frozenset(res)
    cache[curr] = res

    print(f"{curr} -> {res}")

    return res


# cases = int(input())
# for case in range(cases):
#     w, h = map(int, input().split())
#     print(case + 1, len(f({}, (w, h))))

print(f({}, (2, 2)))