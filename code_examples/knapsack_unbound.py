from fractions import Fraction

def knapsack_unbound_recursive(max_weight, weights, values, num_items):

  # Base Case
  if num_items == 0 or max_weight == 0:
    return 0, []

  # If weight of the nth item is more than knapsack of capacity max_weight, then
  # this item cannot be included in the optimal solution
  if (weights[num_items - 1] > max_weight):
    return knapsack_unbound_recursive(weights = weights,
                                      values = values,
                                      max_weight = max_weight,
                                      num_items = num_items - 1)

  # return the maximum of two cases:
  # (1) the item at index num_items can be included
  # (2) not included
  else:
    value0, items0 = knapsack_unbound_recursive(weights = weights,
                                                values = values,
                                                max_weight = max_weight - weights[num_items - 1],
                                                num_items = num_items)
    value0 += values[num_items - 1]
    items0.append(num_items - 1)

    value1, items1 = knapsack_unbound_recursive(weights = weights,
                                                values = values,
                                                max_weight = max_weight,
                                                num_items = num_items - 1)
    return (value0, items0) if value0 >= value1 else (value1, items1)

# Create a memoization matrix:
# mem = [[None for _ in range(len(values) + 1)] for _ in range(max_weight + 1)]
def knapsack_unbound_recursive_memoization(weights, values, max_weight, num_items):

  # Base Case
  if num_items == 0 or max_weight == 0:
    return (0, [])

  if mem[max_weight][num_items] != None:
    return mem[max_weight][num_items]

  # If weight of the nth item is more than knapsack of capacity max_weight, then
  # this item cannot be included in the optimal solution
  if (weights[num_items - 1] > max_weight):
    mem[max_weight][num_items] = knapsack_unbound_recursive_memoization(weights = weights,
                                                                        values = values,
                                                                        max_weight = max_weight,
                                                                        num_items = num_items - 1)
    return mem[max_weight][num_items]

  # return the maximum of two cases:
  # (1) the item at index num_items can be included
  # (2) not included
  else:
    value0, items0 = knapsack_unbound_recursive_memoization(weights = weights,
                                                            values = values,
                                                            max_weight = max_weight - weights[num_items - 1],
                                                            num_items = num_items)
    value0 += values[num_items - 1]
    items0 = items0.copy()
    items0.append(num_items - 1)

    value1, items1 = knapsack_unbound_recursive_memoization(weights = weights,
                                                            values = values,
                                                            max_weight = max_weight,
                                                            num_items = num_items - 1)
    if value0 >= value1:
      mem[max_weight][num_items] = (value0, items0)
    else:
      mem[max_weight][num_items] = (value1, items1)

    return mem[max_weight][num_items]

def knapsack_unbound_bottom_up(weights, values, max_weight, num_items):
  # Making the dp matrix
  dp = [[(0, []) for _ in range(num_items + 1)] for _ in range(max_weight + 1)]

  # Build table dp[][] in a bottom-up manner
  for i in range(num_items + 1):
    for w in range(max_weight + 1):
      if i == 0 or w == 0:
        dp[w][i] = (0, [])
      elif weights[i - 1] <= w:
        value0, items0 = dp[w - weights[i - 1]][i]
        value0 += values[i - 1]
        items0 = items0.copy()
        items0.append(i - 1)

        value1, items1 = dp[w][i - 1]

        if value0 >= value1:
          dp[w][i] = (value0, items0)
        else:
          dp[w][i] = (value1, items1)
      else:
        dp[w][i] = dp[w][i - 1]

  return dp[max_weight][num_items]

def knapsack_unbound_bottom_up_space_efficient(weights, values, max_weight, num_items):
  # Making the dp array
  dp = [(0, []) for _ in range(max_weight + 1)]

  # Build table dp[][] in a bottom-up manner
  for w in range(max_weight + 1):
    for i in range(num_items):
      if weights[i] <= w:

        # Finding the maximum value
        value0, items0 = dp[w - weights[i]]
        value0 += values[i]
        items0 = items0.copy()
        items0.append(i)

        value1, items1 = dp[w]

        if value0 >= value1:
          dp[w] = (value0, items0)
        else:
          dp[w] = (value1, items1)

  return dp[max_weight]

def knapsack_unbound_optimized(weights, values, max_weight, num_items):

  # Stores most dense item
  best_value_for_weight = 0

  # Find the item with highest value per unit weight
  # (if two items have same unit value then choose the lighter item)
  for i in range(1, num_items):
    curr_frac = Fraction(values[i], weights[i])
    best_frac = Fraction(values[best_value_for_weight],
                         weights[best_value_for_weight])
    if curr_frac > best_frac or \
       (curr_frac == best_frac and weights[i] < weights[best_value_for_weight]):
      best_value_for_weight = i

  dp = [(0, []) for _ in range(max_weight + 1)]

  counter = 0
  breaked_weight = None

  for w in range(max_weight + 1):
    for i in range(num_items):

      if (weights[i] <= w):
        value0, items0 = dp[w - weights[i]]
        value0 += values[i]
        items0 = items0.copy()
        items0.append(i)

        value1, items1 = dp[w]

        if value0 >= value1:
          dp[w] = (value0, items0)
        else:
          dp[w] = (value1, items1)

    if w - weights[best_value_for_weight] >= 0 and \
       dp[w][0] - dp[w - weights[best_value_for_weight]][0] == values[best_value_for_weight]:

      counter += 1

      if counter >= weights[best_value_for_weight]:

        breaked_weight = w
        break
    else:
      counter = 0

  if breaked_weight == None:
    return dp[max_weight]
  else:
    start = breaked_weight - weights[best_value_for_weight] + 1
    times = (max_weight - start) // weights[best_value_for_weight]
    index = (max_weight - start) % weights[best_value_for_weight] + start
    result_value = times * values[best_value_for_weight] + dp[index][0]
    result_items = dp[index][1]
    result_items.extend([best_value_for_weight] * times)
    return (result_value, result_items)

# Driver Code
if __name__ == '__main__':
  values = [10, 30, 20]
  weights = [5, 10, 15]
  max_weight = 100

  print(knapsack_unbound_optimized(max_weight = max_weight,
                                   weights = weights,
                                   values = values,
                                   num_items = len(values)))
