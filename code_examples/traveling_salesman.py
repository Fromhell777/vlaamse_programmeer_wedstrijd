
def traveling_salesman():

  graph = {}
  costs = {}

  graph = {1 : [2, 3, 4],
           2 : [1, 5],
           3 : [1, 4, 6],
           4 : [1, 3, 6, 7],
           5 : [2, 7],
           6 : [3, 4],
           7 : [4, 5]}

  costs = {(1, 2) : 4,
           (2, 1) : 4,
           (1, 3) : 3,
           (3, 1) : 3,
           (1, 4) : 2,
           (4, 1) : 2,
           (4, 3) : 5,
           (3, 4) : 5,
           (4, 6) : 1,
           (6, 4) : 1,
           (4, 7) : 7,
           (7, 4) : 7,
           (2, 5) : 5,
           (5, 2) : 5,
           (3, 6) : 4,
           (6, 3) : 4,
           (5, 7) : 1,
           (7, 5) : 1}

  start_node = 4
  to_visit = set(graph.keys())
  to_visit.remove(start_node)
  visited = [start_node]

  min_cost = 1e30

  cache_visited = {}

  def shortest_route(visited, to_visit, curr_node, curr_cost):
    nonlocal min_cost

    if len(to_visit) == 0:
      if (curr_node, start_node) in costs:
        extra_cost = costs[(curr_node, start_node)]
        min_cost = min(curr_cost + extra_cost, min_cost)
      return

    key = tuple(sorted(visited)) + (curr_node,)
    if key in cache_visited:
      if cache_visited[key] < curr_cost:
        return
    cache_visited[key] = curr_cost

    if curr_cost < min_cost:
      dists = []
      for new_node in to_visit:
        if (curr_node, new_node) in costs:
          dists.append((costs[(curr_node, new_node)], new_node))

      dists.sort()

      for _, new_node in dists:

        visited.append(new_node)
        to_visit.remove(new_node)

        extra_cost = costs[(curr_node, new_node)]

        shortest_route(visited, to_visit, new_node, curr_cost + extra_cost)

        visited.pop()
        to_visit.add(new_node)

  shortest_route(visited, to_visit, start_node, 0)

  return min_cost

def traveling_salesman_better_cache():

  graph = {}
  costs = {}

  graph = {1 : [2, 3, 4],
           2 : [1, 5],
           3 : [1, 4, 6],
           4 : [1, 3, 6, 7],
           5 : [2, 7],
           6 : [3, 4],
           7 : [4, 5]}

  costs = {(1, 2) : 4,
           (2, 1) : 4,
           (1, 3) : 3,
           (3, 1) : 3,
           (1, 4) : 2,
           (4, 1) : 2,
           (4, 3) : 5,
           (3, 4) : 5,
           (4, 6) : 1,
           (6, 4) : 1,
           (4, 7) : 7,
           (7, 4) : 7,
           (2, 5) : 5,
           (5, 2) : 5,
           (3, 6) : 4,
           (6, 3) : 4,
           (5, 7) : 1,
           (7, 5) : 1}

  node_to_index = {}
  for i, node in enumerate(graph.keys()):
    node_to_index[node] = i

  start_node = 4
  num_nodes = len(graph)

  # memoization for top down recursion
  memo = [[-1] * (1 << num_nodes) for _ in range(num_nodes)]

  def shortest_route(curr_node, mask):
    # base case
    # It implies we have visited all other nodes already
    if mask == 0:
      if (curr_node, start_node) in costs:
        return costs[(curr_node, start_node)]
      return 10**30

    # memoization
    curr_node_index = node_to_index[curr_node]
    if memo[curr_node_index][mask] != -1:
      return memo[curr_node_index][mask]

    result = 10**30  # result of this sub-problem

    # Choose a node and recurse deeper
    for new_node in graph[curr_node]:
      new_node_index = node_to_index[new_node]
      if (mask & (1 << new_node_index)) != 0:
        if (curr_node, new_node) in costs:
          extra_cost = costs[(curr_node, new_node)]
          new_mask = mask & (~(1 << new_node_index))
          result = min(result, shortest_route(new_node, new_mask) + extra_cost)

    memo[curr_node_index][mask] = result  # storing the minimum value

    return result

  result = shortest_route(start_node, ((1 << num_nodes) - 1) & ~(1 << node_to_index[start_node]))

  return result

