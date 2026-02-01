test_cases = int(input())

for t in range(test_cases):

  num_weights = int(input())

  weights = [int(x) for x in input().split()]

  target = int(input())

  reachable = set()

  found = False
  for i in range(num_weights):
    for j in range(i + 1, num_weights):
      if weights[i] + weights[j] == target:
        found = True
        break

    if found:
      break

  if found:
    print(f"{target} JA")
  else:
    print(f"{target} NEEN")
