
test_cases = int(input())

for t in range(test_cases):

  left_weights = [int(x) for x in input().split()]
  right_weights = [int(x) for x in input().split()]

  left_total_weigth = sum(left_weights)
  right_total_weigth = sum(right_weights)

  total_weight = left_total_weigth + right_total_weigth

  if total_weight % 2 != 0:
    print(f"{t + 1} onmogelijk")
    continue

  if left_total_weigth < right_total_weigth:
    diff = right_total_weigth - left_total_weigth
    left_weights = [2 * i for i in left_weights]
    right_weights = [2 * -i for i in right_weights]
  else:
    diff = left_total_weigth - right_total_weigth
    left_weights = [2 * -i for i in left_weights]
    right_weights = [2 * i for i in right_weights]

  if diff % 2 != 0:
    print(f"{t + 1} onmogelijk")
    continue

  reachable_numbers = {diff : 0}

  all_weights = left_weights + right_weights

  for weight in all_weights:

    new_reachable_numbers = {}

    new_number = diff + weight
    if new_number in reachable_numbers:
      if 1 < reachable_numbers[new_number]:
        new_reachable_numbers[new_number] = 1
    else:
      new_reachable_numbers[new_number] = 1

    for reachable_number, moves in reachable_numbers.items():
      new_number = reachable_number + weight
      if new_number in reachable_numbers:
        if moves + 1 < reachable_numbers[new_number]:
          new_reachable_numbers[new_number] = moves + 1
      else:
        new_reachable_numbers[new_number] = moves + 1

    reachable_numbers.update(new_reachable_numbers)

  if 0 in reachable_numbers:
    print(f"{t + 1} {reachable_numbers[0]}")
  else:
    print(f"{t + 1} onmogelijk")
