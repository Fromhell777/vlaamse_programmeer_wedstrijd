
test_cases = int(input())

for t in range(test_cases):

  num_streets, num_cross = [int(x) for x in input().split()]

  graph = {}
  costs = {}
  required = set()

  for _ in range(num_streets):
    cross0, cross1, cost, hit = [int(x) for x in input().split()]

    graph.setdefault(cross0, [])
    graph.setdefault(cross1, [])
    graph[cross0].append(cross1)
    graph[cross1].append(cross0)

    costs[(cross0, cross1)] = cost
    costs[(cross1, cross0)] = cost

    if hit:
      if cross0 < cross1:
        required.add((cross0, cross1))
      else:
        required.add((cross1, cross0))

  start_cross = int(input())

  min_cost = 1e30
  curr_cost = 0

  def shortest_route(travelled, curr_cross):
    global min_cost
    global curr_cost

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

  print(f"{t + 1} {min_cost}")
