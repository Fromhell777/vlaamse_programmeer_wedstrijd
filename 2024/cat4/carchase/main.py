from queue import PriorityQueue

test_cases = int(input())

for t in range(test_cases):

  start_bad, end_bad, start_pol, num_vertices, num_edges = [int(x) for x in input().split()]

  graph = {k : [] for k in range(num_vertices + 1)}

  costs = {}

  for i in range(num_edges):
    start, end, cost = [int(x) for x in input().split()]
    costs[(start, end)] = cost
    graph.setdefault(start, [])
    graph[start].append(end)

  init_large_value = 1e10

  dist = {k : init_large_value for k in graph.keys()}
  dist[start_bad] = 0

  prev = {k : None for k in graph.keys()}
  prev[start_bad] = start_bad

  visited = set()
  q = PriorityQueue()
  q.put((0, start_bad))

  shortest_dist = init_large_value

  while not q.empty():
    cost, node = q.get()

    if node == end_bad:
      shortest_dist = dist[node]
      break

    if node not in visited:
      visited.add(node)

      for connected_node in graph[node]:
        if connected_node not in visited:
          extra_cost = costs[(node, connected_node)]
          if dist[connected_node] > dist[node] + extra_cost:
            dist[connected_node] = dist[node] + extra_cost
            prev[connected_node] = node
            q.put((dist[connected_node], connected_node))

  if prev[end_bad] == None:
    bad_path = []
  else:
    bad_path = [end_bad]
    while start_bad != end_bad:
      end_bad = prev[end_bad]
      bad_path.append(end_bad)

    bad_path.reverse()

  bad_cost = {}
  cur_cost = 0

  for i in range(1, len(bad_path)):
    cur_cost += costs[(bad_path[i - 1], bad_path[i])]
    bad_cost[bad_path[i]] = cur_cost

  pol_goal_nodes = set(bad_path[1:])

  dist = {k : init_large_value for k in graph.keys()}
  dist[start_pol] = 0

  prev = {k : None for k in graph.keys()}
  prev[start_pol] = start_pol

  visited = set()
  q = PriorityQueue()
  q.put((0, start_pol))

  shortest_dist = init_large_value
  intercept_node = None
  curr_min_bad_cost = init_large_value

  while not q.empty():
    cost, node = q.get()

    if node in pol_goal_nodes:
      if dist[node] > shortest_dist:
        break

      if dist[node] <= bad_cost[node] - 2:
        shortest_dist = dist[node]
        node_bad_cost = bad_cost[node]
        if node_bad_cost < curr_min_bad_cost:
          intercept_node = node
          curr_min_bad_cost = node_bad_cost

    if node not in visited:
      visited.add(node)

      for connected_node in graph[node]:
        if connected_node not in visited:
          extra_cost = costs[(node, connected_node)]
          if dist[connected_node] > dist[node] + extra_cost:
            dist[connected_node] = dist[node] + extra_cost
            prev[connected_node] = node
            q.put((dist[connected_node], connected_node))

  if intercept_node is None:
    print(f"{t + 1} ONMOGELIJK")
  else:
    print(f"{t + 1} {intercept_node} {shortest_dist}")
