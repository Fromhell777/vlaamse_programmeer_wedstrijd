import math

import itertools

def func(grid, c):
  s = sum(grid[e[0]][e[1]] for e in c)
  if s > 0:
    return (1, 0, 0)
  if s == 0:
    return (0, 1, 0)
  else:
    return (0, 0, 1)

def g(a, b):
  return tuple([i + j for i, j in zip(a,b)])

def f(grid, c, x1, x2, y1, y2):
  if x1 == x2 or y1 == y2:
    return (0, 0, 0)

  if tuple((x1, x2, y1, y2)) not in c:
    # print(x1, x2, y1, y2)
    sub = [
        g(f(grid, c, x1 + 1, x2, y1, y2), func(grid, [(y, x1) for y in range(y1, y2)])),
        g(f(grid, c, x1, x2 - 1, y1, y2), func(grid, [(y, x2-1) for y in range(y1, y2)])),
        g(f(grid, c, x1, x2, y1 + 1, y2), func(grid, [(y1, x) for x in range(x1, x2)])),
        g(f(grid, c, x1, x2, y1, y2 - 1), func(grid, [(y2-1, x) for x in range(x1, x2)])),
    ]
    best = max(sub)
    c[tuple((x1, x2, y1, y2))] = best
  return c[(x1, x2, y1, y2)]

cases = int(input())
for case in range(cases):
    b, h = map(int, input().split(" "))
    grid = []
    for _ in range(h):
      r = input()
      votes = [1 if e == 'A' else -1 for e in r]
      grid.append(list(votes))

    c = {}
    f(grid, c, 0, b, 0, h)
    print(case + 1, *c[(0, b, 0, h)])

