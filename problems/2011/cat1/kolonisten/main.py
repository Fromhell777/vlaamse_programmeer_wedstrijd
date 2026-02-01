test_cases = int(input())

dice_props = {2  : 1/36,
              3  : 2/36,
              4  : 3/36,
              5  : 4/36,
              6  : 5/36,
              7  : 6/36,
              8  : 5/36,
              9  : 4/36,
              10 : 3/36,
              11 : 2/36,
              12 : 1/36}

for _ in range(test_cases):

  num_tiles = int(input())

  resources = [x for x in input().split()]
  numbers_to_roll = [int(x) for x in input().split()]

  num_tiles_resource = {}
  for resource in resources:
    num_tiles_resource.setdefault(resource, 0)
    num_tiles_resource[resource] += 1

  expected_resources = {}

  for resource, value in zip(resources, numbers_to_roll):
    expected_resources.setdefault(resource, 0)

    expected_resources[resource] += dice_props[value]

  sorted_result = [x for x in expected_resources.items()]
  sorted_result.sort(key = lambda x: x[1])

  least_resources = [sorted_result[0][0]]
  for resource, value in sorted_result[1:]:
    if abs(value - sorted_result[0][1]) < 1e-6:
      least_resources.append(resource)

  least_resources.sort(key = lambda x: num_tiles_resource[x])

  print(least_resources[0])
