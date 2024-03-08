
test_cases = int(input())

for t in range(test_cases):

  subcasses = int(input())

  data = [int(x) for x in input().split()]

  set_data = set(data)
  a = sorted(list(set_data))

  data_map = {}
  for i in range(1, len(a)):
    data_map[a[i]] = a[i - 1]

  min_value = min(set_data)

  result = f"{t+1}"
  for e in data:
    if e in data_map:
      result += f" {data_map[e]}"

  print(result)
