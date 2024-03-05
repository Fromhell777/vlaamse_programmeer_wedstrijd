
def detect_forest():

  graph = {1 : [2],
           2 : [1],
           3 : [4, 5],
           4 : [3, 5],
           5 : [3, 4]}

  graphs = []

  all_nodes = set(graph.keys())

  while len(all_nodes) > 0:
    node = all_nodes.pop()

    sub_graph = set()
    sub_graph.add(node)

    new_nodes = edges[node].copy()
    while len(new_nodes) > 0:
      new_node = new_nodes.pop()

      if new_node not in sub_graph:
        sub_graph.add(new_node)
        new_nodes.extend(edges[new_node])
        all_nodes.remove(new_node)

    graphs.append(sub_graph)
