test_cases = int(input())

for t in range(test_cases):

  size = int(input())
  data = [int(x) for x in input().split()]

  result = []

  sorted_list = []

  for value in reversed(data):

    # Binary search insert
    low = 0
    high = len(sorted_list)
    mid = 0

    while low < high:

      mid = (low + high) // 2

      if value > sorted_list[mid]:
        low = mid + 1
      else:
        high = mid

    sorted_list.insert(low, value)
    result.append(low)

  if len(result) == 0:
    print(f"{t + 1}")
  else:
    print(f"{t + 1} {' '.join([str(i) for i in reversed(result)])}")
