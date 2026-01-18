char_to_int = {' ' : 0,
               'A' : 1,
               'B' : 2,
               'C' : 3,
               'D' : 4,
               'E' : 5,
               'F' : 6,
               'G' : 7,
               'H' : 8,
               'I' : 9,
               'J' : 10,
               'K' : 11,
               'L' : 12,
               'M' : 13,
               'N' : 14,
               'O' : 15,
               'P' : 16,
               'Q' : 17,
               'R' : 18,
               'S' : 19,
               'T' : 20,
               'U' : 21,
               'V' : 22,
               'W' : 23,
               'X' : 24,
               'Y' : 25,
               'Z' : 26}

int_to_char = {0  : ' ',
               1  : 'A',
               2  : 'B',
               3  : 'C',
               4  : 'D',
               5  : 'E',
               6  : 'F',
               7  : 'G',
               8  : 'H',
               9  : 'I',
               10 : 'J',
               11 : 'K',
               12 : 'L',
               13 : 'M',
               14 : 'N',
               15 : 'O',
               16 : 'P',
               17 : 'Q',
               18 : 'R',
               19 : 'S',
               20 : 'T',
               21 : 'U',
               22 : 'V',
               23 : 'W',
               24 : 'X',
               25 : 'Y',
               26 : 'Z'}

num_encode = int(input())

def decode_input():
  text = input().split()
  codeword = text[0]
  sentence = ' '.join(text[1:])

  codeword = codeword * (len(sentence) // len(codeword) + 1)
  codeword = codeword[:len(sentence)]
  return codeword, sentence

def transform(sentence, codeword, encode):
  new_sentence = ""
  for i in range(len(sentence)):
    if encode:
      new_char = char_to_int[sentence[i]] + char_to_int[codeword[i]]
    else:
      new_char = char_to_int[sentence[i]] - char_to_int[codeword[i]]

    new_char %= 27
    new_sentence += int_to_char[new_char]

  return new_sentence

for _ in range(num_encode):

  codeword, sentence = decode_input()

  encoded_sentence = transform(sentence, codeword, True)

  print(encoded_sentence)

num_decode = int(input())

for _ in range(num_decode):

  codeword, sentence = decode_input()

  decoded_sentence = transform(sentence, codeword, False)

  print(decoded_sentence)