def traveling_salesman_all_connections():

  nodes = ((1, 2),
           (2, 1),
           (1, 3),
           (3, 1),
           (1, 4),
           (4, 1),
           (2, 5),
           (5, 2),
           (3, 6),
           (6, 3),
           (5, 7),
           (7, 5))
  num_nodes = len(nodes)

  costs = [[0] * num_nodes for _ in range(num_nodes)]
  smallest_cost = {}

  for i in range(num_nodes):
    smallest = 1e30
    for j in range(num_nodes):
      x1, y1 = nodes[i]
      x2, y2 = nodes[j]
      cost = abs(x1 - x2)**2 + abs(y1 - y2)**2
      costs[i][j] = cost

      smallest = min(smallest, cost)

    smallest_cost[i] = smallest

  start_node = 0 # Doesn't really matter
  to_visit = set((i for i in range(1, num_nodes)))
  visited = [start_node]

  min_cost = 1e30

  cache_visited = {}

  def shortest_route(visited, to_visit, curr_node, curr_cost):
    nonlocal min_cost

    if len(to_visit) == 0:
      extra_cost = costs[curr_node][start_node]
      min_cost = min(curr_cost + extra_cost, min_cost)
      return

    key = tuple(sorted(visited)) + (curr_node,)
    if key in cache_visited:
      if cache_visited[key] < curr_cost:
        return
    cache_visited[key] = curr_cost

    min_extra_cost = smallest_cost[curr_node]
    for node in to_visit:
      min_extra_cost += smallest_cost[node]

    if curr_cost + min_extra_cost < min_cost:
      dists = []
      for new_node in to_visit:
        dists.append((costs[curr_node][new_node], new_node))

      dists.sort()

      for _, new_node in dists:

        visited.append(new_node)
        to_visit.remove(new_node)

        extra_cost = costs[curr_node][new_node]

        shortest_route(visited, to_visit, new_node, curr_cost + extra_cost)

        visited.pop()
        to_visit.add(new_node)

  shortest_route(visited, to_visit, start_node, 0)

  return min_cost

def traveling_salesman_all_connections_better_cache():

  nodes = ((1, 2),
           (2, 1),
           (1, 3),
           (3, 1),
           (1, 4),
           (4, 1),
           (2, 5),
           (5, 2),
           (3, 6),
           (6, 3),
           (5, 7),
           (7, 5))
  num_nodes = len(nodes)

  costs = [[0] * num_nodes for _ in range(num_nodes)]

  for i in range(num_nodes):
    for j in range(num_nodes):
      x1, y1 = nodes[i]
      x2, y2 = nodes[j]
      cost = abs(x1 - x2)**2 + abs(y1 - y2)**2
      costs[i][j] = cost

  start_node = 0

  # memoization for top down recursion
  memo = [[-1] * (1 << num_nodes) for _ in range(num_nodes)]

  def shortest_route(curr_node, mask):
    # base case
    # It implies we have visited all other nodes already
    if mask == 0:
      return costs[curr_node][start_node]

    # memoization
    if memo[curr_node][mask] != -1:
      return memo[curr_node][mask]

    result = 10**30  # result of this sub-problem

    # Choose a node and recurse deeper
    for new_node in range(1, num_nodes):
      if (mask & (1 << new_node)) != 0:
        extra_cost = costs[curr_node][new_node]
        new_mask = mask & (~(1 << new_node))
        result = min(result, shortest_route(new_node, new_mask) + extra_cost)

    memo[curr_node][mask] = result  # storing the minimum value

    return result

  result = shortest_route(start_node, (1 << num_nodes) - 2)

  return result

