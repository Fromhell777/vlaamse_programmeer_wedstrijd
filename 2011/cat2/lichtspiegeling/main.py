test_cases = int(input())

for _ in range(test_cases):

  num_rows, num_cols = [int(x) for x in input().split()]

  grid = []
  for _ in range(num_rows + 2):
    grid.append(input())

  def move_down(row, col):
    if row + 1 == num_rows + 1:
      return grid[row + 1][col]

    if grid[row + 1][col] == '/':
      return move_left(row + 1, col)
    elif grid[row + 1][col] == '\\':
      return move_right(row + 1, col)

    return move_down(row + 1, col)

  def move_up(row, col):
    if row - 1 == 0:
      return grid[row - 1][col]

    if grid[row - 1][col] == '/':
      return move_right(row - 1, col)
    elif grid[row - 1][col] == '\\':
      return move_left(row - 1, col)

    return move_up(row - 1, col)

  def move_left(row, col):
    if col - 1 == 0:
      return grid[row][col - 1]

    if grid[row][col - 1] == '/':
      return move_down(row, col - 1)
    elif grid[row][col - 1] == '\\':
      return move_up(row, col - 1)

    return move_left(row, col - 1)

  def move_right(row, col):
    if col + 1 == num_cols + 1:
      return grid[row][col + 1]

    if grid[row][col + 1] == '/':
      return move_up(row, col + 1)
    elif grid[row][col + 1] == '\\':
      return move_down(row, col + 1)

    return move_right(row, col + 1)

  correct = True
  for i in range(num_cols):
    start_char = grid[0][i + 1]

    end_char = move_down(0, i + 1)

    if start_char != end_char:
      correct = False
      break

  if correct:
    print("correct")
  else:
    print("verkeerd")
