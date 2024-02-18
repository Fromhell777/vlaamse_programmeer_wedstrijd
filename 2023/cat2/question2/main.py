
test_cases = int(input())

for t in range(test_cases):

  size, test_size = [int(x) for x in input().split()]

  max_score = 0
  found = False

  data = [int(x) for x in input().split()]

  prog_num = size
  prog_score = data[-1]

  for i in range(size):
    score = data[i]

    if i < test_size:
      max_score = max(max_score, score)
    else:
      if score >= max_score and not found:
        prog_num = i + 1
        prog_score = score
        found = True

  print(f"{t + 1} {prog_num} {prog_score}")
