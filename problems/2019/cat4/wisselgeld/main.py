import math

test_cases = int(input())

for t in range(test_cases):

  pay = int(input())
  data = [int(x) for x in input().split()]
  my_coins = data[1:]
  my_coins.sort(reverse = True)

  data = [int(x) for x in input().split()]
  machine_coins = data[1:]
  machine_coins.sort()

  data = [int(x) for x in input().split()]
  return_coins = data[1:]
  return_coins.sort()

  overpay = sum(return_coins)

  test_return = []
  current_overpay = overpay
  current_coin = len(machine_coins) - 1
  while current_overpay > 0:
    if current_coin < 0:
      break

    coin = machine_coins[current_coin]
    if coin <= current_overpay:
      coins = current_overpay // coin
      test_return.extend([coin] * coins)
      current_overpay -= coins * coin

    current_coin -= 1

  if current_overpay != 0:
    print(f"{t + 1} ONMOGELIJK")
    continue

  test_return.sort()
  if test_return != return_coins:
    print(f"{t + 1} ONMOGELIJK")
    continue

  result = math.inf

  def is_subset_sum_recursive(num_items, desired_sum, used_items):
    global result

    # Base Cases
    if desired_sum == 0:
      result = min(result, used_items)
      return
    if num_items == 0:
      return

    # If the last element is greater than the desired_sum, ignore it
    if my_coins[num_items - 1] > desired_sum:
      return is_subset_sum_recursive(num_items - 1, desired_sum, used_items)

    # Check if desired_sum can be obtained by including or excluding the last
    # element
    is_subset_sum_recursive(num_items - 1, desired_sum, used_items)
    if desired_sum > overpay:
      is_subset_sum_recursive(num_items - 1,
                              desired_sum - my_coins[num_items - 1],
                              used_items + 1)

  is_subset_sum_recursive(len(my_coins), pay + overpay, 0)

  if result != math.inf:
    print(f"{t + 1} {result}")
  else:
    print(f"{t + 1} ONMOGELIJK")
