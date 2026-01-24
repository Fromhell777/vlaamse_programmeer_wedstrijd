test_cases = int(input())

for _ in range(test_cases):

  num_cols, num_rows = [int(x) for x in input().split()]

  foreground = []
  for i in range(num_rows):
    foreground.append(input())

  num_cols, num_rows = [int(x) for x in input().split()]

  mask = []
  for i in range(num_rows):
    mask.append(input())

  num_cols, num_rows = [int(x) for x in input().split()]

  background = []
  for i in range(num_rows):
    background.append(input())

  result = [[0 for _ in range(num_cols)] for _ in range(num_rows)]

  for i in range(num_rows):
    for j in range(num_cols):
      if mask[i][j] == 'F':
        result[i][j] = foreground[i][j]
      else:
        result[i][j] = background[i][j]

  print(f"{num_cols} {num_rows}")
  for i in range(num_rows):
    print(''.join(result[i]))
