
test_cases = int(input())

for t in range(test_cases):

  cap, size = [int(x) for x in input().split()]

  lim = cap * 8 // 10

  data = [int(x) for x in input().split()]

  codes = []
  total_pop = 0

  for pop in data:
    total_pop = total_pop + pop

    if (total_pop <= lim):
      codes.append('g')
    elif (total_pop > cap):
      codes.append('r')
    else:
      codes.append('o')

  print(f"{t + 1} {' '.join(codes)}")
