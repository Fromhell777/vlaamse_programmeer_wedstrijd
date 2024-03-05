
class DisjointSetList:

  def __init__(self, size):
    self.parent = [i for i in range(size)]
    self.rank = [0] * size

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
      return

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
      return

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
