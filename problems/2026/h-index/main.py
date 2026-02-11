
n = int(input())
for c in range(n):
    ps = list(map(int, input().split(" ")))
    ps.sort(reverse=True)
    p = -1
    # print(ps)
    for p in range(len(ps)):
        # print(f:e $DE"check {p} {ps[p]}")
        if ps[p] < p+1:
            p = p - 1
            break

    print(c+1, p+1)

