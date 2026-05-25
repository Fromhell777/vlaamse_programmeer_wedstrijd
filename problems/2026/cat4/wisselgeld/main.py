from copy import deepcopy

test_cases = int(input())

for t in range(test_cases):

  num_tables = int(input())

  table_values = list(map(int, input().split()))
  table_values = tuple(table_values)

  num_coins = int(input())

  coin_values = []
  coin_amounts = []
  for _ in range(num_coins):
    data = list(map(int, input().split()))
    coin_values.append(data[0])
    coin_amounts.append(data[1])

  coin_values = tuple(coin_values)

  mem = {}

  def find_subsets(amounts, index, desired_sum):
    if index >= len(coin_values):

      # If we reach the end and the desired_sum becomes 0, we found a valid
      # subset
      if desired_sum == 0:
        return [[]]

      # Otherwise, we return as no valid subset is found
      return -1

    if (tuple(amounts[index:]), desired_sum) in mem:
      return deepcopy(mem[(tuple(amounts[index:]), desired_sum)])

    total_result = -1

    i = 1
    while i * coin_values[index] <= desired_sum and i <= amounts[index]:
      # Include current element in subset
      result = find_subsets(amounts, index + 1, desired_sum - i * coin_values[index])

      if result != -1:
        for j in range(len(result)):
          result[j].append((index, i))

        if total_result == -1:
          total_result = result
        else:
          total_result.extend(result)

      i += 1

    result = find_subsets(amounts, index + 1, desired_sum)

    if result != -1:
      if total_result == -1:
        total_result = result
      else:
        total_result.extend(result)

    mem[(tuple(amounts[index:]), desired_sum)] = deepcopy(total_result)

    return total_result

  result = 0

  def satisfy_tables(coin_amounts, num_items, curr_result):
    global result

    # Base Case
    if num_items == len(table_values):
      result = max(curr_result, result)
      return

    if curr_result + len(table_values) - num_items < result:
      return

    if curr_result + sum(coin_amounts) < result:
      return

    subsets = find_subsets(coin_amounts, 0, table_values[num_items])
    if subsets != -1:
      for subset in subsets:
        for payed in subset:
          coin_amounts[payed[0]] -= payed[1]

        satisfy_tables(coin_amounts, num_items + 1, curr_result + 1)

        # Reinstate data
        for payed in subset:
          coin_amounts[payed[0]] += payed[1]

    satisfy_tables(coin_amounts, num_items + 1, curr_result)

  satisfy_tables(coin_amounts, 0, 0)

  print(f"{t+1} {result}")
