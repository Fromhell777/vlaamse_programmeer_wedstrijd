test_cases = int(input())

for t in range(test_cases):

  num_components = int(input())

  components = [input() for _ in range(num_components)]

  nodes = set()
  for component in components:
    for char in component:
      if char not in ('E', 'O', 'W', 'L', 'D'):
        nodes.add(char)

  nodes = list(nodes)
  nodes.sort()
  start_node = nodes[0]
  end_node = nodes[-1]

  def check_solution(components):

    to_visit = [start_node]
    visited = set()

    # Do floodfill were we check if a lamp is present
    lamp = False
    while len(to_visit) > 0:
      new_node = to_visit.pop()

      if new_node not in visited:
        visited.add(new_node)
        for circuit in components:
          if circuit[1] == 'O':
            continue

          if new_node in circuit:
            pos = circuit.index(new_node)
            if pos == 0:
              to_visit.append(circuit[2])

            elif pos == 2:
              to_visit.append(circuit[0])

            if circuit[1] == 'L':
              lamp = True

    check_lamp_circuit = lamp and (end_node in visited)

    # Do floodfill to check for short circuit
    to_visit = [start_node]
    visited = set()

    # Do floodfill were we check if a lamp is present
    while len(to_visit) > 0:
      new_node = to_visit.pop()

      if new_node not in visited:
        visited.add(new_node)
        for circuit in components:
          if circuit[1] in ('O', 'L'):
            continue

          if new_node in circuit:
            pos = circuit.index(new_node)
            if pos == 0:
              to_visit.append(circuit[2])

            elif pos == 2:
              to_visit.append(circuit[0])

    check_short_circuit = end_node in visited

    return check_lamp_circuit and not check_short_circuit

  def get_solutions(components, current_component):

    if current_component == num_components:
      if check_solution(components):
        return [components.copy()]
      else:
        return []

    result = []

    circuit = components[current_component]

    if circuit[1] in ('E', 'O'):

      new_components = components.copy()
      new_components[current_component] = circuit[0] + 'E' + circuit[2]
      result.extend(get_solutions(new_components, current_component + 1))

      new_components[current_component] = circuit[0] + 'O' + circuit[2]
      result.extend(get_solutions(new_components, current_component + 1))

    elif circuit[1] == 'W':

      new_components = components.copy()
      new_components[current_component] = circuit[0] + 'W' + circuit[2:]
      result.extend(get_solutions(new_components, current_component + 1))

      new_components[current_component] = circuit[0] + 'W' + circuit[2:][::-1]
      result.extend(get_solutions(new_components, current_component + 1))

    else:

      result.extend(get_solutions(components, current_component + 1))

    return result

  result = get_solutions(components, 0)

  for components in result:
    components.sort()

  result.sort()

  if len(result) == 0:
    print(f"{t + 1} ONMOGELIJK")
  else:
    print(f"{t + 1} {', '.join([' '.join(components) for components in result])}")
