# from functools import cache
import time

test_cases = int(input())

for t in range(test_cases):
  start = time.perf_counter()
  num_tables = int(input())

  table_values = list(map(int, input().split()))

  num_coins = int(input())

  # TODO sort
  coin_values = []
  for _ in range(num_coins):
    size, amount = map(int, input().split())
    coin_values.append((size, amount))
  coin_values.sort(reverse=False)

  # print(table_values)
  # print(coin_values)

  cache2 = set()
  def find_subsets(index, desired_sum, current_set, result):
    if time.perf_counter() - start > 0.1:
      return
    # print(index, desired_sum, current_set)

    if index >= len(coin_values):
      # If we reach the end and the desired_sum becomes 0, we found a valid
      # subset
      if desired_sum == 0:
        result.add(current_set)
        return

      # Otherwise, we return as no valid subset is found
      return

    key = (index, desired_sum, current_set)
    if key in cache2:
      return

    size, amount = coin_values[index]
    for picked in range(desired_sum // size + 1):
      if picked > amount:
        break
      next_set = current_set + ((size, picked),)
      find_subsets(index + 1, desired_sum - picked * size, next_set, result)


  # Function to find all subsets summing to desired_sum
  def find_subsets_wrapper(values, desired_sum):
      result = set()
      find_subsets(0, desired_sum, (), result)
      return result

  all_partials = []
  for target in table_values:
    partial_solution = find_subsets_wrapper(coin_values, target)
    all_partials.append(partial_solution)

  table_order = list(range(len(table_values)))
  table_order.sort(key=lambda i: len(all_partials[i]))

  # print()
  # for p in all_partials:
  #   for x in p:
  #     print(x)
  #   print()

  cache = {}
  all_best = 0

  def f(table_index, coins_left) -> int:
    if time.perf_counter() - start > 0.1:
      return 0
    # print(table_index, coins_left)

    global all_best
    # if len(table_values) - table_index <= all_best:
    #   return 0
    if table_index >= len(table_values):
      return 0

    k = (table_index, tuple(coins_left.items()))
    if k in cache:
      return cache[k]

    # ignore
    best = f(table_index + 1, coins_left)

    # satisfy
    for partial in all_partials[table_order[table_index]]:
      coins_left_edit = dict(coins_left)
      fail = False
      # print("derp", partial)
      for cval, ccount in partial:
        for _ in range(ccount):
          curr = coins_left_edit[cval]
          if curr <= 0:
            fail = True
            continue
          coins_left_edit[cval] = curr - 1
      if fail:
        continue

      res = f(table_index+1, coins_left_edit) + 1
      # if res > best:
        # print(partial)
      best = max(best, res)

      # for c in partial:
      #   coins_left[c] += 1

    cache[k] = best
    all_best = max(all_best, best - table_index)
    return best

  # print()
  print(f"{t+1} {f(0, coins_left={a: b for a, b in coin_values})}")

  # break
