import math

test_cases = int(input())

for t in range(test_cases):

  x_size, y_size = [int(x) for x in input().split()]

  port = []
  for i in range(y_size):
     port.append([x for x in input()])

  expected_port = []
  for i in range(y_size):
     expected_port.append([x for x in input()])

  for i in range(y_size):
    for j in range(x_size):
      if (port[i][j] == '*'):
        start_position = (i,j)

  accasible_containers = set()

  visited = set()

  positions = [start_position]

  while len(positions) > 0:
    position = positions.pop()

    if position not in visited:
      visited.add(position)

      if position[0] - 1 >= 0:
        if port[position[0] - 1][position[1]] == '.':
          positions.append((position[0] - 1, position[1]))
        elif port[position[0] - 1][position[1]] != '*':
          accasible_containers.add((position[0] - 1, position[1]))

      if position[1] - 1 >= 0:
        if port[position[0]][position[1] - 1] == '.':
          positions.append((position[0], position[1] - 1))
        elif port[position[0]][position[1] - 1] != '*':
          accasible_containers.add((position[0], position[1] - 1))

      if position[0] + 1 < y_size:
        if port[position[0] + 1][position[1]] == '.':
          positions.append((position[0] + 1, position[1]))
        elif port[position[0] + 1][position[1]] != '*':
          accasible_containers.add((position[0] + 1, position[1]))

      if position[1] + 1 < x_size:
        if port[position[0]][position[1] + 1] == '.':
          positions.append((position[0], position[1] + 1))
        elif port[position[0]][position[1] + 1] != '*':
          accasible_containers.add((position[0], position[1] + 1))

  errors = 0

  for i in range(y_size):
    for j in range(x_size):
      if (port[i][j] != '*' and port[i][j] != '.'):
        if (port[i][j] != expected_port[i][j]):
          if (i,j) not in accasible_containers:
            errors += 1

  container_groups = []

  while len(accasible_containers) > 0:

    container_group = set()

    new_containers = [accasible_containers.pop()]

    while len(new_containers) > 0:
      container = new_containers.pop()

      if container not in container_group:
        container_group.add(container)

        if container[0] - 2 >= 0:
          if (container[0] - 1, container[1]) in visited and \
             port[container[0] - 2][container[1]] not in ['*', '.']:
            new_containers.append((container[0] - 2, container[1]))

            if (container[0] - 2, container[1]) in accasible_containers:
              accasible_containers.remove((container[0] - 2, container[1]))

        if container[1] - 2 >= 0:
          if (container[0], container[1] - 1) in visited and \
             port[container[0]][container[1] - 2] not in ['*', '.']:
            new_containers.append((container[0], container[1] - 2))

            if (container[0], container[1] - 2) in accasible_containers:
              accasible_containers.remove((container[0], container[1] - 2))

        if container[0] + 2 < y_size:
          if (container[0] + 1, container[1]) in visited and \
             port[container[0] + 2][container[1]] not in ['*', '.']:
            new_containers.append((container[0] + 2, container[1]))

            if (container[0] + 2, container[1]) in accasible_containers:
              accasible_containers.remove((container[0] + 2, container[1]))

        if container[1] + 2 < x_size:
          if (container[0], container[1] + 1) in visited and \
             port[container[0]][container[1] + 2] not in ['*', '.']:
            new_containers.append((container[0], container[1] + 2))

            if (container[0], container[1] + 2) in accasible_containers:
              accasible_containers.remove((container[0], container[1] + 2))

    container_groups.append(container_group)

  for container_group in container_groups:
    containers = {}
    expected_containers = {}

    for container in container_group:
      containers.setdefault(expected_port[container[0]][container[1]], 0)
      containers[expected_port[container[0]][container[1]]] += 1

      expected_containers.setdefault(port[container[0]][container[1]], 0)
      expected_containers[port[container[0]][container[1]]] += 1

    for container in expected_containers.keys():
      if container not in containers:
        errors += expected_containers[container]
      else:
        if containers[container] < expected_containers[container]:
          errors += expected_containers[container] - containers[container]

  print(f"{t + 1} {errors}")
