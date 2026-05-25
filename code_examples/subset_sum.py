def is_subset_sum_recursive(values, num_items, desired_sum):
  # Base Cases
  if desired_sum == 0:
    return True
  if num_items == 0:
    return False

  # If the last element is greater than the desired_sum, ignore it
  if values[num_items - 1] > desired_sum:
    return is_subset_sum_recursive(values, num_items - 1, desired_sum)

  # Check if desired_sum can be obtained by including or excluding the last
  # element
  return (is_subset_sum_recursive(values, num_items - 1, desired_sum) or
          is_subset_sum_recursive(values, num_items - 1, desired_sum - values[num_items - 1]))

def is_subset_sum_bottom_up0(values, desired_sum):
  num_items = len(values)

  # Create a 2D list for storing results of subproblems
  dp = [[False] * (desired_sum + 1) for _ in range(num_items + 1)]

  # If desired_sum is 0, then answer is true (empty subset)
  for i in range(num_items + 1):
    dp[i][0] = True

  # Fill the dp table in bottom-up manner
  for i in range(1, num_items + 1):
    for j in range(1, desired_sum + 1):
      if j < values[i - 1]:
        # Exclude the current element
        dp[i][j] = dp[i - 1][j]
      else:
        # Include or exclude
        dp[i][j] = dp[i - 1][j] or dp[i - 1][j - values[i - 1]]

  return dp[num_items][desired_sum]

def is_subset_sum_bottom_up_space_efficient(values, desired_sum):
  num_items = len(values)
  prev = [False] * (desired_sum + 1)
  curr = [False] * (desired_sum + 1)

  # Base case: desired_sum 0 can always be achieved
  prev[0] = True

  # Fill the dp table in a
  # bottom-up manner
  for i in range(1, num_items + 1):
    for j in range(desired_sum + 1):
      if j < values[i - 1]:
        curr[j] = prev[j]
      else:
        curr[j] = prev[j] or prev[j - values[i - 1]]
    prev = curr.copy()

  return prev[desired_sum]

def is_subset_sum_bottom_up_more_space_efficient(values, desired_sum):
  dp = [False] * (desired_sum + 1)

  # Initializing with 1 as sum 0 is always possible
  dp[0] = True

  # Loop to go through every element of the values array
  for value in values:

    # To change the value of all possible sum values to True
    for j in range(desired_sum, value - 1, -1):
      if dp[j - value]:
        dp[j] = True

  # If desired_sum is possible return True else False
  return dp[desired_sum]

def find_subsets(values, index, desired_sum, current_set, result):
  if index >= len(values):

    # If we reach the end and the desired_sum becomes 0, we found a valid
    # subset
    if desired_sum == 0:
      result.append(current_set[:])
      return

    # Otherwise, we return as no valid subset is found
    return

  if values[index] <= desired_sum:
    # Include current element in subset
    current_set.append(values[index])
    find_subsets(values, index + 1, desired_sum - values[index], current_set, result)

    # Backtrack and exclude the current element
    current_set.pop()

  find_subsets(values, index + 1, desired_sum, current_set, result)

# Function to find all subsets summing to desired_sum
def find_subsets_wrapper(values, desired_sum):
    result = []
    curr = []
    find_subsets(values, 0, desired_sum, curr, result)
    return result

def is_subset_sum_unbound_recursive(values, num_items, desired_sum):
  # Base Cases
  if desired_sum == 0:
    return True
  if num_items == 0:
    return False

  # If the last element is greater than the desired_sum, ignore it
  if values[num_items - 1] > desired_sum:
    return is_subset_sum_unbound_recursive(values, num_items - 1, desired_sum)

  # Check if desired_sum can be obtained by including or excluding the last
  # element
  return (is_subset_sum_unbound_recursive(values, num_items - 1, desired_sum) or
          is_subset_sum_unbound_recursive(values, num_items, desired_sum - values[num_items - 1]))

def is_subset_sum_unbound_bottom_up(values, desired_sum):
  num_items = len(values)

  # Create a 2D list for storing results of subproblems
  dp = [[False] * (desired_sum + 1) for _ in range(num_items + 1)]

  # If desired_sum is 0, then answer is true (empty subset)
  for i in range(num_items + 1):
    dp[i][0] = True

  # Fill the dp table in bottom-up manner
  for i in range(1, num_items + 1):
    for j in range(1, desired_sum + 1):
      if j < values[i - 1]:
        # Exclude the current element
        dp[i][j] = dp[i - 1][j]
      else:
        # Include or exclude
        dp[i][j] = dp[i - 1][j] or dp[i][j - values[i - 1]]

  return dp[num_items][desired_sum]

def is_subset_sum_unbound_bottom_up_space_efficient(values, desired_sum):
  dp = [False] * (desired_sum + 1)

  # Initializing with 1 as sum 0 is always possible
  dp[0] = True

  # Loop to go through every element of the values array
  for i in range(1, desired_sum + 1):

    # To change the value of all possible sum values to True
    for value in values:
      if i >= value and dp[i - value]:
        dp[i] = True

  # If desired_sum is possible return True else False
  return dp[desired_sum]

def find_subsets_unbound(values, index, desired_sum, current_set, result):
  if index >= len(values):

    # If we reach the end and the desired_sum becomes 0, we found a valid
    # subset
    if desired_sum == 0:
      result.append(current_set[:])
      return

    # Otherwise, we return as no valid subset is found
    return

  i = 1
  while i * values[index] <= desired_sum:
    # Include current element in subset
    current_set.extend([values[index]] * i)
    find_subsets(values, index + 1, desired_sum - i * values[index], current_set, result)

    # Backtrack and exclude the current element
    for _ in range(i):
      current_set.pop()

    i += 1

  find_subsets(values, index + 1, desired_sum, current_set, result)

# Function to find all subsets summing to desired_sum
def find_subsets_unbound_wrapper(values, desired_sum):
    result = []
    curr = []
    find_subsets_unbound(values, 0, desired_sum, curr, result)
    return result

# Driver Code
if __name__ == '__main__':
  values = [3, 34, 4, 12, 5, 2]
  desired_sum = 9

  print(is_subset_sum_recursive(values, len(values), desired_sum))
  print(is_subset_sum_bottom_up0(values, desired_sum))
  print(is_subset_sum_bottom_up_space_efficient(values, desired_sum))
  print(is_subset_sum_bottom_up_more_space_efficient(values, desired_sum))

  values = [5, 2, 3, 10, 6, 8]
  desired_sum = 10

  print(find_subsets_wrapper(values, desired_sum))

  values = [3, 10, 14, 5]
  desired_sum = 11

  print(is_subset_sum_unbound_recursive(values, len(values), desired_sum))
  print(is_subset_sum_unbound_bottom_up(values, desired_sum))
  print(is_subset_sum_unbound_bottom_up_space_efficient(values, desired_sum))

  values = [5, 2, 3, 10, 6, 8]
  desired_sum = 10

  print(find_subsets_unbound_wrapper(values, desired_sum))
