import copy

test_cases = int(input())

for _ in range(test_cases):

  num_words = int(input())

  words = []
  for _ in range(num_words):
    words.append(input())

  num_pieces = int(input())

  pieces = []
  for _ in range(num_pieces):
    pieces.append(input().lower())

  for word in words:

    solutions = {word : []}
    new_solutions = {}

    while len(solutions) > 0 and "" not in solutions:
      for piece in pieces:
        for word, parts in solutions.items():
          if word.startswith(piece):
            new_parts = copy.deepcopy(parts)
            new_parts.append(piece)
            new_solutions[word[len(piece):]] = new_parts

      solutions = copy.deepcopy(new_solutions)
      new_solutions = {}

    if len(solutions) == 0:
      print("nee")
    else:
      print('-'.join([x.capitalize() for x in solutions[""]]))
