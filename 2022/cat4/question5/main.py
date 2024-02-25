
test_cases = int(input())

for t in range(test_cases):

  win_numbers_size = int(input())
  win_numbers = [int(x) for x in input().split()]
  start, alice0, alice1, bob0, bob1 = [int(x) for x in input().split()]

  alice_values = (alice0, alice1)
  bob_values = (bob0, bob1)

  max_value = max(win_numbers)

  def solve(curr_value, alice_turn):
    if alice_turn:
      test_values = alice_values
    else:
      test_values = bob_values

    if curr_value in win_numbers:
      if alice_turn:
        return "bob", set([curr_value])
      else:
        return "alice", set([curr_value])

    win_data = {}

    for value in test_values:
      next_value = curr_value + value

      if next_value <= max_value:
        win_name, wins = solve(next_value, not alice_turn)
        win_data.setdefault(win_name, set())
        win_data[win_name].update(wins)

    if len(win_data) == 0:
      return "gelijk", set()

    if alice_turn and "alice" in win_data:
      return "alice", win_data["alice"]
    elif not alice_turn and "bob" in win_data:
      return "bob", win_data["bob"]
    elif "gelijk" in win_data:
      return "gelijk", set()
    elif alice_turn:
      return "bob", win_data["bob"]
    else:
      return "alice", win_data["alice"]

  win_name, wins = solve(start, True)

  if win_name == "gelijk":
    print(f"{t + 1} gelijk")
  elif win_name == "alice":
    print(f"{t + 1} win {' '.join([str(i) for i in sorted(wins)])}")
  else:
    print(f"{t + 1} verlies {' '.join([str(i) for i in sorted(wins)])}")
