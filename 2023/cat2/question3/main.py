
test_cases = int(input())

for t in range(test_cases):

  y_size, x_size = [int(x) for x in input().split()]

  matrix = []

  for i in range(y_size):
    matrix.append([int(x, 16) for x in list(input())])

  moves = int(input())

  for i in range(moves):

    row, column, move = [x for x in input().split()]

    row = int(row) - 1
    column = int(column) - 1

    original_num = matrix[row][column]
    done = set()

    if move == "+":
      diff = 1
    else:
      diff = -1

    updates = [(row, column)]

    if (move == "+" and original_num != 15) or \
       (move == "-" and original_num != 0):
      while len(updates) > 0:
        curr_row = updates[-1][0]
        curr_column = updates[-1][1]

        if (curr_row, curr_column) in done:
          updates = updates[0:-1]
          continue

        matrix[curr_row][curr_column] += diff

        done.add(updates[-1])

        updates = updates[0:-1]

        if curr_row - 1 >= 0 and \
           (curr_row - 1, curr_column) not in done:
          if matrix[curr_row - 1][curr_column] == original_num:
            updates.append((curr_row - 1, curr_column))

        if curr_row + 1 < y_size and \
           (curr_row + 1, curr_column) not in done:
          if matrix[curr_row + 1][curr_column] == original_num:
            updates.append((curr_row + 1, curr_column))

        if curr_column - 1 >= 0 and \
           (curr_row, curr_column - 1) not in done:
          if matrix[curr_row][curr_column - 1] == original_num:
            updates.append((curr_row, curr_column - 1))

        if curr_column + 1 < x_size and \
           (curr_row, curr_column + 1) not in done:
          if matrix[curr_row][curr_column + 1] == original_num:
            updates.append((curr_row, curr_column + 1))

  for i in range(y_size):
    print(f"{t + 1} {''.join([hex(x)[2:].upper() for x in matrix[i]])}")
