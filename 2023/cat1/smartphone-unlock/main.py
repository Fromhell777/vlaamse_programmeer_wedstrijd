import math

test_cases = int(input())

for t in range(test_cases):

  y_size, x_size = [int(x) for x in input().split()]
  size = int(input())

  data = [int(x) - 1 for x in input().split()]

  if len(data) != len(set(data)):
    if not (len(data) == len(set(data)) + 1 and data[0] == data[-1]):
      print(f"{t + 1} ongeldig patroon")
      continue

  dirs = set()
  num_hit = set([data[0]])

  bad_pattern = False

  for i in range(1, len(data)):
    x_step = (data[i] % x_size) - (data[i - 1] % x_size)
    y_step = (data[i] // x_size) - (data[i - 1] // x_size)

    gcd = math.gcd(x_step, y_step)

    small_x_step = x_step // gcd
    small_y_step = y_step // gcd

    sign_x = small_x_step > 0
    sign_y = small_y_step > 0

    if sign_x == sign_y or small_x_step == 0 or small_y_step == 0:
      dirs.add((abs(small_x_step), abs(small_y_step)))
    elif sign_x == True:
      dirs.add((small_x_step, small_y_step))
    else:
      dirs.add((-small_x_step, -small_y_step))

    curr_x = small_x_step
    curr_y = small_y_step

    for j in range(gcd - 1):
      new_x = data[i - 1] % x_size + curr_x
      new_y = data[i - 1] // x_size + curr_y
      if new_x + new_y * x_size not in num_hit:
        bad_pattern = True

      curr_x += small_x_step
      curr_y += small_y_step

    num_hit.add(data[i])

  if bad_pattern:
    print(f"{t + 1} ongeldig patroon")
    continue

  complexity = len(data) - 1 + len(dirs)

  print(f"{t + 1} {complexity}")
