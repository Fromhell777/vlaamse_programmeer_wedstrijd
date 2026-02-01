import copy

test_cases = int(input())

for _ in range(test_cases):

  num_patterns = int(input())

  patterns = []
  for _ in range(num_patterns):
    pattern = []
    for _ in range(2):
      pattern.append(list(input()))

    patterns.append(pattern)

  def rotate_clockwise(matrix):
    new_matrix = []
    for i in range(len(matrix[0])):
      new_matrix.append([])
      for j in range(len(matrix) - 1, -1, -1):
        value = matrix[j][i]
        if value == '-':
          value = '|'
        elif value == '|':
          value = '-'
        elif value == '\\':
          value = '/'
        elif value == '/':
          value = '\\'

        new_matrix[-1].append(value)

    return new_matrix

  num_actions = int(input())

  pattern_stack = []
  for _ in range(num_actions):
    action = input()

    if action == "draai":

      pattern_stack[-1] = rotate_clockwise(pattern_stack[-1])

    elif action == "teken":

      top = pattern_stack[-1]
      for line in top:
        print(''.join(line))
      print()

    elif action == "naai":

      top_left = pattern_stack.pop()
      top_right = pattern_stack.pop()

      new_matrix = copy.deepcopy(top_left)
      for i in range(len(top_right)):
        new_matrix[i].extend(top_right[i])

      pattern_stack.append(new_matrix)

    elif action == "stop":
      break
    else:
      action = int(action)

      top = copy.deepcopy(patterns[action - 1])
      pattern_stack.append(top)
