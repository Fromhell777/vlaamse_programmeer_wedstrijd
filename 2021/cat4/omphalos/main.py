import copy

test_cases = int(input())

for t in range(test_cases):

  num_trees = int(input())
  trees = []
  for i in range(num_trees):
    trees.append([int(x) for x in input().split()][1:])

  def find_merged_trees(lhs, rhs):
    merged_trees = []
    for i in range(1, len(lhs)):
      if lhs[-i:] == rhs[:i]:
        merged_trees.append(lhs + rhs[i:])
    return merged_trees

  def contains(tree, subtree):
    for i in range(len(tree) - len(subtree)):
      if tree[i:i + len(subtree)] == subtree:
        return True
    return False

  trees.sort(key = lambda x: len(x), reverse = True)

  result = []
  result_found = False

  def find_total_tree(trees):
    global result
    global result_found

    if result_found:
      return

    if len(trees) == 1:
      result = trees[0]
      result_found = True
      return

    changed = False
    for i in range(1, len(trees)):
      merged_trees = find_merged_trees(trees[0], trees[i])
      merged_trees.extend(find_merged_trees(trees[i], trees[0]))
      for merged_tree in merged_trees:
        changed = True
        new_trees = copy.deepcopy(trees)
        new_trees[0] = merged_tree
        new_trees.pop(i)
        find_total_tree(new_trees)
        if result_found:
          return

    if not changed:

      for tree in trees[1:]:
        if not contains(trees[0], tree):
          return

      result = trees[0]
      result_found = True

  find_total_tree(trees)

  print(f"{t + 1} {' '.join([str(i) for i in result])}")
