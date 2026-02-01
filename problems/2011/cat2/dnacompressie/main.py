test_cases = int(input())

char_to_int = {'D' : 4,
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

int_to_char = {4  : 'D',
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

def compress(dna):

  result = ""

  i = 0
  while i < len(dna):
    char = dna[i]

    if dna[i:i + 4] == char * 4:

      repetitions = 0
      while repetitions < 26 and \
            i + repetitions < len(dna) and \
            dna[i + repetitions] == char:
        repetitions += 1

      result += f"-{int_to_char[repetitions]}{char}"
      i += repetitions

    else:
      result += dna[i]
      i += 1

  return result

def decompress(compressed):
  result = ""

  i = 0
  while i < len(compressed):
    if compressed[i] == '-':
      repetitions = char_to_int[compressed[i + 1]]
      result += compressed[i + 2] * repetitions
      i += 3
    else:
      result += compressed[i]
      i += 1

  return result

for _ in range(test_cases):

  dna, compressed = [x for x in input().split()]

  if dna == "???":
    dna = decompress(compressed)
  else:
    compressed = compress(dna)

  print(dna + ' ' + compressed)
