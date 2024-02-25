
test_cases = int(input())

for t in range(test_cases):

  moves = int(input())

  connections = {}

  for i in range(moves):
    wanted_houses = [x for x in input().split()]
    connections[wanted_houses[0]] = wanted_houses

  max_moves = 0
  curr_moves = 0

  to_visit = set(connections.keys())

  def occupy(occupied, visited, to_visit):
    global max_moves
    global curr_moves

    #if len(to_visit) + curr_moves + max_chain_score > max_moves:
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
            occupy(occupied, visited, to_visit)
          else:
            max_moves = max(curr_moves, max_moves)

          curr_moves = copy_moves
          occupied.remove(house)

      visited.remove(curr_house)
      to_visit.add(curr_house)

  occupy(set(), set(), to_visit)

  print(f"{t + 1} {max_moves}")
