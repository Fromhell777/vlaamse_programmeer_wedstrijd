test_cases = int(input())

for t in range(test_cases):

  num_dishes, max_weight = list(map(int, input().split()))

  weights = []
  values = []
  reductions = []
  for _ in range(num_dishes):
    weight, value, reduction = list(map(int, input().split()))
    weights.append(weight)
    values.append(value)
    reductions.append(reduction)

  mem = [[[None for _ in range(max(values) // min(reductions) + 2)] for _ in range(len(values) + 1)] for _ in range(max_weight + 1)]
  def knapsack_unbound_recursive_memoization(weights, values, reductions, max_weight, num_items, used):

    # Base Case
    if num_items == 0 or max_weight == 0:
      return 0

    if mem[max_weight][num_items][used] != None:
      return mem[max_weight][num_items][used]

    # If weight of the nth item is more than knapsack of capacity max_weight, then
    # this item cannot be included in the optimal solution
    if (weights[num_items - 1] > max_weight) or \
       (values[num_items - 1] <= 0):
      mem[max_weight][num_items][used] = knapsack_unbound_recursive_memoization(weights = weights,
                                                                          values = values,
                                                                          reductions = reductions,
                                                                          max_weight = max_weight,
                                                                          num_items = num_items - 1,
                                                                          used = 0)
      return mem[max_weight][num_items][used]

    # return the maximum of two cases:
    # (1) the item at index num_items can be included
    # (2) not included
    else:

      new_values = values.copy()
      new_values[num_items - 1] -= reductions[num_items - 1]
      value0 = knapsack_unbound_recursive_memoization(weights = weights,
                                                      values = new_values,
                                                      reductions = reductions,
                                                      max_weight = max_weight - weights[num_items - 1],
                                                      num_items = num_items,
                                                      used = used + 1)
      value0 += values[num_items - 1]

      value1 = knapsack_unbound_recursive_memoization(weights = weights,
                                                      values = values,
                                                      reductions = reductions,
                                                      max_weight = max_weight,
                                                      num_items = num_items - 1,
                                                      used = 0)

      mem[max_weight][num_items][used] = max(value0, value1)

      return mem[max_weight][num_items][used]

  result = knapsack_unbound_recursive_memoization(weights,
                                                  values,
                                                  reductions,
                                                  max_weight,
                                                  num_dishes,
                                                  0)

  print(f"{t + 1} {result}")
