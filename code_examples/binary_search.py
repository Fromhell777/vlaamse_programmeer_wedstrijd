
def binary_search(values, elem):

  low = 0
  high = len(values) - 1
  mid = 0

  while low <= high:

    mid = (high + low) // 2

    if values[mid] < elem:
      low = mid + 1

    elif values[mid] > elem:
      high = mid - 1

    else:
      return mid

  # If we reach here, then the element was not present
  return -1

def binary_search_insert_right():

  values = [2,5,6,8,9,14]

  low = 0
  high = len(values)
  mid = 0

  x = 6

  while low < high:

    mid = (low + high) // 2

    if x < values[mid]:
      high = mid
    else:
      low = mid + 1

  values.insert(low, x)

def binary_search_insert_left():

  values = [2,5,6,8,9,14]

  low = 0
  high = len(values)
  mid = 0

  x = 5

  while low < high:

    mid = (low + high) // 2

    if x > values[mid]:
      low = mid + 1
    else:
      high = mid

  values.insert(low, x)
