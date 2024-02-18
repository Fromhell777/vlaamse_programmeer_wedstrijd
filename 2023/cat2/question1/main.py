
test_cases = int(input())

for t in range(test_cases):

  balance = int(input())
  size = int(input())

  data = [int(x) for x in input().split()]

  in_stocks = 0
  last_stock_value = 0

  for i in range(1, len(data)):
    if data[i] > data[i - 1]:
      extra_stocks = balance // data[i - 1]
      balance -= extra_stocks * data[i - 1]
      in_stocks += extra_stocks
      last_stock_value = data[i - 1]

    if data[i] < data[i - 1]:
      balance += in_stocks * data[i - 1]
      in_stocks = 0

  if in_stocks != 0:
    balance += in_stocks * max(data[-1], last_stock_value)

  print(f"{t + 1} {balance}")
