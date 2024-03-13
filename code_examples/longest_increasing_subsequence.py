
def longest_strictly_increasing_subsequence(values):

  # Points to the previous element in the subsequence
  prev = [None] * len(values)

  # min_length_indices[l] stores the index k of the smallest value values[k]
  # such that there is an increasing subsequence of length l ending at values[k]
  min_length_indices = [None] * (len(values) + 1)

  longest_length = 0
  for i in range(len(values)):
    # Binary search for the smallest positive l <= longest_length such that
    # values[min_length_indices[l]] > values[i]
    low = 1
    high = longest_length + 1
    while low < high:
      mid = low + (high - low) // 2 # low <= mid < high
      if values[min_length_indices[mid]] >= values[i]:
        high = mid
      else: # if values[min_length_indices[mid]] < values[i]
        low = mid + 1

    # After searching, low == high is 1 greater than the length of the longest
    # prefix of values[i]
    new_longest_length = low

    # The predecessor of values[i] is the last index of the subsequence of
    # length new_longest_length - 1
    prev[i] = min_length_indices[new_longest_length - 1]
    min_length_indices[new_longest_length] = i

    # If we found a subsequence longer than any we've found yet, update
    # longest_length
    longest_length = max(new_longest_length, longest_length)

  # Reconstruct the longest increasing subsequence.
  # It consists of the data located at the longest_length indices:
  #   [...,  prev[prev[min_length_indices[longest_length]]],
  #    prev[min_length_indices[longest_length]],
  #    min_length_indices[longest_length]]
  sequence = [None] * longest_length
  k = min_length_indices[longest_length]
  for i in range(longest_length - 1, -1, -1):
    sequence[i] = values[k]
    k = prev[k]

  return longest_length, sequence

def longest_increasing_subsequence(values):

  # Points to the previous element in the subsequence
  prev = [None] * len(values)

  # min_length_indices[l] stores the index k of the smallest value values[k]
  # such that there is an increasing subsequence of length l ending at values[k]
  min_length_indices = [None] * (len(values) + 1)

  longest_length = 0
  for i in range(len(values)):
    # Binary search for the smallest positive l <= longest_length such that
    # values[min_length_indices[l]] >= values[i]
    low = 1
    high = longest_length + 1
    while low < high:
      mid = low + (high - low) // 2 # low <= mid < high
      if values[min_length_indices[mid]] > values[i]:
        high = mid
      else: # if values[min_length_indices[mid]] <= values[i]
        low = mid + 1

    # After searching, low == high is 1 greater than the length of the longest
    # prefix of values[i]
    new_longest_length = low

    # The predecessor of values[i] is the last index of the subsequence of
    # length new_longest_length - 1
    prev[i] = min_length_indices[new_longest_length - 1]
    min_length_indices[new_longest_length] = i

    # If we found a subsequence longer than any we've found yet, update
    # longest_length
    longest_length = max(new_longest_length, longest_length)

  # Reconstruct the longest increasing subsequence.
  # It consists of the data located at the longest_length indices:
  #   [...,  prev[prev[min_length_indices[longest_length]]],
  #    prev[min_length_indices[longest_length]],
  #    min_length_indices[longest_length]]
  sequence = [None] * longest_length
  k = min_length_indices[longest_length]
  for i in range(longest_length - 1, -1, -1):
    sequence[i] = values[k]
    k = prev[k]

  return longest_length, sequence

# Driver Code
if __name__ == '__main__':
  values = [0, 8, 4, 12, 2, 10, 6, 14, 1, 9, 5, 13, 3, 11, 7, 15]

  result_length, result = longest_strictly_increasing_subsequence(values)

  print(f"Input sequence: {values}")
  print(f"The length of the longest increasing subsequence is: {result_length}")
  print(f"The longest increasing subsequence is: {result}")

  values = [0, 8, 4, 12, 2, 10, 6, 14, 1, 9, 5, 13, 3, 11, 6, 11, 7, 15]

  result_length, result = longest_increasing_subsequence(values)

  print(f"\nInput sequence: {values}")
  print(f"The length of the longest increasing subsequence is: {result_length}")
  print(f"The longest increasing subsequence is: {result}")
