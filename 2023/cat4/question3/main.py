import random

test_cases = int(input())

for t in range(test_cases):

  y_size, x_size = [int(x) for x in input().split()]

  matrix = []
  for i in range(y_size):
    matrix.append([int(x) for x in input().split()])

  start_positions = set()

  for i in range(y_size):
    for j in range(x_size):
      value = matrix[i][j]
      adjacent = 0
      if i > 0:
        if matrix[i - 1][j] == value:
          adjacent += 1
      if i + 1 < y_size:
        if matrix[i + 1][j] == value:
          adjacent += 1
      if j > 0:
        if matrix[i][j - 1] == value:
          adjacent += 1
      if j + 1 < x_size:
        if matrix[i][j + 1] == value:
          adjacent += 1

      if adjacent == 1:
        start_positions.add((i, j))

  connections = {}

  for i in range(y_size):
    for j in range(x_size):

      value = matrix[i][j]
      connections.setdefault(value, set())

      if i > 0:
        adjacent_value = matrix[i - 1][j]
        if not ((i, j) in start_positions and (i - 1, j) in start_positions):
          if adjacent_value != value and (i - 1, j):
            connections[value].add(adjacent_value)
      if i + 1 < y_size:
        adjacent_value = matrix[i + 1][j]
        if not ((i, j) in start_positions and (i + 1, j) in start_positions):
          if adjacent_value != value and (i + 1, j):
            connections[value].add(adjacent_value)
      if j > 0:
        adjacent_value = matrix[i][j - 1]
        if not ((i, j) in start_positions and (i, j - 1) in start_positions):
          if adjacent_value != value and (i, j - 1):
            connections[value].add(adjacent_value)
      if j + 1 < x_size:
        adjacent_value = matrix[i][j + 1]
        if not ((i, j) in start_positions and (i, j + 1) in start_positions):
          if adjacent_value != value and (i, j + 1):
            connections[value].add(adjacent_value)

  max_vhdl = 0
  curr_vdhl = 0

  solo_nodes = [k for k,v in connections.items() if len(v) == 1]
  chains = {}

  to_visit = set(connections.keys())

  while len(solo_nodes) > 0:
    solo_node = solo_nodes.pop()
    to_visit.remove(solo_node)

    prev_node = None
    length = 1

    travel = True
    while travel:
      new_connections = connections[solo_node]

      if len(new_connections) > 2:
        solo_node = prev_node
        length -= 1
        travel = False
        continue

      if solo_node in to_visit:
        to_visit.remove(solo_node)

      for node in new_connections:
        if prev_node != node:
          prev_node = solo_node
          solo_node = node
          if len(connections[solo_node]) == 1:
            travel = False
          break

      length += 1

    chains.setdefault(solo_node, 0)
    chains[solo_node] = length

  if len(chains) > 0 and next(iter(chains.values())) == len(connections):
    max_vhdl = next(iter(chains.values())) // 2
    if next(iter(chains.values())) % 2 == 1:
      max_vhdl += 1
    print(f"{t + 1} {max_vhdl}")
    continue

  max_chain_score = 0
  for length in chains.values():
    max_chain_score += length

  def color(colors, visited, to_visit):
    global max_vhdl
    global curr_vdhl

    if len(to_visit) + curr_vdhl + max_chain_score > max_vhdl:
      curr_node = to_visit.pop()
      visited.add(curr_node)
      adjacent_colors = 0
      for node in connections[curr_node]:
        adjacent_colors += colors[node]

      copy_vhdl = curr_vdhl

      if adjacent_colors == 0:
        colors[curr_node] = 1
        curr_vdhl += 1

        for node in connections[curr_node]:
          if node in chains.keys():
            curr_vdhl += chains[node] // 2

        if len(to_visit) > 0:
          color(colors, visited, to_visit)

      max_vhdl = max(curr_vdhl, max_vhdl)

      curr_vdhl = copy_vhdl

      colors[curr_node] = 0

      for node in connections[curr_node]:
        if node in chains.keys():
          curr_vdhl += chains[node] // 2
          if chains[node] % 2 == 1:
            curr_vdhl += 1

      max_vhdl = max(curr_vdhl, max_vhdl)

      if len(to_visit) > 0:
        color(colors, visited, to_visit)

      visited.remove(curr_node)
      to_visit.add(curr_node)

  color({k : 0 for k in connections.keys()}, set(), to_visit)

  print(f"{t + 1} {max_vhdl}")
