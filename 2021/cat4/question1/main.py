
test_cases = int(input())

for t in range(test_cases):

  budget, num_bars = [int(x) for x in input().split()]

  costs = []
  scores = []

  for _ in range(num_bars):
    cost, score = [int(x) for x in input().split()]
    costs.append(cost)
    scores.append(score)

  # Making the dp array
  dp = [0 for _ in range(budget + 1)]

  # Taking first i elements
  for i in range(1, len(scores) + 1):

    # Starting from back,
    # so that we also have data of
    # previous computation when taking i - 1 items
    for w in range(budget, 0, -1):
      if costs[i - 1] <= w:

        # Finding the maximum value
        dp[w] = max(scores[i - 1] + dp[w - costs[i - 1]], dp[w])

  print(f"{t + 1} {dp[budget]}")
