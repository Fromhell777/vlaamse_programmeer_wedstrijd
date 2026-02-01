import itertools

def longest_strictly_increasing_subsequence(values):

  # Points to the previous element in the subsequence
  prev = [None] * len(values)

  # min_length_indices[l] stores the index k of the smallest value values[k]
  # such that there is an increasing subsequence of length l ending at values[k]
  min_length_indices = [None] * (len(values) + 1)

  longest_length = 0
  for i in range(len(values)):
    # Binary search for the smallest positive l <= longest_length such that
    # values[min_length_indices[l]] > values[i]
    low = 1
    high = longest_length + 1
    while low < high:
      mid = low + (high - low) // 2 # low <= mid < high
      if values[min_length_indices[mid]] >= values[i]:
        high = mid
      else: # if values[min_length_indices[mid]] < values[i]
        low = mid + 1

    # After searching, low == high is 1 greater than the length of the longest
    # prefix of values[i]
    new_longest_length = low

    # The predecessor of values[i] is the last index of the subsequence of
    # length new_longest_length - 1
    prev[i] = min_length_indices[new_longest_length - 1]
    min_length_indices[new_longest_length] = i

    # If we found a subsequence longer than any we've found yet, update
    # longest_length
    longest_length = max(new_longest_length, longest_length)

  # Reconstruct the longest increasing subsequence.
  # It consists of the data located at the longest_length indices:
  #   [...,  prev[prev[min_length_indices[longest_length]]],
  #    prev[min_length_indices[longest_length]],
  #    min_length_indices[longest_length]]
  sequence = [None] * longest_length
  k = min_length_indices[longest_length]
  for i in range(longest_length - 1, -1, -1):
    sequence[i] = values[k]
    k = prev[k]

  return longest_length, sequence

test_cases = int(input())

for t in range(test_cases):

  data = [x for x in input().split()]

  num_cards = int(data[0])
  cards = data[1:]

  suits = set()
  for card in cards:
    suits.add(card[0])

  contains_black = False
  contains_red = False

  for card in cards:
    if card[0] == 'H' or card[0] == 'R':
      contains_red = True
    if card[0] == 'S' or card[0] == 'K':
      contains_black = True

  if contains_black and contains_red:
    same_colors_neighbours = False
  else:
    same_colors_neighbours = True

  number_map = {'2'  : 0,
                '3'  : 1,
                '4'  : 2,
                '5'  : 3,
                '6'  : 4,
                '7'  : 5,
                '8'  : 6,
                '9'  : 7,
                "10" : 8,
                'B'  : 9,
                'V'  : 10,
                'H'  : 11,
                'A'  : 12}

  min_moves = len(cards)

  for suit_order in itertools.permutations(suits):

    valid_sequence = True
    for i in range(1, len(suit_order)):
      if suit_order[i - 1] == 'S' or \
         suit_order[i - 1] == 'K':
        color0 = "black"
      else:
        color0 = "red"

      if suit_order[i] == 'S' or \
         suit_order[i] == 'K':
        color1 = "black"
      else:
        color1 = "red"

      if not same_colors_neighbours and color0 == color1:
        valid_sequence = False

    if not valid_sequence:
      continue

    card_values = []

    for card in cards:
      card_values.append(number_map[card[1:]] + 13 * suit_order.index(card[0]))

    lis_length, lis_sequence = longest_strictly_increasing_subsequence(card_values)

    min_moves = min(min_moves, len(card_values) - lis_length)

  print(f"{t+1} {min_moves}")
