import copy

test_cases = int(input())

for _ in range(test_cases):

  seats = int(input())
  parties = int(input())
  votes = [int(x) for x in input().split()]

  result = [0] * parties

  total_votes = sum(votes)

  div = 2
  while seats > 0:
    new_result = copy.deepcopy(result)

    for i, vote in enumerate(votes):
      if vote * div >= total_votes:
        new_result[i] += 1
        seats -= 1

    if seats >= 0:
      result = new_result
    div += 1

  print(' '.join([str(x) for x in result]))
