
test_cases = int(input())

def parse(p):
  try:
    return int(p) - 1, None
  except:
    return int(p[0]) - 1, int(p[-1]) - 1

def coord2index(coord):
  return 3*coord[0] + coord[1]

def index2coord(index):
  return index // 3, index % 3


for t in range(test_cases):
  board = [0 for _ in range(9)]
  pointers = {}

  for row in [input() for _ in range(3)]:
    for pointer in row.split(','):
      f, to = parse(pointer)
      if to is None:
        board[f] = 1
      pointers[f] = to

  for i in range(9):
    found = False
    for j in range(9):
      evil_index0 = index2coord(i)
      evil_index1 = index2coord(j)

      if evil_index0 != evil_index1 and not found:
        valid = True
        for k in range(9):
          curr_coord = index2coord(k)
          if curr_coord == evil_index0 or curr_coord == evil_index1:
            continue

          for dy, dx in [(0,1), (1,0), (-1,0), (0,-1), (1,1), (-1,-1), (-1,1), (1,-1)]:
            new_y = curr_coord[0] + dy
            new_x = curr_coord[1] + dx
            if new_y >= 0 and new_x >= 0 and new_y < 3 and new_x < 3:
              if board[k] == 1:
                if (new_y, new_x) == evil_index0 or (new_y, new_x) == evil_index1:
                  valid = False
                  break
              else:
                if not (index2coord(pointers[k]) == evil_index0 or \
                        index2coord(pointers[k]) == evil_index1):
                  valid = False
                  break

        if valid:
          found = True
          result = [i,j]
          break

    if found:
      break

  result.sort()

  print(f'{t+1} {",".join([str(i + 1) for i in result])}')
