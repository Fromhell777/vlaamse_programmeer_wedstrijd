test_cases = int(input())

for t in range(test_cases):

  if t > 0:
    input()

  num_rows = 7
  num_cols = 8

  grid = []
  for _ in range(num_rows):
    grid.append([int(x) for x in input().split()])

  tiles = set()
  for i in range(7):
    for j in range(i, 7):
      tiles.add((i, j))

  result = 0

  def find_solution(grid_taken, tiles):
    global result

    if len(tiles) == 0:
      result += 1
      return

    current_position = None
    for i in range(num_rows):
      for j in range(num_cols):
        if not grid_taken[i][j]:
          current_position = (i,j)
          break

      if current_position is not None:
        break

    if current_position is None:
      return

    right_position = (current_position[0], current_position[1] + 1)
    down_position  = (current_position[0] + 1, current_position[1])

    if right_position[1] < num_cols and \
       not grid_taken[right_position[0]][right_position[1]]:
      num1 = grid[current_position[0]][current_position[1]]
      num2 = grid[right_position[0]][right_position[1]]

      if num1 < num2:
        tile = (num1, num2)
      else:
        tile = (num2, num1)

      if tile in tiles:
        tiles.remove(tile)
        grid_taken[current_position[0]][current_position[1]] = True
        grid_taken[right_position[0]][right_position[1]] = True

        find_solution(grid_taken, tiles)

        tiles.add(tile)
        grid_taken[current_position[0]][current_position[1]] = False
        grid_taken[right_position[0]][right_position[1]] = False

    if down_position[0] < num_rows and \
       not grid_taken[down_position[0]][down_position[1]]:
      num1 = grid[current_position[0]][current_position[1]]
      num2 = grid[down_position[0]][down_position[1]]

      if num1 < num2:
        tile = (num1, num2)
      else:
        tile = (num2, num1)

      if tile in tiles:
        tiles.remove(tile)
        grid_taken[current_position[0]][current_position[1]] = True
        grid_taken[down_position[0]][down_position[1]] = True

        find_solution(grid_taken, tiles)

        tiles.add(tile)
        grid_taken[current_position[0]][current_position[1]] = False
        grid_taken[down_position[0]][down_position[1]] = False

  grid_taken = [[False] * num_cols for _ in range(num_rows)]

  find_solution(grid_taken, tiles)

  print(result)
