from suffix_tree import SuffixTree

def find_longest_repeated_substring_impl(tree, node, max_height, substring_index):
  if node.leaf:
    current_height = tree.size - node.suffix_index - tree.edge_length(node)

    if current_height > max_height:
      substring_index = node.suffix_index

    max_height = max(max_height, current_height)
    return max_height, substring_index

  for child_node in node.children.values():
    max_height, substring_index = \
      find_longest_repeated_substring_impl(tree            = tree,
                                           node            = child_node,
                                           max_height      = max_height,
                                           substring_index = substring_index)

  return max_height, substring_index

def find_longest_repeated_substring(tree):
  max_height, substring_index = \
    find_longest_repeated_substring_impl(tree            = tree,
                                         node            = tree.root,
                                         max_height      = 0,
                                         substring_index = -1)

  if max_height == 0:
    return ""
  else:
    return tree.txt[substring_index:substring_index + max_height]

# Driver code
if __name__ == "__main__":

  txt = "abcabxabcd$"

  tree = SuffixTree(txt)
  tree.build_suffix_tree()

  substring = find_longest_repeated_substring(tree)
  print(f"The pattern longest repeated substring in \"{txt}\" is: {substring}")
