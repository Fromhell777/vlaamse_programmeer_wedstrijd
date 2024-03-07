test_cases = int(input())

for t in range(test_cases):

  max_waffles, max_irons, num_clients = [int(x) for x in input().split()]

  data = []

  for i in range(num_clients):
    data.append([int(x) for x in input().split()])

  def knapsack_0_1(weights, values, max_waffles, max_irons, num_items):

    # Base Case
    if num_items == 0 or (max_waffles == 0 and max_irons == 0):
      return 0

    if (max_waffles, max_irons, num_items) in mem:
      return mem[(max_waffles, max_irons, num_items)]

    # If weight of the nth item is more than knapsack of capacity max_weight, then
    # this item cannot be included in the optimal solution
    if (weights[num_items - 1][0] > max_waffles) or \
       (weights[num_items - 1][1] > max_irons):
      return knapsack_0_1(weights     = weights,
                          values      = values,
                          max_waffles = max_waffles,
                          max_irons   = max_irons,
                          num_items   = num_items - 1)

    # return the maximum of two cases:
    # (1) the item at index num_items can be included
    # (2) not included
    else:
      value0 = knapsack_0_1(weights     = weights,
                            values      = values,
                            max_waffles = max_waffles - weights[num_items - 1][0],
                            max_irons   = max_irons - weights[num_items - 1][1],
                            num_items   = num_items - 1) + values[num_items - 1]
      value1 = knapsack_0_1(weights     = weights,
                            values      = values,
                            max_waffles = max_waffles,
                            max_irons   = max_irons,
                            num_items   = num_items - 1)

      if value0 >= value1:
        mem[(max_waffles, max_irons, num_items)] = value0
      else:
        mem[(max_waffles, max_irons, num_items)] = value1

      return mem[(max_waffles, max_irons, num_items)]

  mem = {}

  result = knapsack_0_1(weights     = data,
                        values      = [1 for _ in range(num_clients)],
                        max_waffles = max_waffles,
                        max_irons   = max_irons,
                        num_items   = num_clients)

  print(f"{t+1} {result}")
