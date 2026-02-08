import math

test_cases = int(input())

for t in range(test_cases):

  num_houses, num_select = [int(x) for x in input().split()]

  houses = []
  for _ in range(num_houses):
    x, y = [int(x) for x in input().split()]
    # Transform the Manhattan distance into the Chebyshev distance. This
    # transforms the diamond shape area into a square shape area to check on the grid
    houses.append((x + y, x - y))

  houses.sort()

  min_x = math.inf
  max_x = 0
  min_y = math.inf
  max_y = 0
  for house in houses:
    min_x = min(min_x, house[0])
    max_x = max(max_x, house[0])
    min_y = min(min_y, house[1])
    max_y = max(max_y, house[1])

  max_square = max(max_x - min_x, max_y - min_y)

  def is_square_large_enough(size):

    x_right_index = 0
    for x_left_index in range(0, num_houses):
      while x_right_index < num_houses and \
            houses[x_right_index][0] - houses[x_left_index][0] <= size:
        x_right_index += 1

      x_right_index -= 1

      slice_houses = houses[x_left_index:x_right_index + 1].copy()
      slice_houses.sort(key = lambda x: x[1])

      y_right_index = 0
      for y_left_index in range(0, len(slice_houses)):

        while y_right_index < len(slice_houses) and \
              slice_houses[y_right_index][1] - slice_houses[y_left_index][1] <= size:
          y_right_index += 1

        y_right_index -= 1

        if y_right_index - y_left_index + 1 >= num_select:
          return True

        if y_right_index + 1 == len(slice_houses):
          break

      if x_right_index + 1 == num_houses:
        return False


  # Binary search the square size that still contains the desired number of houses
  low = 0
  high = max_square
  mid = 0

  while low < high:

    mid = (high + low) // 2

    if is_square_large_enough(mid):
      high = mid
    else:
      low = mid + 1

  print(f"{t + 1} {low}")
