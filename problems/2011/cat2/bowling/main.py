test_cases = int(input())

def check_bowl(throws):
  current_frame = 0
  current_throw = 0
  while current_frame < 9:
    if current_throw >= len(throws):
      return False

    throw1 = throws[current_throw]
    current_throw += 1

    if throw1 > 10:
      return False

    if throw1 == 10:
      current_frame += 1
      continue

    if current_throw >= len(throws):
      return False

    throw2 = throws[current_throw]
    current_throw += 1

    if throw1 + throw2 > 10:
      return False

    current_frame += 1

  if current_throw >= len(throws):
    return False

  throw1 = throws[current_throw]
  current_throw += 1

  if throw1 > 10:
    return False

  if current_throw >= len(throws):
    return False

  throw2 = throws[current_throw]
  current_throw += 1

  if throw2 > 10:
    return False

  if throw1 == 10:
    if current_throw >= len(throws):
      return False

    throw3 = throws[current_throw]
    current_throw += 1

    if throw3 > 10:
      return False

    if throw2 != 10:
      if throw2 + throw3 > 10:
        return False

  else:
    if throw1 + throw2 > 10:
      return False

    if throw1 + throw2 == 10:
      if current_throw >= len(throws):
        return False

      throw3 = throws[current_throw]
      current_throw += 1

      if throw3 > 10:
        return False

  if current_throw != len(throws):
    return False

  return True

for _ in range(test_cases):

  throws = [int(x) for x in input().split()]

  valid_game = check_bowl(throws)

  if not valid_game:
    print("ONGELDIG")
    continue

  score = []
  current_frame = 0
  current_throw = 0
  while current_frame < 9:

    if len(score) == 0:
      score.append(0)
    else:
      score.append(score[-1])

    throw1 = throws[current_throw]
    current_throw += 1

    score[-1] += throw1

    if throw1 == 10:
      current_frame += 1
      score[-1] += throws[current_throw] + throws[current_throw + 1]
      continue

    throw2 = throws[current_throw]
    current_throw += 1

    score[-1] += throw2

    if throw1 + throw2 == 10:
      score[-1] += throws[current_throw]

    current_frame += 1

  throw1 = throws[current_throw]
  current_throw += 1

  score.append(score[-1])
  score[-1] += throw1

  throw2 = throws[current_throw]
  current_throw += 1

  score[-1] += throw2

  if throw1 == 10:
    throw3 = throws[current_throw]
    score[-1] += throw3
  else:
    if throw1 + throw2 == 10:
      throw3 = throws[current_throw]
      score[-1] += throw3

  print(' '.join([str(x) for x in score]))
