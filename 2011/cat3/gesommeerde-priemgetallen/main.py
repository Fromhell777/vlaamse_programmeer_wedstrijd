import math

test_cases = int(input())

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

primes = generate_primes(32767)
primes_set = set(primes)

for _ in range(test_cases):

  left_bound, right_bound = [int(x) for x in input().split()]

  left_prime_index = 0
  for i in range(len(primes)):
    if primes[i] >= left_bound:
      left_prime_index = i
      break

  right_prime_index = 0
  for i in range(len(primes) - 1, -1, -1):
    if primes[i] <= right_bound:
      right_prime_index = i
      break

  best_solution = primes[left_prime_index]
  best_length = 1
  for i in range(1, right_prime_index - left_prime_index + 2):
    current_sum = sum(primes[left_prime_index:left_prime_index + i])
    if current_sum > primes[right_prime_index]:
      continue

    if current_sum < primes[right_prime_index] and \
       current_sum in primes_set:
      if i > best_length:
        best_length = i
        best_solution = current_sum

    for j in range(right_prime_index - left_prime_index + 2 - i):
      current_sum += primes[left_prime_index + i + j]
      current_sum -= primes[left_prime_index + j]

      if current_sum > primes[right_prime_index]:
        break

      if current_sum < primes[right_prime_index] and \
         current_sum in primes_set:
        if i > best_length:
          best_length = i
          best_solution = current_sum

  print(best_solution)
