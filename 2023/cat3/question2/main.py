import math

test_cases = int(input())

for t in range(test_cases):

  points = [int(x) for x in input().split()]

  xdata = [x for x in input().split()]
  ydata = [x for x in input().split()]

  name1 = xdata[0]
  name2 = ydata[0]

  places1 = [int(i) for i in xdata[1:]]
  places2 = [int(i) for i in ydata[1:]]

  scores1 = 0
  scores2 = 0

  diff1 = 0
  diff2 = 0

  for i in range(len(places1)):

    if places1[i] <= len(points):
      scores1 += points[places1[i] - 1]
      diff1 += 1

    if places2[i] <= len(points):
      scores2 += points[places2[i] - 1]
      diff2 += 1

  if scores1 == scores2:
    print(f"{t + 1} ex aequo")

    if diff1 != diff2:
      if diff1 > diff2:
        print(f"{t + 1} {name1} wint door verschuiving met {1}")
        print(f"{t + 1} {name2} wint door verschuiving met {-1}")
      else:
        print(f"{t + 1} {name2} wint door verschuiving met {1}")
        print(f"{t + 1} {name1} wint door verschuiving met {-1}")

  else:
    if scores1 < scores2:
      name1, name2 = name2, name1
      scores1, scores2 = scores2, scores1
      diff1, diff2 = diff2, diff1

    print(f"{t + 1} {name1} wint")

    if diff1 != diff2:
      if diff1 > diff2:
        shift = math.ceil((scores2 - scores1) / (diff1 - diff2))
        if (points[-1] + shift > 0):
          if (scores1 + shift * (diff1 - diff2) == scores2):
            print(f"{t + 1} ex aequo door verschuiving met {shift}")
            if (points[-1] + shift - 1 > 0):
              print(f"{t + 1} {name2} wint door verschuiving met {shift - 1}")
          else:
            print(f"{t + 1} {name2} wint door verschuiving met {shift}")
      elif diff2 > diff1:
        shift = math.ceil((scores1 - scores2) / (diff2 - diff1))
        if (points[-1] + shift + 1 > 0):
          if (scores1 == scores2 + shift * (diff2 - diff1)):
            print(f"{t + 1} {name2} wint door verschuiving met {shift + 1}")
            if (points[-1] + shift > 0):
              print(f"{t + 1} ex aequo door verschuiving met {shift}")
          else:
            if (points[-1] + shift > 0):
              print(f"{t + 1} {name2} wint door verschuiving met {shift}")
