import math

test_cases = int(input())

for t in range(test_cases):

  num_box = int(input())

  heights = list(map(int, input().split()))

  diffs = []
  for _ in range(num_box):
    diffs.append(list(map(int, input().split())))

  cache = {}
  def min_height_base(base, boxes_left):
    if (base, boxes_left) in cache:
      return cache[(base, boxes_left)]

    if len(boxes_left) == 0:
      return 0

    result = math.inf
    for i in range(len(boxes_left)):
      other_boxes = boxes_left[:i] + boxes_left[i + 1:]
      diff = diffs[base][boxes_left[i]]
      result = min(result, diff + min_height_base(boxes_left[i], other_boxes))

    cache[(base, boxes_left)] = result

    return result

  results = {}
  def min_height(boxes):
    global results

    result = math.inf
    for i in range(len(boxes)):
      base = heights[boxes[i]]
      other_boxes = boxes[:i] + boxes[i + 1:]
      result = min(result, base + min_height_base(boxes[i], other_boxes))

    results[boxes] = result

  for i in range(2**num_box):
    boxes = []
    index = 0
    while i > 0:
      if i % 2 == 1:
        boxes.append(index)

      index += 1
      i >>= 1

    min_height(tuple(boxes))

  total_min_height = math.inf
  for boxes, height in results.items():
    other_boxes = [i for i in range(num_box)]
    for box in boxes:
      other_boxes.remove(box)

    other_boxes = tuple(other_boxes)
    if len(other_boxes) == 0:
      total_min_height = min(total_min_height, height)
    elif other_boxes in results.keys():
      total_min_height = min(total_min_height, max(height, results[other_boxes]))

  print(f"{t+1} {total_min_height}")
