test_cases = int(input())

for _ in range(test_cases):

  data = [int(x) for x in input().split()]
  num_cards = data[0]
  cards = data[1:]

  prev_value = set()
  current_index = 0
  current_value = 0
  while len(cards) > 0:
    if cards[current_index] == current_value + 1:
      cards.pop(current_index)
      print(f"{current_value + 1} gevangen")

      current_value = 0
      prev_value = set()
    else:
      current_index += 1
      current_value = (current_value + 1) % num_cards

    if len(cards) > 0:
      current_index %= len(cards)

    if current_index == 0:
      if current_value in prev_value:
        break
      else:
        prev_value.add(current_value)

  if len(cards) == 0:
    print("alles gevangen")
  else:
    print("er kunnen geen kaarten meer gevangen worden")
