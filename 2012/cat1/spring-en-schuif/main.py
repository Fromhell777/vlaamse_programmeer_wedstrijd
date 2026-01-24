test_cases = int(input())

for _ in range(test_cases):

  turn, board = [x for x in input().split()]

  def count_moves(board, turn):
    shift = 0
    jump = 0
    for i, piece in enumerate(board):
      if piece == turn:

        if i + 1 < len(board) and board[i + 1] == 'L':
          shift += 1

        if i + 2 < len(board) and \
           board[i + 1] not in ('L' + turn) and \
           board[i + 2] == 'L':
          jump += 1

    return shift, jump

  if turn == 'W':
    shift, jump = count_moves(board, turn)
  else:
    shift, jump = count_moves(board[::-1], turn)

  print(f"{jump} {shift}")
