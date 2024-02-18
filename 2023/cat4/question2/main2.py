
test_cases = int(input())

for t in range(test_cases):

  size = int(input())

  edges = {}
  for i in range(size):
    left, right = [int(x) for x in input().split()]

    edges.setdefault(left, [])
    edges[left].append(right)
    edges.setdefault(right, [])
    edges[right].append(left)

  graphs = []

  loop_nodes = set(edges.keys())

  while len(loop_nodes) > 0:
    node = loop_nodes.pop()

    new_graph = set()
    new_graph.add(node)

    new_nodes = edges[node].copy()
    while len(new_nodes) > 0:
      new_node = new_nodes.pop()

      if new_node not in new_graph:
        new_graph.add(new_node)
        new_nodes.extend(edges[new_node])
        loop_nodes.remove(new_node)

    graphs.append(new_graph)

  bords = []

  for graph in graphs:
    solo_nodes = [i for i in graph if len(edges[i]) == 1]

    current_bords = []

    while len(solo_nodes) > 0:
      solo_node = solo_nodes.pop()

      if len(edges[solo_node]) > 0:
        connection = edges[solo_node][0]

        current_bords.append((connection, solo_node))

        edges[connection].remove(solo_node)

        if len(edges[connection]) == 1:
          solo_nodes.append(connection)
        elif len(edges[connection]) == 0:
          current_bords.extend([(i[1],i[0]) for i in current_bords])

    bords.extend(current_bords)

  if len(bords) > 0:
    print(f"{t + 1} {' '.join(['(' + str(i[0]) + ',' + str(i[1]) + ')' for i in sorted(bords)])}")
  else:
    print(f"{t + 1} geen")
