test_cases = int(input())

for t in range(test_cases):

  data = list(map(int, input().split()))

  data.sort(reverse = True)

  result = 0
  for cites in data:
    if cites > result:
      result += 1

  print(f"{t + 1} {result}")
