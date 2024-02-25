import math

test_cases = int(input())

for t in range(test_cases):

  height0, height1, tube_height0, tube_height1  = [int(x) for x in input().split()]

  tube_height = max(tube_height0, tube_height1)

  result0 = 0
  result1 = 0

  left_over0 = 0
  left_over1 = 0

  extra0 = 0
  extra1 = 0

  if height0 < tube_height:
    result0 = height0
    left_over0 = tube_height - height0

  if height0 >= tube_height:
    result0 = tube_height
    extra0 = height0 - tube_height

  if height1 < tube_height:
    divide -= height1
    result1 = height1
    left_over1 = tube_height - height1

  if height1 >= tube_height:
    result1 = tube_height
    extra1 = height1 - tube_height

  result0 += min(left_over0, extra1)
  result1 += min(left_over1, extra0)

  divide = extra1 - min(left_over0, extra1) + extra0 - min(left_over1, extra0)

  result0 += divide // 2
  result1 += divide // 2

  if result0 == result1:
    print(f"{t + 1} gelijk")
  else:
    print(f"{t + 1} {result0} {result1}")
