
def traveling_salesman():

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
