from queue import Queue

def breadth_first_search(rhs_to_lhs, matches_lhs,
                         matches_rhs, distance_lhs):

  rhs_index_Queue = Queue()

  for i in range(len(matches_lhs)):

    if matches_lhs[i] == -1:
      distance_lhs[i] = 0
      rhs_index_Queue.put(i)
    else:
      distance_lhs[i] = -1

  while not rhs_index_Queue.empty():
    rhs_index = rhs_index_Queue.get_nowait()

    for lhs_index in rhs_to_lhs[rhs_index]:

      if matches_rhs[lhs_index] == -1:
        return True
      elif distance_lhs[matches_rhs[lhs_index]] == -1:
        distance_lhs[matches_rhs[lhs_index]] = distance_lhs[rhs_index] + 1
        rhs_index_Queue.put(matches_rhs[lhs_index])

  return False

def depth_first_search(rhs_index, rhs_to_lhs, matches_lhs,
                       matches_rhs, distance_lhs):

  for lhs_index in rhs_to_lhs[rhs_index]:

    if matches_rhs[lhs_index] == -1:

      matches_rhs[lhs_index] = rhs_index
      matches_lhs[rhs_index] = lhs_index
      return True

    elif distance_lhs[matches_rhs[lhs_index]] == \
         distance_lhs[rhs_index] + 1:

      if depth_first_search(rhs_index    = matches_rhs[lhs_index],
                            rhs_to_lhs   = rhs_to_lhs,
                            matches_lhs  = matches_lhs,
                            matches_rhs  = matches_rhs,
                            distance_lhs = distance_lhs):
        matches_rhs[lhs_index] = rhs_index
        matches_lhs[rhs_index] = lhs_index
        return True

  distance_lhs[rhs_index] = -1
  return False

def bipartite_maximum_cardinality_matching():

  num_lhs = 4
  num_rhs = 5

  rhs_to_lhs = {0 : [1, 2, 3],
                1 : [2, 3, 0],
                2 : [3, 0],
                3 : [1],
                4 : [3]}

  # Perform the Hopcroft-Karp algorithm
  matches_lhs = [-1] * num_lhs
  matches_rhs = [-1] * num_rhs

  maximumCardinalityMatching = 0

  distance_lhs = [-1] * num_lhs

  while breadth_first_search(rhs_to_lhs   = rhs_to_lhs,
                             matches_lhs  = matches_lhs,
                             matches_rhs  = matches_rhs,
                             distance_lhs = distance_lhs):

    for i in range(num_lhs):

      if matches_lhs[i] == -1:
        if depth_first_search(rhs_index    = i,
                              rhs_to_lhs   = rhs_to_lhs,
                              matches_lhs  = matches_lhs,
                              matches_rhs  = matches_rhs,
                              distance_lhs = distance_lhs):
          maximumCardinalityMatching += 1

  # Extract the resulting configuration
  print(f"matches for the left-hand side: {matches_lhs}")
  print(f"matches for the right-hand side: {matches_rhs}")
