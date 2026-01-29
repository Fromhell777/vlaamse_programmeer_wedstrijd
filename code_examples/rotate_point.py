def rotate_counterclockwise(center_point, point):
  translate_point = [point[0] - center_point[0], point[1] - center_point[1]]
  rotate_point = [-translate_point[1], translate_point[0]]
  return (rotate_point[0] + center_point[0], rotate_point[1] + center_point[1])

def rotate_clockwise(center_point, point):
  translate_point = [point[0] - center_point[0], point[1] - center_point[1]]
  rotate_point = [translate_point[1], -translate_point[0]]
  return (rotate_point[0] + center_point[0], rotate_point[1] + center_point[1])

# Driver Code
if __name__ == '__main__':

  center_point = (4,5)
  point = (3,7)

  print(rotate_clockwise(center_point, point))
  print(rotate_counterclockwise(center_point, point))
