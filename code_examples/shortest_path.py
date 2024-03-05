import heapq
from queue import PriorityQueue

def shortest_path_priority_queue():

  graph = {1 : [2],
           2 : [1],
           3 : [4, 5],
           4 : [3, 5],
           5 : [3, 4]}

  costs = {(1,2) : 1,
           (2,1) : 1,
           (3,5) : 1,
           (3,4) : 1,
           (4,3) : 1,
           (4,5) : 1,
           (5,3) : 1,
           (5,4) : 1}

  start_node = 3
  end_node = 5

  init_large_value = 1e10

  dist = {k : init_large_value for k in graph.keys()}
  dist[start_node] = 0

  visited = set()
  q = PriorityQueue()
  q.put((0, start_node))

  shortest_dist = init_large_value

  while not q.empty():
    cost, node = q.get()

    if node == end_node:
      shortest_dist = dist[node]
      break

    if node not in visited:
      visited.add(node)

      for connected_node in nodes[node]:
        if connected_node not in visited:
          extra_cost = costs[(node, connected_node)]
          if dist[connected_node] > dist[node] + extra_cost:
            dist[connected_node] = dist[node] + extra_cost
            q.put((dist[connected_node], connected_node))

def shortest_path_heap_queue():

  graph = {1 : [2],
           2 : [1],
           3 : [4, 5],
           4 : [3, 5],
           5 : [3, 4]}

  costs = {(1,2) : 1,
           (2,1) : 1,
           (3,5) : 1,
           (3,4) : 1,
           (4,3) : 1,
           (4,5) : 1,
           (5,3) : 1,
           (5,4) : 1}

  start_node = 3
  end_node = 5

  init_large_value = 1e10

  dist = {k : init_large_value for k in graph.keys()}
  dist[start_node] = 0

  visited = set()
  queue = []
  heapq.heappush(queue, (0, start_node))

  shortest_dist = init_large_value

  while len(queue) > 0:
    cost, node = heapq.heappop(queue)

    if node == end_node:
      shortest_dist = dist[node]
      break

    if node not in visited:
      visited.add(node)

      for connected_node in nodes[node]:
        if connected_node not in visited:
          extra_cost = costs[(node, connected_node)]
          if dist[connected_node] > dist[node] + extra_cost:
            dist[connected_node] = dist[node] + extra_cost
            heapq.heappush(queue, (dist[connected_node], connected_node))
