
def undirected_graph_cycle_detection(graph):

  start_node = next(iter(graph.keys()))

  visited = set()

  to_visit = [(start_node, start_node)]

  while len(to_visit) > 0:
    node, parent_node = to_visit.pop()

    if node not in visited:
      visited.add(node)
      for new_node in graph[node]:
        if new_node not in visited:
          to_visit.append((new_node, node))

        elif new_node != parent_node:
          return True

  return False

# Driver Code
if __name__ == '__main__':

  graph = {1 : [2],
           2 : [1, 3],
           3 : [2, 4, 5],
           4 : [3, 5],
           5 : [3, 4]}

  has_cycle = undirected_graph_cycle_detection(graph)

  if has_cycle:
    print("The graph contains a cylce")
  else:
    print("The graph contains no cylce")
