
def floodfill_matrix():

  matrix = [[0,1,2],
            [3,4,5],
            [6,7,8]]

  y_size = len(matrix)
  x_size = len(matrix[0])

  visited = set()

  to_visit = [(0,0)]

  dirs = [[0, 1], [1, 0], [0, -1], [-1, 0]]

  while len(to_visit) > 0:
    position = to_visit.pop()

    if position not in visited:
      visited.add(position)

      for dy, dx in dirs:
        new_y = position[0] + dy
        new_x = position[1] + dx
        if new_y >= 0 and new_x >= 0 and new_y < y_size and new_x < x_size:
          if matrix[new_y][new_x] == f_something:
            to_visit.append((new_y, new_x))

def floodfill_graph():

  graph = {1 : [2],
           2 : [1],
           3 : [4, 5],
           4 : [3, 5],
           5 : [3, 4]}

  start_node = 1

  sub_graph = set()
  sub_graph.add(start_node)

  new_nodes = graph[start_node].copy()

  while len(new_nodes) > 0:
    new_node = new_nodes.pop()

    if new_node not in sub_graph:
      sub_graph.add(new_node)
      new_nodes.extend(graph[new_node])
