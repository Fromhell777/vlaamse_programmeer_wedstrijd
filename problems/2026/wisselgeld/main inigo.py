test_cases = int(input())

for t in range(test_cases):

  num_tables = int(input())

  table_values = list(map(int, input().split()))

  num_coins = int(input())

  coin_values = []
  for _ in range(num_coins):
    size, amount = map(int, input().split())
    coin_values.extend([size] * amount)

  def find_subsets(values, index, desired_sum, current_set, result):
    if index >= len(values):

      # If we reach the end and the desired_sum becomes 0, we found a valid
      # subset
      if desired_sum == 0:
        result.add(current_set[:])
        return

      # Otherwise, we return as no valid subset is found
      return

    if values[index] <= desired_sum:
      # Include current element in subset
      current_set = current_set + (values[index],)
      find_subsets(values, index + 1, desired_sum - values[index], current_set, result)

      # Backtrack and exclude the current element
      current_set = current_set[:-1]

    find_subsets(values, index + 1, desired_sum, current_set, result)

  # Function to find all subsets summing to desired_sum
  def find_subsets_wrapper(values, desired_sum):
      result = set()
      curr = tuple()
      find_subsets(values, 0, desired_sum, curr, result)
      return result

  partial_solutions = []
  for target in table_values:

    print(coin_values)
    partial_solution = find_subsets_wrapper(coin_values, target)
    print(partial_solution)



  #print(f"{t+1} {result}")
