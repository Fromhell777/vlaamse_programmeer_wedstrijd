test_cases = int(input())

for t in range(test_cases):

  size = int(input())

  data = [int(input()) for i in range(size)]

  minimum = min(data)
  maximum = max(data)

  print(f"{t+1} {minimum} {maximum}")
