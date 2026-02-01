test_cases = int(input())

for t in range(test_cases):

  num_cars = int(input())

  poleposition = []
  for _ in range(num_cars):
    poleposition.append(list(map(int, input().split())))

  result = [-1] * num_cars

  correct = True
  for index, (car_number, diff) in enumerate(poleposition):
    new_position = index + diff
    if 0 <= new_position < len(result):
      result[new_position] = car_number
    else:
      correct = False
      break

  if correct and not any(x == -1 for x in result):
    print('\n'.join([str(x) for x in result]))
  else:
    print(-1)
