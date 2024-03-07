
test_cases = int(input())

for t in range(test_cases):

  costs = [int(x) for x in input().split()]

  prefix_costs = [0]
  for cost in costs:
    prefix_costs.append(cost + prefix_costs[-1])

  num_tasks = int(input())

  total_cost = 0

  for i in range(num_tasks):
    task_cost, task_time = [int(x) for x in input().split()]

    task_hours = task_time // 60
    task_min_left = task_time % 60

    current_min = prefix_costs[-1] * task_time * task_cost

    for j in range(len(costs) - task_hours + 1):
      if j != 0:
        current_min = min(current_min,
                          task_cost * ((prefix_costs[task_hours + j] -
                                        prefix_costs[j]) * 60 +
                                       costs[j - 1] * task_min_left))

      if j != len(costs) - task_hours:
        current_min = min(current_min,
                          task_cost * ((prefix_costs[task_hours + j] -
                                        prefix_costs[j]) * 60 +
                                       costs[j + task_hours] * task_min_left))

    total_cost += current_min

  print(f"{t + 1} {total_cost}")
