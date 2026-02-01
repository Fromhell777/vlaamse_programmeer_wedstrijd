
test_cases = int(input())

for t in range(test_cases):

  trips = int(input())

  stations = {}
  persons = {}

  for i in range(trips):
    person, start, stop = [int(x) for x in input().split()]

    already_visited_start = False
    already_visited_stop = False

    if person not in persons.keys():
      persons[person] = []

    if start not in persons[person]:
      persons[person].append(start)
    else:
      already_visited_start = True

    if stop not in persons[person]:
      persons[person].append(stop)
    else:
      already_visited_stop = True

    if not already_visited_start:
      if start in stations.keys():
        stations[start] += 1
      else:
        stations[start] = 1

    if not already_visited_stop:
      if stop in stations.keys():
        stations[stop] += 1
      else:
        stations[stop] = 1

  sorted_stations = sorted(stations.items(), key=lambda x:(-x[1], x[0]))

  print(f"{t + 1} {' '.join([str(station) + '(' + str(busy) + ')' for station, busy in sorted_stations])}")
