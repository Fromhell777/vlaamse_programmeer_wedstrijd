test_cases = int(input())

for _ in range(test_cases):

  num_sentences = int(input())

  sentence = []
  for i in range(num_sentences):
    sentence.append(input())
  sentence = '\n'.join(sentence)

  num_commands = int(input())

  for _ in range(num_commands):

    repetition, word = [x for x in input().split()]
    repetition = int(repetition)

    word_repeated = ' '.join([word] * repetition)

    current_start = 0
    new_sentence = ""

    while True:
      index = sentence.find(word_repeated, current_start)

      if index != -1:
        if index == 0 or index + len(word_repeated) >= len(sentence) or \
           (sentence[index - 1] in (' ', '\n') and
            sentence[index + len(word_repeated)] in (' ', '\n')):
          new_sentence += sentence[current_start:index] + word
        else:
          new_sentence += sentence[current_start:index] + word_repeated
        current_start = index + len(word_repeated)
      else:
        new_sentence += sentence[current_start:]
        break

    sentence = new_sentence

  print(sentence)
