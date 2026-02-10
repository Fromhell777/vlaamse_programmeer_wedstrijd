
test_cases = int(input())

for t in range(test_cases):

  kapital = int(input())
  num_stocks = int(input())

  stocks = list(map(int, input().split()))

  if len(stocks) > 0:
    current_stocks = kapital // stocks[0]
    kapital -= current_stocks * stocks[0]
    for i in range(1, len(stocks)):
      if stocks[i] < stocks[i-1]:
        kapital += current_stocks * stocks[i-1]
        current_stocks = kapital // stocks[i]
        kapital -= current_stocks * stocks[i]

    result = kapital + current_stocks * stocks[-1]
  else:
    result = kapital

  print(f"{t + 1} {result}")
