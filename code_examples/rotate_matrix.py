def rotate_clockwise(matrix):
  new_matrix = []
  for i in range(len(matrix[0])):
    new_matrix.append([])
    for j in range(len(matrix) - 1, -1, -1):
      new_matrix[-1].append(matrix[j][i])

  return new_matrix

def rotate_counterclockwise(matrix):
  new_matrix = []
  for i in range(len(matrix[0]) - 1, -1, -1):
    new_matrix.append([])
    for j in range(len(matrix)):
      new_matrix[-1].append(matrix[j][i])

  return new_matrix

# Driver Code
if __name__ == '__main__':

  matrix = [[0,1,2],
            [3,4,5],
            [6,7,8],
            [9,0,1]]

  print(rotate_clockwise(matrix))
  print(rotate_counterclockwise(matrix))
