
def list_cycle_detection_floyd():
  """Floyd's cycle detection algorithm."""

  connections = [2,3,1,0]

  x0 = 0

  # Main phase of algorithm: finding a repetition x_i = x_2i.
  # The hare moves twice as quickly as the tortoise and
  # the distance between them increases by 1 at each step.
  # Eventually they will both be inside the cycle and then,
  # at some point, the distance between them will be
  # divisible by the period λ.
  tortoise = connections[x0] # connections(x0) is the element/node next to x0.
  hare = connections[connections[x0]]
  while tortoise != hare:
    tortoise = connections[tortoise]
    hare = connections[connections[hare]]

  # At this point the tortoise position, ν, which is also equal
  # to the distance between hare and tortoise, is divisible by
  # the period λ. So hare moving in cycle one step at a time,
  # and tortoise (reset to x0) moving towards the cycle, will
  # intersect at the beginning of the cycle. Because the
  # distance between them is constant at 2ν, a multiple of λ,
  # they will agree as soon as the tortoise reaches index μ.

  # Find the position μ of first repetition.
  mu = 0
  tortoise = x0
  while tortoise != hare:
    tortoise = connections[tortoise]
    hare = connections[hare]   # Hare and tortoise move at same speed
    mu += 1

  # Find the length of the shortest cycle starting from x_μ
  # The hare moves one step at a time while tortoise is still.
  # lam is incremented until λ is found.
  lam = 1
  hare = connections[tortoise]
  while tortoise != hare:
    hare = connections[hare]
    lam += 1

  # mu is the position of the first repetition
  # lam is the length of the cycle
  return lam, mu

def list_cycle_detection_brent():
  """Brent's cycle detection algorithm."""

  connections = [2,3,1,0]

  x0 = 0

  # main phase: search successive powers of two
  power = 1
  lam = 1
  tortoise = x0
  hare = connections[x0]  # connections[x0) is the element/node next to x0.
  while tortoise != hare:
    if power == lam:  # time to start a new power of two?
      tortoise = hare
      power *= 2
      lam = 0
    hare = connections[hare]
    lam += 1

  # Find the position of the first repetition of length λ
  tortoise = x0
  hare = x0
  # range(lam) produces a list with the values 0, 1, ... , lam-1
  # The distance between the hare and tortoise is then λ.
  for i in range(lam):
    hare = connections[hare]

  # Next, the hare and tortoise move at same speed until they agree
  mu = 0
  while tortoise != hare:
    tortoise = connections[tortoise]
    hare = connections[hare]
    mu += 1
 
  return lam, mu
