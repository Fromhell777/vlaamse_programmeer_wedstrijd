
# Class to store information of a suffix
class suffix:

  def __init__(self):
    self.index = 0
    self.rank = [0, 0]

# This is the main function that takes a string 'txt' of size n as an argument,
# builds and returns the suffix array for the given string
def build_suffix_array(txt):

    txt_size = len(txt)

    # A structure to store suffixes and their indexes
    suffixes = [suffix() for _ in range(txt_size)]

    # Store suffixes and their indexes in an array of structures. The structure
    # is needed to sort the suffixes alphabetically and maintain their old
    # indexes while sorting
    for i in range(txt_size):
      suffixes[i].index = i
      suffixes[i].rank[0] = (ord(txt[i]) - ord('a'))

      if i + 1 < txt_size:
        suffixes[i].rank[1] = (ord(txt[i + 1]) - ord("a"))
      else:
        suffixes[i].rank[1] = -1

    # Sort the suffixes according to the rank and next rank
    suffixes = sorted(suffixes, key = lambda x : (x.rank[0], x.rank[1]))

    # At this point, all suffixes are sorted according to first 2 characters.
    # Let us sort suffixes according to first 4 characters, then first 8 and so
    # on

    # This array is needed to get the index in suffixes[] from the original
    # index. This mapping is needed to get next suffix.
    ind = [0] * txt_size

    k = 4
    while (k < 2 * txt_size):

      # Assigning rank and index values to first suffix
      rank = 0

      # Assigning rank to suffixes
      for i in range(0, txt_size):

        if i != 0:
          # If first rank and next ranks are same as that of previous suffix in
          # array, assign the same new rank to this suffix. Otherwise increment
          # rank and assign
          if not ((suffixes[i].rank[0] == prev_rank) and \
                  (suffixes[i].rank[1] == suffixes[i - 1].rank[1])):
            rank += 1

        prev_rank = suffixes[i].rank[0]
        suffixes[i].rank[0] = rank
        ind[suffixes[i].index] = i

      # Assign next rank to every suffix
      for i in range(txt_size):
        next_index = suffixes[i].index + k // 2

        if next_index < txt_size:
          suffixes[i].rank[1] = suffixes[ind[next_index]].rank[0]
        else:
          suffixes[i].rank[1] = -1

      # Sort the suffixes according to first k characters
      suffixes = sorted(suffixes, key = lambda x : (x.rank[0], x.rank[1]))

      k *= 2

    # Store indexes of all sorted suffixes in the suffix array
    suffix_array = [suffix.index for suffix in suffixes]

    # Return the suffix array
    return suffix_array

# Return indices from txt where the patter is located. Finding every occurrence
# of the pattern is equivalent to finding every suffix that begins with the
# substring
def find_substring(txt, pattern, suffix_array):
  # Find starting position of interval
  low = 0
  high = len(txt)
  while low < high:
    mid = (low + high) // 2

    # txt[suffix_array[i]:] is the ith smallest suffix
    if pattern > txt[suffix_array[mid]:]:
      low = mid + 1
    else:
      high = mid

  start = low

  # Find ending position of interval
  high = len(txt)
  while low < high:
    mid = (low + high) // 2

    if txt[suffix_array[mid]:].startswith(pattern):
      low = mid + 1
    else:
      high = mid

  stop = high

  return suffix_array[start:stop]

# Driver code
if __name__ == "__main__":

  txt = "banana"
  pattern = "ana"

  suffix_array = build_suffix_array(txt)
  pattern_indices = find_substring(txt          = txt,
                                   pattern      = pattern,
                                   suffix_array = suffix_array)

  print(f"The pattern \"{pattern}\" in \"{txt}\" is located at the " + \
        f"following indices: {pattern_indices}")
