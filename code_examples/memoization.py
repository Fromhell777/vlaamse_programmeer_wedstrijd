import functools

@functools.cache
def factorial(n):
  if n < 2:
    return 1

  return n * factorial(n-1)

# Driver Code
if __name__ == '__main__':

  print(factorial(20))
  print(factorial(25))
