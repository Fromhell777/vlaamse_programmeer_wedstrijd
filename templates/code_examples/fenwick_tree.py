
# Also called a binary indexed tree
class FenwickTree:

  # Constructs a Binary Indexed Tree for given array of size array_size
  def __init__(self, arr) :

    # Original array size
    self.array_size = len(arr)

    # Create and initialize tree[] as 0
    self.tree = [0] * (self.array_size + 1)

    # Store the actual values in tree[] using update()
    for i in range(self.array_size):
      self.updatebit(i, arr[i])

  def __str__(self):
    return str(self.tree[1:self.array_size + 1])

  # Returns sum of arr[0..index]. This function assumes that the array is
  # preprocessed and partial sums of array elements are stored in tree[]
  def getsum(self, index):
    result = 0 # Initialize result

    # Index in tree[] is 1 more than the index in arr[]
    index += 1

    # Traverse ancestors of tree[index]
    while index > 0:

      # Add current element of tree to sum
      result += self.tree[index]

      # Move index to parent node in getSum View
      index -= index & (-index)

    return result

  # Function to get sum on interval [l, r]
  def query(self, l, r):
    return self.getsum(r) - self.getsum(l - 1)

  # Updates a node in Binary Indexed Tree (BIT) at given index in tree. The
  # given added_value is added to tree[index] and all of its ancestors in tree
  def updatebit(self, index, added_value):

    # Index in tree[] is 1 more than the index in arr[]
    index += 1

    # Traverse all ancestors and add added_value
    while index <= self.array_size:

      # Add added_value to current node of tree
      self.tree[index] += added_value

      # Update index to that of parent in update View
      index += index & (-index)

# Driver code to test above methods
if __name__ == "__main__" :

  a = [2, 1, 1, 3, 2, 3, 4, 5, 6, 7, 8, 9]

  tree = FenwickTree(a)
  print(f"Sum of elements in arr[0..5] is {tree.getsum(5)}")

  a[3] += 6
  tree.updatebit(3, 6)
  print(f"Sum of elements in arr[0..5] after update is {tree.getsum(5)}")
