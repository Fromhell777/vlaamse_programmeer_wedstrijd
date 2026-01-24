import copy
import re

test_cases = int(input())

for _ in range(test_cases):

  num_rows, num_cols = [int(x) for x in input().split()]

  grid = []
  equal_pos = (0,0)
  for i in range(num_rows):
    grid.append(input().replace('x', '*'))
    if '=' in grid[-1]:
      equal_pos = (i, grid[-1].find('='))

  equations = []
  tiles_hit = []

  current_equation = ""

  visited = set()

  dirs = [[0, 1], [1, 0], [0, -1], [-1, 0]]

  def get_equations(y, x):
    global current_equation

    if (y,x) not in visited:
      visited.add((y,x))

      current_equation += grid[y][x]
      if current_equation[-1] not in "=+-*":
        equations.append(current_equation[1:])
        tiles_hit.append(copy.deepcopy(visited))
        tiles_hit[-1].remove(equal_pos)

      for dy, dx in dirs:
        new_y = y + dy
        new_x = x + dx
        if new_y >= 0 and new_x >= 0 and new_y < num_rows and new_x < num_cols:
          if len(current_equation) < num_cols * num_rows - 1:
            if (current_equation[-1] in "=+-*"):
              if (grid[new_y][new_x] not in "=+-*"):
                get_equations(new_y, new_x)
            else:
              get_equations(new_y, new_x)

      current_equation = current_equation[:-1]
      visited.remove((y,x))

  get_equations(equal_pos[0], equal_pos[1])

  map_to_equations = {}
  for i, forward_equation in enumerate(equations):

    test_leading_zero = re.split("\\+|-|\\*", forward_equation)
    if any(number[0] == '0' for number in test_leading_zero):
      continue

    current_tiles_hit = tiles_hit[i]
    current_tiles_hit = list(current_tiles_hit)
    current_tiles_hit.sort()
    current_tiles_hit = tuple(current_tiles_hit)
    map_to_equations.setdefault(current_tiles_hit, [])
    map_to_equations[current_tiles_hit].append(forward_equation)

  total_tiles = set()
  for i in range(num_rows):
    for j in range(num_cols):
      total_tiles.add((i,j))

  total_tiles.remove(equal_pos)

  def get_result():
    for i, lhs in enumerate(equations):

      test_leading_zero = re.split("\\+|-|\\*", lhs[::-1])
      if any(number[0] == '0' for number in test_leading_zero):
        continue

      other_tiles = total_tiles - tiles_hit[i]
      other_tiles = list(other_tiles)
      other_tiles.sort()
      other_tiles = tuple(other_tiles)

      if other_tiles in map_to_equations:
        for rhs in map_to_equations[other_tiles]:
          equation = lhs[::-1] + "==" + rhs
          if eval(equation):
            result = lhs[::-1] + '=' + rhs
            result = result.replace('*', 'x')
            return result

  print(get_result())
