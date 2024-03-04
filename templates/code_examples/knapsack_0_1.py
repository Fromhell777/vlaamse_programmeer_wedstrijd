
def knapsack_0_1_recursive(max_weight, weights, values, num_items):

  # Base Case
  if num_items == 0 or max_weight == 0:
    return 0, []

  # If weight of the nth item is more than knapsack of capacity max_weight, then
  # this item cannot be included in the optimal solution
  if (weights[num_items - 1] > max_weight):
    return knapsack_0_1_recursive(weights = weights,
                                  values = values,
                                  max_weight = max_weight,
                                  num_items = num_items - 1)

  # return the maximum of two cases:
  # (1) the item at index num_items can be included
  # (2) not included
  else:
    value0, items0 = knapsack_0_1_recursive(weights = weights,
                                            values = values,
                                            max_weight = max_weight - weights[num_items - 1],
                                            num_items = num_items - 1)
    value0 += values[num_items - 1]
    items0.append(num_items - 1)

    value1, items1 = knapsack_0_1_recursive(weights = weights,
                                            values = values,
                                            max_weight = max_weight,
                                            num_items = num_items - 1)
    return (value0, items0) if value0 >= value1 else (value1, items1)

# Create a memoization matrix:
# mem = [[None for _ in range(len(values) + 1)] for _ in range(max_weight + 1)]
def knapsack_0_1_recursive_memoization(weights, values, max_weight, num_items):

  # Base Case
  if num_items == 0 or max_weight == 0:
    return (0, [])

  if mem[max_weight][num_items] != None:
    return mem[max_weight][num_items]

  # If weight of the nth item is more than knapsack of capacity max_weight, then
  # this item cannot be included in the optimal solution
  if (weights[num_items - 1] > max_weight):
    mem[max_weight][num_items] = knapsack_0_1_recursive_memoization(weights = weights,
                                                                    values = values,
                                                                    max_weight = max_weight,
                                                                    num_items = num_items - 1)
    return mem[max_weight][num_items]

  # return the maximum of two cases:
  # (1) the item at index num_items can be included
  # (2) not included
  else:
    value0, items0 = knapsack_0_1_recursive_memoization(weights = weights,
                                                        values = values,
                                                        max_weight = max_weight - weights[num_items - 1],
                                                        num_items = num_items - 1)
    value0 += values[num_items - 1]
    items0.append(num_items - 1)

    value1, items1 = knapsack_0_1_recursive_memoization(weights = weights,
                                                        values = values,
                                                        max_weight = max_weight,
                                                        num_items = num_items - 1)
    if value0 >= value1:
      mem[max_weight][num_items] = (value0, items0)
    else:
      mem[max_weight][num_items] = (value1, items1)

    return mem[max_weight][num_items]

def knapsack_0_1_bottom_up0(weights, values, max_weight, num_items):
  # Making the dp matrix
  dp = [[0 for _ in range(num_items + 1)] for _ in range(max_weight + 1)]

  # Build table dp[][] in a bottom-up manner
  for i in range(num_items + 1):
    for w in range(max_weight + 1):
      if i == 0 or w == 0:
        dp[w][i] = 0
      elif weights[i - 1] <= w:
        dp[w][i] = max(values[i - 1] + dp[w - weights[i - 1]][i - 1],
                       dp[w][i - 1])
      else:
        dp[w][i] = dp[w][i - 1]

  # Get items making up the optimal solution
  optimal_items = []

  curr_max_weight = max_weight

  for i in range(num_items, 0, -1):
    if dp[curr_max_weight][i] > dp[curr_max_weight][i - 1]:
      optimal_items.append(i - 1)
      curr_max_weight -= weights[i - 1]

  return dp[max_weight][num_items], optimal_items

def knapsack_0_1_bottom_up1(weights, values, max_weight, num_items):
  # Making the dp matrix
  dp = [[(0, []) for _ in range(num_items + 1)] for _ in range(max_weight + 1)]

  # Build table dp[][] in a bottom-up manner
  for i in range(num_items + 1):
    for w in range(max_weight + 1):
      if i == 0 or w == 0:
        dp[w][i] = (0, [])
      elif weights[i - 1] <= w:
        value0, items0 = dp[w - weights[i - 1]][i - 1]
        value0 += values[i - 1]
        items0.append(i - 1)

        value1, items1 = dp[w][i - 1]

        if value0 >= value1:
          dp[w][i] = (value0, items0)
        else:
          dp[w][i] = (value1, items1)
      else:
        dp[w][i] = dp[w][i - 1]

  return dp[max_weight][num_items]

def knapsack_0_1_bottom_up_space_efficient(weights, values, max_weight, num_items):
  # Making the dp array
  dp = [(0, []) for i in range(max_weight + 1)]

  # Taking first i elements
  for i in range(1, num_items + 1):

    # Starting from back,
    # so that we also have data of
    # previous computation when taking i - 1 items
    for w in range(max_weight, 0, -1):
      if weights[i - 1] <= w:

        # Finding the maximum value
        value0, items0 = dp[w - weights[i - 1]]
        value0 += values[i - 1]
        items0 = items0.copy()
        items0.append(i - 1)

        value1, items1 = dp[w]

        if value0 >= value1:
          dp[w] = (value0, items0)
        else:
          dp[w] = (value1, items1)

  return dp[max_weight]

# Driver Code
if __name__ == '__main__':
    values = [60, 100, 120]
    weights = [10, 20, 30]
    max_weight = 50

    print(knapsack_0_1_bottom_up_space_efficient(max_weight = max_weight,
                                                 weights = weights,
                                                 values = values,
                                                 num_items = len(values)))
 
