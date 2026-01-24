test_cases = int(input())

for _ in range(test_cases):

  index = int(input()) - 1

  order_of_magnitude = 0
  new_index = index
  while 10**order_of_magnitude * 9 * (order_of_magnitude + 1) < new_index:
    new_index -= 10**order_of_magnitude * 9 * (order_of_magnitude + 1)
    order_of_magnitude += 1

  number_length = order_of_magnitude + 1
  final_number = (new_index // number_length) + 10**order_of_magnitude
  result = str(final_number)[new_index % number_length]

  print(result)
