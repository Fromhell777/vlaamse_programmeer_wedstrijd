
test_cases = int(input())

for t in range(test_cases):

  size = int(input())

  edges = {}
  for i in range(size):
    left, right = [int(x) for x in input().split()]

    edges.setdefault(left, [])
    edges[left].append(right)
    edges.setdefault(right, [])
    edges[right].append(left)

  bords = []
  inverse_bords = {}

  found_solo = False
  for k, v in edges.items():
    if len(v) == 1:
      solo_node = k
      found_solo = True

  while found_solo:

    while solo_node is not None:
      connection = edges[solo_node][0]

      bords.append((connection, solo_node))
      inverse_bords.setdefault(solo_node, [])
      inverse_bords[solo_node].append((solo_node, connection))

      inverse_bords.setdefault(connection, [])
      inverse_bords[connection].extend(inverse_bords[solo_node])

      edges[connection].remove(solo_node)

      del edges[solo_node]

      if len(edges[connection]) == 1:
        solo_node = connection
      elif len(edges[connection]) == 0:
        bords.extend(inverse_bords[connection])
        solo_node = None
      else:
        solo_node = None

    found_solo = False
    for k, v in edges.items():
      if len(v) == 1:
        solo_node = k
        found_solo = True

  if len(bords) > 0:
    print(f"{t + 1} {' '.join(['(' + str(i[0]) + ',' + str(i[1]) + ')' for i in sorted(bords)])}")
  else:
    print(f"{t + 1} geen")
