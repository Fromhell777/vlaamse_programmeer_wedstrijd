import math

import itertools

cases = int(input())


for case in range(cases):
    k, n = map(int, input().split(" "))
    h = []
    for _ in range(k):
        x, y = map(int, input().split(" "))
        h.append((x, y))

    # best = math.inf

    # h.sort(key=lambda p: max(p))
    # h_new = [None] * len(h)
    # h_new[::2] = h[::2]
    # h_new[1::2] = h[1::2][::-1]

    # for js in itertools.combinations(range(k), n):

    #     curr = 0
    #     for ai in js:
    #         for bi in js[:ai]:
    #             curr = max(curr, abs(h[ai][0] - h[bi][0]) + abs(h[ai][1] - h[bi][1]))
    #             if curr > best:
    #                 break
    #         if curr > best:
    #                 break

    #     best = min(best, curr)

    # print(case, best)

    best = math.inf

    h.sort(key=lambda b: abs(b[0]) + abs(b[1]))

    for ci, (cx, cy) in enumerate(h[:-1]):
        c = [
            p
            for p in h
            if abs(cx - p[0]) + abs(cy - p[1]) < best
        ]

        c.sort(key=lambda b: abs(cx - b[0]) + abs(cy - b[1]))

        if len(c) < n:
            continue

        # d = [((abs(cx - b[0]) + abs(cy - b[1])), b) for b in c]
        # d.sort()



        closest = c[:n]

        curr= 0
        for ai in range(n):
            for b in closest[:ai]:
                curr = max(curr, abs(closest[ai][0] - b[0]) + abs(closest[ai][1] - b[1]))
                if curr > best:
                    break
            if curr > best:
                    break

        # d = max(abs(closest[ai][0] - b[0]) + abs(closest[ai][1] - b[1]) for ai in range(n) for b in closest[:ai])
        best = min(best, curr)

    print(case + 1, best)
