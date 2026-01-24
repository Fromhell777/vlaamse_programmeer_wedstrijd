test_cases = int(input())

for _ in range(test_cases):

  data = [int(x) for x in input().split()]

  num_students = data[0]

  if num_students < 2:
    print("spieken kon niet")
    continue

  results = data[1:]

  diff = [abs(results[i] - results[i-1]) for i in range(1, len(results))]

  min_index = 0
  min_diff = diff[0]
  for i in range(len(diff)):
    if diff[i] < min_diff:
      min_index = i
      min_diff = diff[i]

  if min_diff == 0:
    print(f"{min_index + 1} en {min_index + 2} zijn zwaar verdacht")
  else:
    print(f"{min_index + 1} en {min_index + 2} zijn verdacht")
