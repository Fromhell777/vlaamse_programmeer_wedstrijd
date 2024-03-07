test_cases = int(input())

for t in range(test_cases):

  data = [int(x) for x in input().split()]
  size = data[0]

  nums = data[1:]

  reek_rij = True
  meet_rij = True

  diff = nums[1] - nums[0]
  for i in range(1, len(nums) - 1):
    if nums[i] + diff != nums[i + 1]:
      reek_rij = False

  div = nums[1] // nums[0]
  if div * nums[0] != nums[1]:
    meet_rij = False
  else:
    for i in range(1, len(nums) - 1):
      if div * nums[i] != nums[i + 1]:
        meet_rij = False

  if meet_rij:
    print(f"{t + 1} meetkundig met stap {div}: {nums[-1] * div}")
  elif reek_rij:
    print(f"{t + 1} rekenkundig met stap {diff}: {nums[-1] + diff}")
  else:
    print(f"{t + 1} geen van beide")
