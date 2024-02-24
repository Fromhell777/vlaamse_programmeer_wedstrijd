
class SegmentTree:

  # Function to build the tree
  def __init__(self, arr) :

    # Original array size
    self.size = len(arr)

    # Max size of tree
    self.tree = [0] * 2**((self.size - 1).bit_length() + 1)

    # Insert leaf nodes in tree
    for i in range(self.size):
      self.tree[self.size + i] = arr[i]

    # Build the tree by calculating parents
    for i in range(self.size - 1, 0, -1):
      # Merging of 2 nodes. Can be replaced by another operation
      self.tree[i] = self.tree[i << 1] + self.tree[(i << 1) | 1]

  # Function to update a tree node
  def updateTreeNode(self, p, value):

    # Set value at position p
    self.tree[p + self.size] = value

    # Move upward and update parents
    i = p + self.size

    while i > 1:
      # Merging of 2 nodes. Can be replaced by another operation
      self.tree[i >> 1] = self.tree[i] + self.tree[i ^ 1]
      i >>= 1

  # Function to get sum on interval [l, r)
  def query(self, l, r):

    result = 0

    # Loop to find the sum in the range
    l += self.size
    r += self.size

    while l < r:

      # We are at a right node
      if (l & 1):
        # calculating the new result value of the combination of the two sub
        # modes. Can be replaces by another opreation
        result += self.tree[l]
        l += 1

      # We are at a left node
      if (r & 1):
        r -= 1
        # calculating the new result value of the combination of the two sub
        # modes. Can be replaces by another opreation
        result += self.tree[r]

      l >>= 1
      r >>= 1

    return result

# Driver Code
if __name__ == "__main__" :

    a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]

    # build tree
    s = SegmentTree(a)

    # print the sum in range(1,2) index-based
    print(s.query(1, 3))

    # modify element at 2nd index
    s.updateTreeNode(2, 1)

    # print the sum in range(1,2) index-based
    print(s.query(1, 3))
