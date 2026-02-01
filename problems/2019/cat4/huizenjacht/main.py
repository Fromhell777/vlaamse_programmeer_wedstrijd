import math

test_cases = int(input())

for t in range(test_cases):

  num_houses, num_select = [int(x) for x in input().split()]

  houses = []
  for _ in range(num_houses):
    data = [int(x) for x in input().split()]
    houses.append(tuple(data))

  houses.sort()

  distances = [[0] * num_houses for _ in range(num_houses)]
  for i in range(num_houses):
    for j in range(num_houses):
      house0 = houses[i]
      house1 = houses[j]
      dist = abs(house0[0] - house1[0]) + abs(house0[1] - house1[1])
      distances[i][j] = dist
      distances[j][i] = dist

  result = math.inf

  for house_index in range(num_houses):

    current_set = set()
    current_set.add(house_index)

    last_house_added = house_index
    houses_last_dist = [0] * num_houses

    set_worst_dist = 0

    test_houses = set([i for i in range(num_houses)])
    test_houses = test_houses - current_set

    while len(current_set) < num_select:
      min_dist = math.inf
      best_house = -1
      houses_to_remove = set()
      for new_house_index in test_houses:
        worst_dist = houses_last_dist[new_house_index]
        worst_dist = max(worst_dist, distances[new_house_index][last_house_added])
        houses_last_dist[new_house_index] = worst_dist

        if worst_dist >= result:
          houses_to_remove.add(new_house_index)

        if worst_dist < min_dist:
          best_house = new_house_index
          min_dist = worst_dist

      current_set.add(best_house)
      set_worst_dist = min_dist
      last_house_added = best_house

      if set_worst_dist >= result:
        break

      test_houses.remove(best_house)
      test_houses = test_houses - houses_to_remove


    result = min(result, set_worst_dist)

  print(f"{t + 1} {result}")
