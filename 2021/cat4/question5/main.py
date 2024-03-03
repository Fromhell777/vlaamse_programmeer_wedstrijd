
test_cases = int(input())

for t in range(test_cases):

  size_ref_output = int(input())

  ref_output = {}
  max_test_case = 1

  for _ in range(size_ref_output):
    curr_ref_output = [x for x in input().split()]

    test_case = int(curr_ref_output[0])

    max_test_case = max(test_case, max_test_case)

    ref_output.setdefault(test_case, [])
    ref_output[test_case].append(' '.join(curr_ref_output))

  curr_test_case = 0

  user_output = {}

  size_user_output = int(input())

  for _ in range(size_user_output):
    curr_user_output = [x for x in input().strip().split()]

    if curr_user_output == []:
      continue

    if not curr_user_output[0].isdigit():
      continue

    new_test_case = int(curr_user_output[0])

    if new_test_case < 1 or new_test_case > max_test_case:
      continue

    if new_test_case < curr_test_case:
      continue

    curr_test_case = new_test_case

    user_output.setdefault(curr_test_case, [])
    user_output[curr_test_case].append(' '.join(curr_user_output))

  correct = 0

  for k, v in ref_output.items():
    v.sort()

  for k, v in user_output.items():
    v.sort()

  for k, v in user_output.items():
    if ref_output[k] == v:
      correct += 1

  print(f"{t + 1} {correct}/{len(ref_output)}")
