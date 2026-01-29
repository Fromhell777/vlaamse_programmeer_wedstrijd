test_cases = int(input())

for _ in range(test_cases):

  data = [x for x in input().split()]
  num_decode = int(data[-1])

  morse = data[0]

  dots = morse.count('.')
  stripes = morse.count('-')

  for _ in range(num_decode):
    new_dots = dots + stripes * 3
    new_stripes = dots + stripes

    dots = new_dots
    stripes = new_stripes

  print(dots + stripes)
