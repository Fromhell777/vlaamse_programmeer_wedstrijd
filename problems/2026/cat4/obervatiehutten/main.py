test_cases = int(input())

for t in range(test_cases):

  num_huts = int(input())

  huts = []
  for _ in range(num_huts):
    x, y = map(int, input().split())
    huts.append((x,y))

  costs = [[0] * num_huts for _ in range(num_huts)]

  for i in range(num_huts):
    for j in range(num_huts):
      x1, y1 = huts[i]
      x2, y2 = huts[j]
      cost = abs(x1 - x2)**2 + abs(y1 - y2)**2
      costs[i][j] = cost

  n = len(costs)
  num_masks = 1 << (n - 1)
  full_mask = num_masks - 1
  inf = 2**32 - 1

  # dp[mask][i] = minimum cost to reach subset 'mask' and end at node i
  dp = [[inf] * n for _ in range(num_masks)]

  # Base case: start at node n - 1, mask = 1 << (n - 1)
  # We have a special setup case for node n - 1. Otherwise we have a lot of
  # recalculation of costs from node n - 1 while that's not possible
  dp[full_mask][n - 1] = 0
  for i in range(n - 1):
    mask = 1 << i
    dp[mask][i] = costs[n - 1][i]

  # Iterate over all subsets that include node n - 1
  for mask in range(1, num_masks):
    bit_1 = []
    for i in range(n):
      if mask & (1 << i):
        bit_1.append(i)

    for i in bit_1:
      prev_mask = mask ^ (1 << i)

      # Try all possibilities of coming to i from some j in prev_mask
      for j in bit_1:
        if i != j:
          cost = dp[prev_mask][j] + costs[j][i]
          if cost < dp[mask][i]:
            dp[mask][i] = cost

  # Close the tour: return to node n - 1
  min_cost = inf
  for i in range(n - 1):
    min_cost = min(min_cost, dp[full_mask][i] + costs[i][n - 1])

  print(f"{t+1} {min_cost}")
