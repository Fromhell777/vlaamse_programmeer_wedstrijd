def convolve(values0, values1):
  result = [0] * (len(values0) + len(values1) - 1)

  for i in range(len(result)):
    start_index = max(0, i - len(values1) + 1)
    stop_index = min(i + 1, len(values0))
    for j in range(start_index, stop_index):
      result[i] += values0[j] * values1[i - j]

  return result

# Driver Code
if __name__ == '__main__':
  values0 = [1, 1, 1, 1, 1, 1]
  values1 = [1, 1, 1, 1, 1, 1]

  print(convolve(values0, values1))

  values0 = [1, 1, 1, 1, 1, 1]
  values1 = [1, 1]

  print(convolve(values0, values1))

  values0 = [1, 1]
  values1 = [1, 1, 1, 1, 1, 1]

  print(convolve(values0, values1))

  values1 = [1, 2]
  values0 = [1, 2, 3, 4, 5, 6]

  print(convolve(values0, values1))
