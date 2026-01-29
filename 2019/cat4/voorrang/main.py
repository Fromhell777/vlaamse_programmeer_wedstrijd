import math

test_cases = int(input())

for t in range(test_cases):

  num_streets = int(input())

  graph = {}

  for _ in range(num_streets):
    x1, y1, x2, y2 = [int(x) for x in input().split()]
    point1 = (x1,y1)
    point2 = (x2,y2)

    graph.setdefault(point1, [])
    graph[point1].append(point2)
    graph.setdefault(point2, [])
    graph[point2].append(point1)

  data = [int(x) for x in input().split()]
  start_point = tuple(data)

  data = [int(x) for x in input().split()]
  end_point = tuple(data)

  next_point = graph[start_point][0]
  all_moves = [[next_point, start_point, 0]]

  def rotate(center_point, point):
    translate_point = [point[0] - center_point[0], point[1] - center_point[1]]
    rotate_point = [-translate_point[1], translate_point[0]]
    return (rotate_point[0] + center_point[0], rotate_point[1] + center_point[1])

  costs = {}
  for point in graph.keys():
    costs[point] = {}

    if len(graph[point]) > 0:

      connected_point = graph[point][0]
      for _ in range(4):
        costs[point][connected_point] = math.inf
        connected_point = rotate(point, connected_point)

  while len(all_moves) > 0:
    current_point, prev_point, current_cost = all_moves.pop()

    move_cost = 0
    next_point = prev_point
    for _ in range(3):
      next_point = rotate(current_point, next_point)
      if next_point in graph[current_point]:
        new_cost = current_cost + move_cost
        if new_cost < costs[next_point][current_point]:
          costs[next_point][current_point] = new_cost
          all_moves.append([next_point, current_point, new_cost])
        move_cost += 1

  if end_point in graph:
    second_to_last_point = graph[end_point][0]

    if costs[end_point][second_to_last_point] < math.inf:
      print(f"{t + 1} {costs[end_point][second_to_last_point]}")
    else:
      print(f"{t + 1} ONMOGELIJK")
  else:
    print(f"{t + 1} ONMOGELIJK")
