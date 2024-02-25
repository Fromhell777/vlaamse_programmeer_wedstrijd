
test_cases = int(input())

for t in range(test_cases):

  size = int(input())

  left, right = [int(x) for x in input().split()]

  edges = {}
  for i in range(size):

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


  print(f"{t + 1} {' '.join(['(' + str(i[0]) + ',' + str(i[1]) + ')' for i in sorted(bords)])}")
