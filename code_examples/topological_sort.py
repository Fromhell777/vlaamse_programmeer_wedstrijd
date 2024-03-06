from queue import Queue

def topological_sort(graph):

  # Create a vector to store indegrees of all vertices. Initialize all
  # indegrees as 0. This count the amount of incomming edges
  in_degrees = {k : 0 for k in graph.keys()}

  # Traverse adjacency lists to fill indegrees of
  # vertices.  This step takes O(V + E) time
  for node in graph.keys():
    for adjacent_node in graph[node]:
      in_degrees[adjacent_node] += 1

  # Create an queue and enqueue all vertices with
  # indegree 0
  queue = Queue()
  for node, in_degree in in_degrees.items():
    if in_degree == 0:
      queue.put(node)

  # Initialize count of visited vertices
  cnt = 0

  # Create a vector to store result (A topological ordering of the vertices)
  top_order = []

  # One by one dequeue vertices from queue and enqueue adjacents if indegree of
  # adjacent becomes 0
  while not queue.empty():

    # Extract front of queue (or perform dequeue) and add it to topological
    # order
    node = queue.get_nowait()
    top_order.append(node)

    # Iterate through all neighbouring nodes of dequeued node u and decrease
    # their in-degree by 1
    for i in graph[node]:
      in_degrees[i] -= 1
      # If in-degree becomes zero, add it to queue
      if in_degrees[i] == 0:
        queue.put(i)

    cnt += 1

  # Check if there was a cycle
  if cnt != len(graph.keys()):
    return None
  else:
    return top_order

# Driver Code
if __name__ == '__main__':

  graph = {1 : [2],
           2 : [3],
           3 : [],
           4 : [3],
           5 : [3]}

  result = topological_sort(graph)

  if result is None:
    print("The graph contains a cylce")
  else:
    print(f"The topological sorted node are: {result}")
