import copy

test_cases = int(input())

for _ in range(test_cases):

  data = [int(x) for x in input().split()]
  total = data[0]
  coins = data[1:]

  hit_values = {0 : 1}

  for coin in coins:
    new_hit_values = copy.deepcopy(hit_values)

    intermediate_value = coin
    while intermediate_value <= total:

      for value, hits in hit_values.items():
        if value + intermediate_value <= total:
          new_hit_values.setdefault(value + intermediate_value, 0)
          new_hit_values[value + intermediate_value] += hits

      intermediate_value += coin

    hit_values = new_hit_values

  if total in hit_values:
    print(hit_values[total])
  else:
    print(0)
