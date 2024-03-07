from queue import PriorityQueue

test_cases = int(input())

for t in range(test_cases):

  data = [x for x in input().split()]

  moves = []
  for i in range(len(data) // 2):
    moves.append((int(data[2 * i]), data[2 * i + 1]))

  curr_node = (0,0)
  nodes = {curr_node : []}
  for move in moves:
    for i in range(move[0]):
      if move[1] == "W":
        new_node = (curr_node[0] - 1, curr_node[1])
      elif move[1] == "N":
        new_node = (curr_node[0], curr_node[1] + 1)
      elif move[1] == "O":
        new_node = (curr_node[0] + 1, curr_node[1])
      elif move[1] == "Z":
        new_node = (curr_node[0], curr_node[1] - 1)

      nodes.setdefault(new_node, [])
      nodes[new_node].append(curr_node)
      nodes[curr_node].append(new_node)

      curr_node = new_node

  start_node = (0,0)
  end_node = curr_node

  dist = {k : 1e10 for k in nodes.keys()}
  dist[start_node] = 0

  visited = set()
  q = PriorityQueue()
  q.put((0, start_node))

  shortest_dist = 1e10

  while not q.empty():
    cost, node = q.get()

    if node == end_node:
      shortest_dist = dist[node]
      break

    if node not in visited:
      visited.add(node)

      for adjacent_node in nodes[node]:
        if adjacent_node not in visited:
          if dist[adjacent_node] > dist[node] + 1:
            dist[adjacent_node] = dist[node] + 1
            q.put((dist[adjacent_node], adjacent_node))

  print(f"{t + 1} {shortest_dist}")
