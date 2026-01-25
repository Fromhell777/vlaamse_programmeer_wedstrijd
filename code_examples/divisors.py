def get_divisors(number):
  divisors = []

  for i in range(1, int(number**0.5) + 1):
    if number % i == 0:
      divisors.append(i)

      converse_divisor = number // i
      if i != converse_divisor:
        divisors.append(converse_divisor)

  divisors.sort()

  return divisors

def get_prime_divisors(number):
  divisors = []

  while number % 2 == 0:
    divisors.append(2)
    number //= 2

  while number % 3 == 0:
    divisors.append(3)
    number //= 3

  i = 5
  while i * i <= number:
    for k in (i, i + 2):
      while number % k == 0:
        divisors.append(k)
        number //= k
    i += 6

  if number > 1:
    divisors.append(number)

  return divisors

def get_divisors2(number):
  divisors = []

  if number == 1:
    divisors.append(1)

  elif number > 1:
    prime_factors = get_prime_divisors(number)

    divisors = [1]
    last_prime = 0
    factor = 0
    slice_len = 0

    # Find all the products that are divisors of number
    for prime in prime_factors:
      if last_prime != prime:
        slice_len = len(divisors)
        factor = prime
      else:
        factor *= prime

      for i in range(slice_len):
        divisors.append(divisors[i] * factor)

      last_prime = prime

    divisors.sort()

  return divisors

# Driver Code
if __name__ == '__main__':
  print(get_divisors(40))
  print(get_divisors(24))
  print(get_divisors(5050))

  print(get_prime_divisors(40))
  print(get_prime_divisors(24))
  print(get_prime_divisors(5050))

  print(get_divisors2(40))
  print(get_divisors2(24))
  print(get_divisors2(5050))
