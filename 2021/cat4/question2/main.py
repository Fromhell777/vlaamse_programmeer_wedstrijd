
test_cases = int(input())

def is_int(x):
  try:
    int(x)
    return True
  except:
    return False

for t in range(test_cases):

  size = int(input())
  trans = {}
  for i in range(size):
    parts = [e.strip() for e in input().split()]
    res = []
    for p in parts:
      if p in trans:
        p = trans[p]
      else:
        if p in ['=', '-', '+', '*', '/']:
          p = p
        elif is_int(p):
          p = p
        else:
          new_name = 'a' * (len(trans) + 1)
          trans[p] = new_name
          p = trans[p]
      res.append(p)
    s = f'{t+1} '
    for e in res:
      s += e
    print(s)

