import heapq
from queue import PriorityQueue

test_cases = int(input())

for t in range(test_cases):

  num_streets = int(input())

  streets = []
  for i in range(num_streets):
    street = [int(x) for x in input().split()]

    x1 = street[0]
    y1 = street[1]
    x2 = street[2]
    y2 = street[3]

    point1 = (x1, y1)
    point2 = (x2, y2)

    street = [point1, point2]
    street.sort()

    streets.append(tuple(street))

  streets = set(tuple(streets))
  print(streets)

  start_point = tuple([int(x) for x in input().split()])
  end_point = tuple([int(x) for x in input().split()])

  streets_map = {street : i for i, street in enumerate(streets)}
  rev_map = {i : street for i, street in enumerate(streets)}


  graph = {}
  costs = {}

  for i, street in enumerate(streets):
    x1 = street[0][0]
    x2 = street[1][0]
    y1 = street[0][1]
    y2 = street[1][1]

    if street[0][0] == street[1][0]:
      new_point1 = (x1 + 1, y1 + 1)
      new_point2 = (x1 + 1, y1 + 1)
      current_cost = 0
      if (new_point1, new_point2) in streets:
        graph.setdefault(i, [])
        j = streets_map[(new_point1, new_point2)]
        graph[i].append(j)
        costs[(i, j)] = current_cost
        current_cost += 1

      new_point1 = (x1, y1 + 1)
      new_point2 = (x1, y1 + 2)
      if (new_point1, new_point2) in streets:
        graph.setdefault(i, [])
        j = streets_map[(new_point1, new_point2)]
        graph[i].append(j)
        costs[(i, j)] = current_cost
        current_cost += 1

      new_point1 = (x1 - 1, y1 + 1)
      new_point2 = (x1, y1 + 1)
      if (new_point1, new_point2) in streets:
        graph.setdefault(i, [])
        j = streets_map[(new_point1, new_point2)]
        graph[i].append(j)
        costs[(i, j)] = current_cost
        current_cost += 1

      new_point1 = (x1 - 1, y1)
      new_point2 = (x1, y1)
      current_cost = 0
      if (new_point1, new_point2) in streets:
        graph.setdefault(i, [])
        j = streets_map[(new_point1, new_point2)]
        graph[i].append(j)
        costs[(i, j)] = current_cost
        current_cost += 1

      new_point1 = (x1, y1 - 1)
      new_point2 = (x1, y1)
      if (new_point1, new_point2) in streets:
        graph.setdefault(i, [])
        j = streets_map[(new_point1, new_point2)]
        graph[i].append(j)
        costs[(i, j)] = current_cost
        current_cost += 1

      new_point1 = (x1, y1)
      new_point2 = (x1 + 1, y1)
      if (new_point1, new_point2) in streets:
        graph.setdefault(i, [])
        j = streets_map[(new_point1, new_point2)]
        graph[i].append(j)
        costs[(i, j)] = current_cost
        current_cost += 1

    if street[0][1] == street[1][1]:
      new_point1 = (x1 + 1, y1 - 1)
      new_point2 = (x1 + 1, y1)
      current_cost = 0
      if (new_point1, new_point2) in streets:
        graph.setdefault(i, [])
        j = streets_map[(new_point1, new_point2)]
        graph[i].append(j)
        costs[(i, j)] = current_cost
        current_cost += 1

      new_point1 = (x1 + 1, y1)
      new_point2 = (x1 + 2, y1)
      if (new_point1, new_point2) in streets:
        graph.setdefault(i, [])
        j = streets_map[(new_point1, new_point2)]
        graph[i].append(j)
        costs[(i, j)] = current_cost
        current_cost += 1

      new_point1 = (x1 + 1, y1)
      new_point2 = (x1 + 1, y1 + 1)
      if (new_point1, new_point2) in streets:
        graph.setdefault(i, [])
        j = streets_map[(new_point1, new_point2)]
        graph[i].append(j)
        costs[(i, j)] = current_cost
        current_cost += 1

      new_point1 = (x1, y1)
      new_point2 = (x1, y1 + 1)
      current_cost = 0
      if (new_point1, new_point2) in streets:
        graph.setdefault(i, [])
        j = streets_map[(new_point1, new_point2)]
        graph[i].append(j)
        costs[(i, j)] = current_cost
        current_cost += 1

      new_point1 = (x1 - 1, y1)
      new_point2 = (x1, y1)
      if (new_point1, new_point2) in streets:
        graph.setdefault(i, [])
        j = streets_map[(new_point1, new_point2)]
        graph[i].append(j)
        costs[(i, j)] = current_cost
        current_cost += 1

      new_point1 = (x1, y1 - 1)
      new_point2 = (x1, y1)
      if (new_point1, new_point2) in streets:
        graph.setdefault(i, [])
        j = streets_map[(new_point1, new_point2)]
        graph[i].append(j)
        costs[(i, j)] = current_cost
        current_cost += 1

  print(graph)
  print(costs)

  start_streets = [street for street in streets if start_point in street]
  end_streets = [street for street in streets if end_point in street]

  init_large_value = 1e10

  result = init_large_value
  found = False

  print(start_streets)
  print(end_streets)
  for start_street in start_streets:
    for end_street in end_streets:

      start_node = streets_map[start_street]
      end_node = streets_map[end_street]

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
          found = True
          break

        if node not in visited:
          visited.add(node)

          for connected_node in graph[node]:
            if connected_node not in visited:
              extra_cost = costs[(node, connected_node)]
              print(extra_cost)
              if dist[connected_node] > dist[node] + extra_cost:
                dist[connected_node] = dist[node] + extra_cost
                heapq.heappush(queue, (dist[connected_node], connected_node))

      result = min(result, shortest_dist)

  if found:
    print(f"{t + 1} {result}")
  else:
    print(f"{t + 1} ONMOGELIJK")
