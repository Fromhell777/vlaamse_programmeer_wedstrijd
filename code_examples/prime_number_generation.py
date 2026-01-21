import math

def generate_primes(maximum):

  primes = [2]

  for num in range(3, maximum, 2):
    is_prime = True
    square_root = math.sqrt(num)
    for prime in primes:
      if num % prime == 0:
        is_prime = False
        break
      if prime > square_root:
        break

    if is_prime:
      primes.append(num)

  return primes
