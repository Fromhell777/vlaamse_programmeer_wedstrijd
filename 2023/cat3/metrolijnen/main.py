import math
from queue import PriorityQueue

test_cases = int(input())

for t in range(test_cases):

  num_lines = int(input())

  nodes = {}

  for i in range(num_lines):
    data = [int(x) for x in input().split()]

    num_stations = data[0]
    stations = data[1:]

    for station in stations:
      nodes.setdefault(station, set())

      for j in stations:
        if j != station:
          nodes[station].add(j)

  num_trips = int(input())

  for i in range(num_trips):
    start, end = [int(x) for x in input().split()]


    if start == end:
      print(f"{t + 1} 0")
      continue

    visited_stations = {start : 0}
    new_stations = PriorityQueue()
    new_stations.put((0, start))

    found = False

    while new_stations.qsize() > 0 and not found:
      dist, station = new_stations.get()

      for j in nodes[station]:
        if j not in visited_stations:
          visited_stations[j] = dist + 1
          new_stations.put((dist + 1, j))
        else:
          old_dist = visited_stations[j]
          if old_dist > dist + 1:
            visited_stations[j] = dist + 1
            new_stations.put((dist + 1, j))

        if j == end:
          found = True
          print(f"{t + 1} {dist + 1}")
          break

    if not found:
      print(f"{t + 1} ONMOGELIJK")
