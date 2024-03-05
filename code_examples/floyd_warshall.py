
# Define infinity as the large
# enough value. This value will be
# used for vertices not connected to each other
INF = 99999

# Solves all pair shortest path via Floyd Warshall Algorithm
def floyd_warshall(costs, num_vertices):

  # Matrix that will finally have the shortest distances between every pair of vertices
  dist = [[INF for _ in range(num_vertices)] for _ in range(num_vertices)]

  # Matrix that will finally have the previous nodes for when traversing the
  # shortest distance between 2 vertices
  prev = [[None for _ in range(num_vertices)] for _ in range(num_vertices)]

  # Initialise the distance matrix with the edge weights
  for i in range(num_vertices):
    for j in range(num_vertices):
      # Fill in weigths for the edge (i, j)
      if i == j:
        dist[i][j] = 0
        prev[i][j] = i

      if (i, j) in costs:
        dist[i][j] = costs[(i, j)]
        prev[i][j] = i
      else:
        dist[i][j] = INF

  # Add all vertices one by one to the set of intermediate vertices.
  # 1) Before start of an iteration, we have the shortest distances between
  #    all pairs of vertices such that the shortest distances considers only
  #    the vertices in the set {0, 1, 2, ... k - 1} as intermediate vertices.
  # 2) After the end of a iteration, vertex number k is added to the set of
  #    intermediate vertices and the set becomes {0, 1, 2, ... k}
  for k in range(num_vertices):

    # Pick all vertices as source one by one
    for i in range(num_vertices):

      # Pick all vertices as destination for the above picked source
      for j in range(num_vertices):

        # If vertex k is on the shortest path from i to j, then update the
        # value of dist[i][j]
        if dist[i][j] > dist[i][k] + dist[k][j]:
          dist[i][j] = dist[i][k] + dist[k][j]
          prev[i][j] = prev[k][j]

  return dist, prev

def get_shortest_path(prev, start, end):
  if prev[start][end] == None:
    return []

  result = [end]
  while start != end:
    end = prev[start][end]
    result.append(end)

  result.reverse()
  return result

# Driver's code
if __name__ == "__main__":
  #
  #         10
  #    (0)------->(3)
  #     |         /|\
  #   5 |          |
  #     |          | 1
  #    \|/         |
  #    (1)------->(2)
  #         3

  num_vertices = 4

  graph = {0 : [1, 3],
           1 : [2],
           2 : [3],
           3 : []}

  costs = {(0,1) : 5,
           (0,3) : 10,
           (1,2) : 3,
           (2,3) : 1}

  result_dist, result_prev = floyd_warshall(costs, num_vertices)

  print("Following matrix shows the shortest distances " + \
        "between every pair of vertices")
  for i in range(num_vertices):
    line = ""
    for j in range(num_vertices):
      if result_dist[i][j] == INF:
        line += f"{'INF':>7}"
      else:
        line += f"{result_dist[i][j]:7}"

    print(line)

  print()

  for i in range(num_vertices):
    for j in range(num_vertices):
      print(f"Shortest route from {i} to {j}: {get_shortest_path(result_prev, i, j)}")
