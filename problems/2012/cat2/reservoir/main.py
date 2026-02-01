test_cases = int(input())

for _ in range(test_cases):

  num_rows, num_cols = [int(x) for x in input().split()]

  grid = []
  for _ in range(num_rows):
    grid.append([int(x) for x in input().split()])

  max_height = 0
  for row in grid:
    max_height = max(max_height, max(row))

  def floodfill_ok(row, col, height):

    visited = set()

    to_visit = [(row,col)]

    dirs = [[0, 1], [1, 0], [0, -1], [-1, 0]]

    while len(to_visit) > 0:
      position = to_visit.pop()

      if position not in visited:
        visited.add(position)

        for dy, dx in dirs:
          new_y = position[0] + dy
          new_x = position[1] + dx
          if new_y >= 0 and new_x >= 0 and new_y < num_rows and new_x < num_cols:
            if grid[new_y][new_x] < height:
              if new_y == 0 or \
                 new_x == 0 or \
                 new_y == num_rows - 1 or \
                 new_x == num_cols - 1:
                return False

              to_visit.append((new_y, new_x))

    return True

  result = 0
  for row in range(1, num_rows - 1):
    for col in range(1, num_cols - 1):
      block_height = grid[row][col]

      for height in range(block_height + 1, max_height + 1):
        if floodfill_ok(row, col, height):
          result += 1
        else:
          break

  print(result)
