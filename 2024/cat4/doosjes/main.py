import itertools

# From more_itertools
def set_partitions(iterable, k=None):
    """
    Yield the set partitions of *iterable* into *k* parts. Set partitions are
    not order-preserving.

    >>> iterable = 'abc'
    >>> for part in set_partitions(iterable, 2):
    ...     print([''.join(p) for p in part])
    ['a', 'bc']
    ['ab', 'c']
    ['b', 'ac']


    If *k* is not given, every set partition is generated.

    >>> iterable = 'abc'
    >>> for part in set_partitions(iterable):
    ...     print([''.join(p) for p in part])
    ['abc']
    ['a', 'bc']
    ['ab', 'c']
    ['b', 'ac']
    ['a', 'b', 'c']

    """
    L = list(iterable)
    n = len(L)
    if k is not None:
        if k < 1:
            raise ValueError(
                "Can't partition in a negative or zero number of groups"
            )
        elif k > n:
            return

    def set_partitions_helper(L, k):
        n = len(L)
        if k == 1:
            yield [L]
        elif n == k:
            yield [[s] for s in L]
        else:
            e, *M = L
            for p in set_partitions_helper(M, k - 1):
                yield [[e], *p]
            for p in set_partitions_helper(M, k):
                for i in range(len(p)):
                    yield p[:i] + [[e] + p[i]] + p[i + 1 :]

    if k is None:
        for k in range(1, n + 1):
            yield from set_partitions_helper(L, k)
    else:
        yield from set_partitions_helper(L, k)

def calc_min_height(start_order, curr_min_height):

  result = curr_min_height

  for order in itertools.permutations(start_order):

    height = 0

    breaked = False
    for index, j in enumerate(order):
      if index == 0:
        height = box_heights[j]
      else:
        height += matrix[order[index - 1]][j]

      if height >= result:
        breaked = True
        break

    if breaked:
      continue

    result = min(result, height)

  return result

test_cases = int(input())

for t in range(test_cases):

  num_box = int(input())

  box_heights = [int(x) for x in input().split()]

  matrix = []

  for _ in range(num_box):
    matrix.append([int(x) for x in input().split()])

  total_min_height = 10e10

  for sorted_order_left, sorted_order_right in set_partitions([i for i in range(num_box)], 2):

    min_left = calc_min_height(sorted_order_left, total_min_height)

    if min_left >= total_min_height:
      continue

    min_right = calc_min_height(sorted_order_right, total_min_height)

    total_min_height = min(total_min_height, max(min_left, min_right))

  # All in one stack
  min_left = calc_min_height([i for i in range(num_box)], total_min_height)

  total_min_height = min(total_min_height, min_left)

  print(f"{t+1} {total_min_height}")
