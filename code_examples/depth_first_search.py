
def depth_first_search():

  graph = {1 : [2],
           2 : [1],
           3 : [4, 5],
           4 : [3, 5],
           5 : [3, 4]}

  start_node = 3

  visited = set()

  to_visit = [start_node]

  while len(to_visit) > 0:
    new_node = to_visit.pop()

    if new_node not in visited:
      visited.add(new_node)
      to_visit.extend(graph[new_node])
