from queue import Queue

def breadth_first_search():

  graph = {1 : [2],
           2 : [1],
           3 : [4, 5],
           4 : [3, 5],
           5 : [3, 4]}

  start_node = 3

  visited = set()

  to_visit = Queue(maxsize = 0) # infinite size
  to_visit.put(start_node)

  while not to_visit.empty():
    new_node = to_visit.get_nowait()

    if new_node not in visited:
      visited.add(new_node)
      for node in graph[new_node]:
        to_visit.put(node)
