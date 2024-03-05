
def minimax0(curDepth, nodeIndex, maxTurn, scores, targetDepth):

  # base case : targetDepth reached
  if curDepth == targetDepth:
    return scores[nodeIndex]

  if maxTurn:
    return max(minimax0(curDepth    = curDepth + 1,
                        nodeIndex   = nodeIndex * 2,
                        maxTurn     = False,
                        scores      = scores,
                        targetDepth = targetDepth),
               minimax0(curDepth    = curDepth + 1,
                        nodeIndex   = nodeIndex * 2 + 1,
                        maxTurn     = False,
                        scores      = scores,
                        targetDepth = targetDepth))

  else:
    return min(minimax0(curDepth    = curDepth + 1,
                        nodeIndex   = nodeIndex * 2,
                        maxTurn     = True,
                        scores      = scores,
                        targetDepth = targetDepth),
               minimax0(curDepth    = curDepth + 1,
                        nodeIndex   = nodeIndex * 2 + 1,
                        maxTurn     = True,
                        scores      = scores,
                        targetDepth = targetDepth))

def minimax1(win_numbers, a_values, b_values, start_number):

  max_value = max(win_numbers)

  def solve(curr_value, a_turn):
    if a_turn:
      player_values = a_values
    else:
      player_values = b_values

    # Base condition
    if curr_value in win_numbers:
      if a_turn:
        return "B", set([curr_value])
      else:
        return "A", set([curr_value])

    win_data = {}

    for value in player_values:
      next_value = curr_value + value

      if next_value <= max_value:
        winner, winning_numbers = solve(next_value, not a_turn)
        win_data.setdefault(winner, set())
        win_data[winner].update(winning_numbers)

    if len(win_data) == 0:
      return "ex aequo", set()
    elif len(win_data) == 1:
      return next(iter(win_data.keys())), next(iter(win_data.values()))
    elif a_turn and "A" in win_data:
      return "A", win_data["A"]
    elif not a_turn and "B" in win_data:
      return "B", win_data["B"]
    else:
      return "ex aequo", set()

  return solve(start_number, True)

# Driver code
if __name__ == '__main__':
  # Tesing the minimax algorithm on the simple game
  scores = [3, 5, 2, 9, 12, 5, 23, 23]

  treeDepth = (len(scores) - 1).bit_length()

  result = minimax0(curDepth    = 0,
                    nodeIndex   = 0,
                    maxTurn     = True,
                    scores      = scores,
                    targetDepth = treeDepth)

  print(f"The optimal value is : {result}")

  # Tesing the minimax algorithm on the Nim variant game
  win_numbers = [100, 107, 118, 134, 154, 171,
                 182, 201, 206, 224, 227, 247]

  a_values     = [7, 11]
  b_values     = [7, 11]
  start_number = 97

  winner, winning_numbers = minimax1(win_numbers  = win_numbers,
                                     a_values     = a_values,
                                     b_values     = b_values,
                                     start_number = start_number)

  if winner == "ex aequo":
    print(f"Nim variant result: {winner}")
  else:
    print(f"Nim variant result: player {winner} wins " + \
          f"with winning numbers {winning_numbers}")
