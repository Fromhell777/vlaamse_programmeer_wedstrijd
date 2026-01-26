test_cases = int(input())

for _ in range(test_cases):

  num_rules = int(input())

  branches = {}
  for _ in range(num_rules):
    data = [x for x in input().split()]
    branches[data[0]] = data[2:]

  def count_branches(branch_name):
    result = 1
    for child in branches[branch_name]:
      if child == '*':
        result += 1
      else:
        result += count_branches(child)

    return result

  result = 0
  for child in branches["stam"]:
    if child == '*':
      result += 1
    else:
      result += 2**count_branches(child) - 1

  print(result)
