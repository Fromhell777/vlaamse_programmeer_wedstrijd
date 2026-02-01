test_cases = int(input())

for t in range(test_cases):

  start_weight = int(input())
  num_stops = int(input())

  distances = list(map(int, input().split()))
  drop_weights = list(map(int, input().split()))

  cost = 0
  current_weight = start_weight
  for i in range(num_stops):
    cost += current_weight * distances[i]
    if i < len(drop_weights) - 1:
      current_weight -= drop_weights[i]

  reverse_cost = 0
  current_weight = start_weight
  for i in range(num_stops):
    reverse_cost += current_weight * distances[::-1][i]
    if i < len(drop_weights) - 1:
      current_weight -= drop_weights[::-1][i]

  if cost <= reverse_cost:
    print(f"{start_weight} goed")
  else:
    print(f"{start_weight} omgekeerd")
