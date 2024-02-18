import math

test_cases = int(input())

for t in range(test_cases):

  num_persons = int(input())

  data = [int(x) - 1 for x in input().split()]

  inside = [False for i in range(num_persons)]
  sales = [[0,1] for i in range(num_persons)]
  num_inside = 0

  for person in data:
    if not inside[person]:
      entering = True
    else:
      entering = False

    if entering:
      for i in range(len(inside)):
        if inside[i]:
            sales[i][0] = sales[i][0] * 2**num_inside + sales[i][1]
            sales[i][1] *= 2**num_inside

    if not inside[person]:
      inside[person] = True
      num_inside += 1
    else:
      inside[person] = False
      num_inside -= 1

  new_sales = sales.copy()

  for i, sale in enumerate(sales):
    gcd = math.gcd(sale[0], sale[1])
    new_sales[i] = [sale[0] // gcd, sale[1] // gcd]

  for i, sale in enumerate(new_sales):
    if sale[0] == 0:
      result = "0"
    else:
      if sale[0] * 100 > sale[1] * 73:
        result = f"73/100"
      else:
        result = f"{sale[0]}/{sale[1]}"

    print(f"{t + 1} {i + 1} {result}")
