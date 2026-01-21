import sys

patterns = []
section1 = True
words = []
for line in sys.stdin:
  if section1:
    if line[0] == '-':
      section1 = False
      continue

    patterns.append(line[:-1])
  else:
    words.append(line[:-1])

patterns_text = []
for pattern in patterns:
  pattern_text = [char for char in list(pattern) if char not in "012345"]
  patterns_text.append(''.join(pattern_text))

for word in words:
  word = '.' + word + '.'

  new_word = list('0'.join(list(word)))

  for i, pattern in enumerate(patterns_text):
    start_index = 0
    while True:
      found_index = word.find(pattern, start_index)
      if found_index == -1:
        break

      number_index = found_index * 2 - 1

      for char in patterns[i]:
        if char in "012345":
          old_value = int(new_word[number_index])
          new_value = int(char)
          new_word[number_index] = str(max(old_value, new_value))
        else:
          number_index += 2

      start_index = found_index + len(pattern)

  result = ""
  for char in new_word[2:-2]:
    if char in "012345":
      if (int(char) % 2) == 1:
        result += '-'
    else:
        result += char

  print(result)
