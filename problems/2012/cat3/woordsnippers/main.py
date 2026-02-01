import copy

test_cases = int(input())

for _ in range(test_cases):

  words = [x for x in input().split()]

  def find_merged_words_rigth(main, rhs):
    merged_words = []
    if main[len(main) - len(rhs) + 1:] == rhs[:-1]:
      merged_words.append(main + rhs[-1])
    return merged_words

  def find_merged_words_left(main, lhs):
    merged_words = []
    if main[:len(lhs) - 1] == lhs[1:]:
      merged_words.append(lhs[0] + main)
    return merged_words

  result = []
  result_found = False

  def find_total_word(words):
    global result
    global result_found

    if result_found:
      return

    if len(words) == 1:
      result = words[0]
      result_found = True
      return

    for i in range(1, len(words)):
      merged_words = find_merged_words_rigth(words[0], words[i])
      merged_words.extend(find_merged_words_left(words[0], words[i]))
      for merged_word in merged_words:
        new_words = copy.deepcopy(words)
        new_words[0] = merged_word
        new_words.pop(i)
        find_total_word(new_words)
        if result_found:
          return

  find_total_word(words)

  print(''.join([str(i) for i in result]))
