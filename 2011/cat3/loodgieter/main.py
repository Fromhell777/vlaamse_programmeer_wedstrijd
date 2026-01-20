test_cases = int(input())

char_to_int = {'A' : 1,
               'B' : 2,
               'C' : 3,
               'D' : 4,
               'E' : 5,
               'F' : 6,
               'G' : 7,
               'H' : 8,
               'I' : 9,
               'J' : 10,
               'K' : 11,
               'L' : 12,
               'M' : 13,
               'N' : 14,
               'O' : 15,
               'P' : 16,
               'Q' : 17,
               'R' : 18,
               'S' : 19,
               'T' : 20,
               'U' : 21,
               'V' : 22,
               'W' : 23,
               'X' : 24,
               'Y' : 25,
               'Z' : 26}

int_to_char = {1  : 'A',
               2  : 'B',
               3  : 'C',
               4  : 'D',
               5  : 'E',
               6  : 'F',
               7  : 'G',
               8  : 'H',
               9  : 'I',
               10 : 'J',
               11 : 'K',
               12 : 'L',
               13 : 'M',
               14 : 'N',
               15 : 'O',
               16 : 'P',
               17 : 'Q',
               18 : 'R',
               19 : 'S',
               20 : 'T',
               21 : 'U',
               22 : 'V',
               23 : 'W',
               24 : 'X',
               25 : 'Y',
               26 : 'Z'}

def char_to_connections(char):
  number = char_to_int[char]
  up = (number % 2) == 1
  right = ((number >> 1) % 2) == 1
  down = ((number >> 2) % 2) == 1
  left = ((number >> 3) % 2) == 1

  return [up, right, down, left]

for _ in range(test_cases):

  grid_size = int(input())
  data = input()

  grid = []
  for _ in range(grid_size):
    grid.append(list(input()))

  tiles = {}
  for char in data:
    tiles.setdefault(char, 0)
    tiles[char] += 1

  def check_fit(char, i, j):
    up, right, down, left = char_to_connections(char)

    if i == 0:
      if up:
        return False
    else:
      other_char = grid[i - 1][j]
      if other_char != '?':
        other_up, other_right, other_down, other_left = char_to_connections(other_char)
        if not (up == other_down):
          return False

    if i == grid_size - 1:
      if down:
        return False
    else:
      other_char = grid[i + 1][j]
      if other_char != '?':
        other_up, other_right, other_down, other_left = char_to_connections(other_char)
        if not (down == other_up):
          return False

    if j == 0:
      if left:
        return False
    else:
      other_char = grid[i][j - 1]
      if other_char != '?':
        other_up, other_right, other_down, other_left = char_to_connections(other_char)
        if not (left == other_right):
          return False

    if j == grid_size - 1:
      if right:
        return False
    else:
      other_char = grid[i][j + 1]
      if other_char != '?':
        other_up, other_right, other_down, other_left = char_to_connections(other_char)
        if not (right == other_left):
          return False

    return True

  def get_solution():
    if len(tiles) == 0:
      return True

    grid_fit = [[[] for _ in range(grid_size)] for _ in range(grid_size)]

    for i in range(grid_size):
      for j in range(grid_size):
        if grid[i][j] == '?':
          for tile in tiles.keys():
            if check_fit(tile, i, j):
              grid_fit[i][j].append(tile)

    min_fit = len(data)
    min_location = [0,0]
    for i in range(grid_size):
      for j in range(grid_size):
        if len(grid_fit[i][j]) > 0 and len(grid_fit[i][j]) < min_fit:
          min_fit = len(grid_fit[i][j])
          min_location = [i,j]

    for tile in grid_fit[min_location[0]][min_location[1]]:
      grid[min_location[0]][min_location[1]] = tile
      tiles[tile] -= 1

      if tiles[tile] == 0:
        tiles.pop(tile)
        found = get_solution()
        if found:
          return True
        tiles[tile] = 1
      else:
        found = get_solution()
        if found:
          return True
        tiles[tile] += 1

      grid[min_location[0]][min_location[1]] = '?'

    return False

  get_solution()

  for i in range(grid_size):
    print(''.join(grid[i]))
