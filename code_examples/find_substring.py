from suffix_array import build_suffix_array
from suffix_tree import SuffixTree

# Using the Suffix Array:
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

# Using the Suffix Tree:
def check_substring_impl(tree, node, string, index):
  # Returns whether it contains the substring and at which node

  if node.start != -1:
    # Traverse edge character by character
    edge_len = min(tree.edge_length(node), len(string) - index)
    if tree.txt[node.start:node.start + edge_len] != string[index:index + edge_len]:
      return False, None
    index += edge_len

  if index == len(string):
    return True, node

  next_char = string[index]
  if node.children.get(next_char) is not None:
    return check_substring_impl(tree   = tree,
                                node   = node.children[next_char],
                                string = string,
                                index  = index)

  return False, None

def check_substring(tree, string):
  # Function to check if the string is a substring
  return check_substring_impl(tree   = tree,
                              node   = tree.root,
                              string = string,
                              index  = 0)

def get_substring_locations(node):
  if node.leaf:
    return [node.suffix_index]

  start_positions = []

  for child_node in node.children.values():
    start_positions.extend(get_substring_locations(child_node))

  return start_positions

def find_all_substrings(tree, string):
  # Function to find all the locations of a substring in the string. It
  # returns all the indices of where the substring is located
  contains, node = check_substring_impl(tree   = tree,
                                        node   = tree.root,
                                        string = string,
                                        index  = 0)

  if contains:
    return get_substring_locations(node)

  return []

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

  # The Suffix Tree needs a sentinel character at the end to avoid implicit
  # substrings in the tree
  tree = SuffixTree(txt + '$')
  tree.build_suffix_tree()

  match, _ = find_all_substrings(tree, pattern)
  print(f"The pattern \"{pattern}\" in \"{txt}\" is located at the " + \
        f"following indices: {pattern_indices}")
