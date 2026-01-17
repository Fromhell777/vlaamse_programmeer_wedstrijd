import copy

test_cases = int(input())

for _ in range(test_cases):

  num_rows, num_cols = [int(x) for x in input().split()]

  art = []
  for i in range(num_rows):
    art.append(input())

  num_querry = int(input())

  for _ in range(num_querry):

    num_sub_rows, num_sub_cols = [int(x) for x in input().split()]

    def test_match(art, sub_art):
      for i in range(num_cols - num_sub_cols + 1):
        for j in range(num_rows - num_sub_rows + 1):
          matched = True
          for k in range(num_sub_rows):
            if art[j + k][i:i + num_sub_cols] != sub_art[k]:
              matched = False
              break

          if matched:
            return j, i

      return -1, -1

    def rotate(art):
      new_art = []
      for i in range(num_sub_cols):
        row = ""
        for j in range(1, num_sub_rows + 1):
          row += art[-j][i]
        new_art.append(row)
      return new_art


    sub_art = []
    for i in range(num_sub_rows):
      sub_art.append(input())

    rotation = 0
    for i in range(4):
      result_row, result_col = test_match(art, sub_art)

      if result_row != -1:
        print(f"{result_row + 1} {result_col + 1} {rotation}")
        break

      rotation += 90
      sub_art = rotate(sub_art)
      num_sub_rows, num_sub_cols = num_sub_cols, num_sub_rows




