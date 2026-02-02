test_cases = int(input())

for _ in range(test_cases):

  num_lines = int(input())

  lines = []
  max_x = 0
  max_y = 0
  for _ in range(num_lines):
    x1, y1, x2, y2 = map(int, input().split())

    lines.append((x1, y1, x2, y2))

    max_x = max(max_x, x2 + 1)
    max_y = max(max_y, y2 + 1)

  grid_hor = [[False] * 2 * max_y for _ in range(2 * max_x)]
  grid_ver = [[False] * 2 * max_y for _ in range(2 * max_x)]

  crosspoints = set()

  for x1, y1, x2, y2 in lines:
    if x1 == x2:
      for y in range(2 * y1, 2 * y2 + 1):
        grid_hor[2 * x1][y] = True

        if grid_ver[2 * x1][y]:
          crosspoints.add((2 * x1, y))

    if y1 == y2:
      for x in range(2 * x1, 2 * x2 + 1):
        grid_ver[x][2 * y1] = True

        if grid_hor[x][2 * y1]:
          crosspoints.add((x, 2 * y1))

  result = 0

  for x1,y1 in crosspoints:
    for x2,y2 in crosspoints:
      if x1 < x2 and y1 < y2:
        rect = True

        for x in range(x1, x2 + 1):
          if (not grid_ver[x][y1]) or (not grid_ver[x][y2]):
            rect = False
            break

        for y in range(y1, y2 + 1):
          if (not grid_hor[x1][y]) or (not grid_hor[x2][y]):
            rect = False
            break

        if rect:
          result += 1

  print(result)
