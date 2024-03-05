
def detect_chains():

  graph = {1 : [2],
           2 : [1],
           3 : [4, 5],
           4 : [3, 5],
           5 : [3, 4]}

  solo_nodes = [k for k,v in graph.items() if len(v) == 1]
  chains = {}

  while len(solo_nodes) > 0:
    solo_node = solo_nodes.pop()

    prev_node = None
    length = 1

    travel = True
    while travel:
      new_connections = graph[solo_node]

      for node in new_connections:
        if prev_node != node:
          prev_node = solo_node
          new_node = node
          break

      if len(graph[new_node]) <= 2:
        length += 1
        solo_node = new_node

      if len(graph[new_node]) != 2:
        travel = False

    chains.setdefault(solo_node, 0)
    chains[solo_node] = length
