from queue import PriorityQueue

class DisjointSetDict:

  def __init__(self, nodes):
    self.parent = {i : i for i in nodes}
    self.rank = {i : 0 for i in nodes}

  # Function to find the representative (or the root node) of a set
  def find(self, i):
    # If i is not the representative of its set, recursively find the representative
    if self.parent[i] != i:
      self.parent[i] = self.find(self.parent[i]) # Path compression
    return self.parent[i]

  # Unites the set that includes i and the set that includes j by rank
  def union_by_rank(self, i, j):
    # Find the representatives (or the root nodes) for the set that includes i and j
    irep = self.find(i)
    jrep = self.find(j)

    # Elements are in the same set, no need to unite anything
    if irep == jrep:
      return False # To indicate if a union happened

    # Get the rank of i's tree
    irank = self.rank[irep]

    # Get the rank of j's tree
    jrank = self.rank[jrep]

    # If i's rank is less than j's rank
    if irank < jrank:
      # Move i under j
      self.parent[irep] = jrep
    # Else if j's rank is less than i's rank
    elif jrank < irank:
      # Move j under i
      self.parent[jrep] = irep
    # Else if their ranks are the same
    else:
      # Move i under j (doesn't matter which one goes where)
      self.parent[irep] = jrep
      # Increment the result tree's rank by 1
      self.rank[jrep] += 1

    return True # To indicate if a union happened

def kruskals_minimal_spanning_tree(graph, edges):

  # Create the disjoint set
  disjoint_set = DisjointSetDict(graph.keys())

  result = []
  cost = 0

  for edge, weight in sorted(edges.items(), key = lambda x : x[1]):
    # Check whether a union actually happened
    if disjoint_set.union_by_rank(edge[0], edge[1]):
      cost += weight
      result.append(edge)

  return cost, result

def prims_minimal_spanning_tree(graph, edges):

  # Contains the included nodes
  included_nodes = set()

  q = PriorityQueue()

  # Large value to initialise the queue of nodes
  init_large_value = 1e10
  first = True
  for node in graph.keys():
    if first:
      q.put((0, node, None))
      first = False
    else:
      q.put((init_large_value, node, None))

  result = []
  cost = 0

  while not q.empty():
    weight, node, edge = q.get()

    if node not in included_nodes:
      included_nodes.add(node)

      if edge is not None:
        cost += weight
        result.append(edge)

      for adjacent_node in graph[node]:
        if adjacent_node not in included_nodes:
          if adjacent_node < node:
            q.put((edges[(adjacent_node, node)], adjacent_node, (adjacent_node, node)))
          else:
            q.put((edges[(node, adjacent_node)], adjacent_node, (node, adjacent_node)))

  return cost, result

# Driver Code
if __name__ == '__main__':

  graph = {1 : [2],
           2 : [1, 3],
           3 : [2, 4, 5],
           4 : [3, 5],
           5 : [3, 4]}

  edges = {(1,2) : 2,
           (2,3) : 8,
           (3,5) : 1,
           (3,4) : 5,
           (4,5) : 1}

  cost, spanning_edges = kruskals_minimal_spanning_tree(graph, edges)

  print(f"Minimal spanning tree cost: {cost}")
  print(f"Minimal spanning tree edges: {spanning_edges}")

  cost, spanning_edges = prims_minimal_spanning_tree(graph, edges)

  print(f"Minimal spanning tree cost: {cost}")
  print(f"Minimal spanning tree edges: {spanning_edges}")
