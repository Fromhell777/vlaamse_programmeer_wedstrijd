
def backtracking():

  connections = {1 : [1, 2, 3],
                 2 : [2, 3],
                 3 : [3, 1]}

  max_moves = 0
  curr_moves = 0

  to_visit = set(connections.keys())

  def solve(occupied, visited, to_visit):
    nonlocal max_moves
    nonlocal curr_moves

    # Can be replaced by a branch cutting condition for extra speed up.
    # For example:
    #   if len(to_visit) + curr_moves > max_moves:
    if True:
      curr_house = to_visit.pop()
      visited.add(curr_house)

      copy_moves = curr_moves

      for house in connections[curr_house]:
        if house not in occupied:
          occupied.add(house)

          if house != curr_house:
            curr_moves += 1

          if len(to_visit) > 0:
            solve(occupied, visited, to_visit)
          else:
            max_moves = max(curr_moves, max_moves)

          curr_moves = copy_moves
          occupied.remove(house)

      visited.remove(curr_house)
      to_visit.add(curr_house)

  solve(set(), set(), to_visit)

  result = max_moves
