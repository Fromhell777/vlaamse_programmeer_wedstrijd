test_cases = int(input())

for _ in range(test_cases):

  num_busses = int(input())

  bus_routes = []
  for _ in range(num_busses):
    data = [int(x) for x in input().split()]
    bus_routes.append(data[1:])

  bus_knowledge = [set([i]) for i in range(num_busses)]

  bus_positions = [0] * num_busses
  done = False
  for i in range(1440):
    for j in range(num_busses):
      for k in range(num_busses):
        bus1 = bus_routes[j][bus_positions[j]]
        bus2 = bus_routes[k][bus_positions[k]]
        if bus1 == bus2 and j != k:
          bus_knowledge[j] = bus_knowledge[j].union(bus_knowledge[k])
          bus_knowledge[k] = bus_knowledge[k].union(bus_knowledge[j])

    if all([len(x) == num_busses for x in bus_knowledge]):
      print(i)
      done = True
      break

    for j in range(num_busses):
      bus_positions[j] += 1
      bus_positions[j] %= len(bus_routes[j])

  if not done:
    print("NOOIT")
