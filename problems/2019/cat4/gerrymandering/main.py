import functools

test_cases = int(input())

for t in range(test_cases):

  num_cols, num_rows = map(int, input().split())

  grid = []
  for _ in range(num_rows):
    row = list(input())
    row = [x.replace('A', '1') for x in row]
    row = [x.replace('B', "-1") for x in row]

    row = [int(x) for x in row]
    grid.append(row)

  def get_winner(votes):
    winner = sum(votes)

    if winner > 0:
      return 1, 0, 0
    elif winner < 0:
      return 0, 0, -1

    return 0, 1, 0

  @functools.cache
  def find_best_separation(start_row, start_col, end_row, end_col):

    if (start_row > end_row) or (start_col > end_col):
      return (0, 0, 0)

    new_results = []

    extra_win, extra_equal, extra_loss = get_winner(grid[start_row][start_col:end_col + 1])
    win, equal, loss = find_best_separation(start_row + 1, start_col, end_row, end_col)
    new_results.append((win + extra_win, equal + extra_equal, loss + extra_loss))

    extra_win, extra_equal, extra_loss = get_winner(grid[end_row][start_col:end_col + 1])
    win, equal, loss = find_best_separation(start_row, start_col, end_row - 1, end_col)
    new_results.append((win + extra_win, equal + extra_equal, loss + extra_loss))

    extra_win, extra_equal, extra_loss = get_winner([grid[x][start_col] for x in range(start_row, end_row + 1)])
    win, equal, loss = find_best_separation(start_row, start_col + 1, end_row, end_col)
    new_results.append((win + extra_win, equal + extra_equal, loss + extra_loss))

    extra_win, extra_equal, extra_loss = get_winner([grid[x][end_col] for x in range(start_row, end_row + 1)])
    win, equal, loss = find_best_separation(start_row, start_col, end_row, end_col - 1)
    new_results.append((win + extra_win, equal + extra_equal, loss + extra_loss))

    return max(new_results)

  win, equal, loss = find_best_separation(0, 0, num_rows - 1, num_cols - 1)

  print(f"{t + 1} {win} {equal} {-loss}")
