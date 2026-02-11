import time

test_cases = int(input())

for t in range(test_cases):
  start = time.perf_counter()

  num_huts = int(input())

  huts = []
  for _ in range(num_huts):
    x, y = map(int, input().split())
    huts.append((x,y))

  costs = [[0]*num_huts for _ in range(num_huts)]
  all_costs = []

  for i in range(num_huts):
    for j in range(num_huts):
      x1, y1 = huts[i]
      x2, y2 = huts[j]
      cost = (max(x1,x2) - min(x1,x2))**2 + (max(y1,y2) - min(y1,y2))**2
      costs[i][j] = cost
      if i != j and i < j:
        all_costs.append(cost)

  all_costs.sort()

  start_cross = 0

  min_cost = 1e30
  curr_cost = 0

  # best_by_len = {}

  best_by_travelled = {}

  def shortest_route(travelled, curr_cross):
    global min_cost
    global curr_cost

    if time.perf_counter()  - start > 0.1:
      return

    copy_cost = curr_cost

    key = tuple(sorted(travelled)) + (curr_cross,)
    if key in best_by_travelled:
      if best_by_travelled[key] < curr_cost:
        return
    best_by_travelled[key] = curr_cost

    nodes_left = num_huts - len(travelled)

    heur = sum(all_costs[:nodes_left])

    if curr_cost + heur < min_cost:
      dists = []
      for i in range(num_huts):
        if i == curr_cross:
          continue
        dists.append((costs[i][curr_cross], i))

      dists.sort()

      for _, new_cross in dists:
        if new_cross not in travelled:

          travelled.add(new_cross)

          curr_cost += costs[curr_cross][new_cross]

          shortest_route(travelled, new_cross)

          if len(travelled) == num_huts:
            curr_cost += costs[start_cross][new_cross]
            min_cost = min(curr_cost, min_cost)

          curr_cost = copy_cost

          travelled.remove(new_cross)

  shortest_route(set([start_cross]), start_cross)

  print(f"{t+1} {min_cost}")
