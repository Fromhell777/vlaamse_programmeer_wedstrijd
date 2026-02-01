import math

test_cases = int(input())

for t in range(test_cases):

  bal = input()
  target = int(input())
  num_tests = int(input())

  for _ in range(num_tests):
    volume = int(input())

    low_target = 10 * target - 5
    high_target = 10 * target + 5
    low_target = low_target**3
    high_target = high_target**3

    diameter = 20**3 * (3 / 4 * volume / math.pi)

    if low_target <= diameter < high_target:
      print(f"{volume} {bal}")
    else:
      print(f"{volume} geen {bal}")