def traveling_salesman_all_connections_optimized():

  nodes = ((1, 2),
           (2, 1),
           (1, 3),
           (3, 1),
           (1, 4),
           (4, 1),
           (2, 5),
           (5, 2),
           (3, 6),
           (6, 3),
           (5, 7),
           (7, 5))
  num_nodes = len(nodes)

  costs = [[0] * num_nodes for _ in range(num_nodes)]

  for i in range(num_nodes):
    for j in range(num_nodes):
      x1, y1 = nodes[i]
      x2, y2 = nodes[j]
      cost = abs(x1 - x2)**2 + abs(y1 - y2)**2
      costs[i][j] = cost

  num_masks = 1 << (num_nodes - 1)
  full_mask = num_masks - 1
  inf = 2**32

  # dp[mask][i] = minimum cost to reach subset 'mask' and end at node i
  dp = [[inf] * num_nodes for _ in range(num_masks)]
  # parent[mask][i] = previous node before i in optimal path for (mask, i)
  parent = [[None] * num_nodes for _ in range(num_masks)]

  # Base case: start at node num_nodes - 1, mask = 1 << (num_nodes - 1)
  # We have a special setup case for node num_nodes - 1. Otherwise we have a lot of
  # recalculation of costs from node num_nodes - 1 while that's not possible
  dp[full_mask][num_nodes - 1] = 0
  for i in range(num_nodes - 1):
    mask = 1 << i
    dp[mask][i] = costs[num_nodes - 1][i]

  # Iterate over all subsets that include node num_nodes - 1
  for mask in range(1, num_masks):
    bit_1 = []
    for i in range(num_nodes):
      if mask & (1 << i):
        bit_1.append(i)

    for i in bit_1:
      prev_mask = mask ^ (1 << i)

      # Try all possibilities of coming to i from some j in prev_mask
      for j in bit_1:
        if i != j:
          cost = dp[prev_mask][j] + costs[j][i]
          if cost < dp[mask][i]:
            dp[mask][i] = cost
            parent[mask][i] = j

  # Close the tour: return to node num_nodes - 1
  min_cost = inf
  last = None
  for i in range(num_nodes - 1):
    cost = dp[full_mask][i] + costs[i][num_nodes - 1]
    if cost < min_cost:
      min_cost = cost
      last = i

  # Reconstruct path
  path = []
  mask = full_mask
  curr = last
  while curr is not None:
    path.append(curr)
    prev = parent[mask][curr]
    mask ^= (1 << curr)
    curr = prev

  path.append(num_nodes - 1) # add the start node
  path.reverse()             # reverse to get num_nodes - 1 -> ... -> last
  path.append(num_nodes - 1) # and return to num_nodes - 1

  return result, path

def traveling_salesman_with_required_streets():

  graph = {}
  costs = {}
  required = set()

  graph = {1 : [2, 3, 4],
           2 : [1, 5],
           3 : [1, 6],
           4 : [1],
           5 : [2, 7],
           6 : [3],
           7 : [5]}

  costs = {(1, 2) : 4,
           (2, 1) : 4,
           (1, 3) : 3,
           (3, 1) : 3,
           (1, 4) : 2,
           (4, 1) : 2,
           (2, 5) : 5,
           (5, 2) : 5,
           (3, 6) : 4,
           (6, 3) : 4,
           (5, 7) : 1,
           (7, 5) : 1}

  # These streets are required to be hit
  required = set([(1, 2),
                  (1, 4),
                  (3, 6)])

  start_cross = 3

  min_cost = 1e30
  curr_cost = 0

  def shortest_route(travelled, curr_cross):
    nonlocal min_cost
    nonlocal curr_cost

    copy_cost = curr_cost

    if curr_cost < min_cost:
      for new_cross in graph[curr_cross]:
        if (curr_cross, new_cross) not in travelled:

          travelled.add((curr_cross, new_cross))

          curr_cost += costs[(curr_cross, new_cross)]

          if new_cross == start_cross:
            hit_all_streets = True
            for street in required:
              if not (street in travelled or (street[1], street[0]) in travelled):
                hit_all_streets = False
                break

            if hit_all_streets:
              min_cost = min(curr_cost, min_cost)
            else:
              shortest_route(travelled, new_cross)
          else:
            shortest_route(travelled, new_cross)

          curr_cost = copy_cost

          travelled.remove((curr_cross, new_cross))

  shortest_route(set(), start_cross)

  return min_cost

# Driver Code
if __name__ == '__main__':

  result = traveling_salesman()
  print(f"Shortest route is: {result}")

  result = traveling_salesman_better_cache()
  print(f"Shortest route is: {result}")

  result = traveling_salesman_all_connections()
  print(f"Shortest route is: {result}")

  result = traveling_salesman_all_connections_better_cache()
  print(f"Shortest route is: {result}")

  result, path = traveling_salesman_all_connections_optimized()
  print(f"Shortest route is: {result}")
  print(f"Shortest path is: {path}")

  result = traveling_salesman_with_required_streets()
  print(f"Shortest route is: {result}")
