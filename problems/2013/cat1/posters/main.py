test_cases = int(input())

for t in range(test_cases):

  num_posters = int(input())

  posters = []
  max_length = 0
  for _ in range(num_posters):
    poster = list(map(int, input().split()))
    poster[0] -= 1
    posters.append(poster)
    max_length = max(max_length, sum(poster))

  board = [-1] * max_length

  for poster_number, poster in enumerate(posters):
    for i in range(poster[0], poster[0] + poster[1]):
      board[i] = poster_number

  unique_board = set(board)
  result = len(unique_board)
  if -1 in unique_board:
    result -= 1

  print(result)
