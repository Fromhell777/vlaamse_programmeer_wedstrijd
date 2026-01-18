import functools

test_cases = int(input())

@functools.lru_cache(maxsize=10000)
def sum_squares(number):
  sum = 0
  for char in str(number):
    sum += int(char)**2
  return sum

for _ in range(test_cases):

  number = int(input())

  seen_numbers = set([number])

  while True:
    if number == 1:
      print("JA")
      break
    else:
      new_number = sum_squares(number)

      if new_number in seen_numbers:
        print("NEE")
        break

      seen_numbers.add(new_number)
      number = new_number
