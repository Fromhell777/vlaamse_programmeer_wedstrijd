test_cases = int(input())

for t in range(test_cases):

  data = list(map(int, input().split()))

  data.sort()

  result = 0
  cache = set()
  def find_different_rectangles(rectangles):
    global result

    sorted_rectangles = rectangles.copy()
    sorted_rectangles.sort()
    if tuple(sorted_rectangles) in cache:
      return

    cache.add(tuple(sorted_rectangles))

    result = max(len(set(sorted_rectangles)), result)

    new_rectangles = sorted_rectangles.copy()
    for i, rectangle in enumerate(sorted_rectangles):
      for new_width in range(1, rectangle[0]):
        new_rectangles[i] = (new_width, rectangle[1])
        new_rectangles.append((rectangle[0] - new_width, rectangle[1]))
        find_different_rectangles(new_rectangles)
        new_rectangles.pop()

      for new_height in range(1, rectangle[1]):
        new_rectangle = [rectangle[0], new_height]
        new_rectangle.sort()
        new_rectangles[i] = tuple(new_rectangle)

        new_rectangle = [rectangle[0], rectangle[1] - new_height]
        new_rectangle.sort()
        new_rectangles.append(tuple(new_rectangle))

        find_different_rectangles(new_rectangles)
        new_rectangles.pop()

      new_rectangles[i] = rectangle

  find_different_rectangles([tuple(data)])

  print(f"{t + 1} {result}")
