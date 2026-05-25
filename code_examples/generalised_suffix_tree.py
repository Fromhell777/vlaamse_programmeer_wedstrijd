# A generalised Suffix-Tree. It holds multiple strings

# The reference must be shared by all the Nodes for a certain string
class LeafEnd:

  def __init__(self, end):
    self.end = end

# The Suffix-tree's node
class Node:

  def __init__(self, leaf, string_index = None):
    self.children = {}

    # This will be non-negative for leaves and will give index of suffix for
    # the path from root to this leaf. For non-leaf node, it will be -1
    self.leaf = {}
    self.suffix_index = {}

    # These two will store the edge label details from parent node to current
    # node. (start, end) interval specifies the edge, by which the node is
    # connected to its parent node. Each edge will connect two nodes, one
    # parent and one child, and (start, end) interval of a given edge will be
    # stored in the child node. Lets say there are two nodes A (parent) and B
    # (Child) connected by an edge with indices (5, 8) then this indices (5, 8)
    # will be stored in node B
    self.start = {}
    self.end = {}

    # This will point to other node where current node should point via suffix
    # link
    self.suffix_link = {}

    if string_index is not None:
      self.leaf = {string_index : leaf}
      self.suffix_index = {string_index : None}
      self.start = {string_index : None}
      self.end = {string_index : None}
      self.suffix_link = {string_index : None}

  def __eq__(self, node):
    return self.start == node.start and \
           self.end == node.end and \
           self.suffix_index == node.suffix_index

  def __ne__(self, node):
    return self.start != node.start or \
           self.end != node.end or \
           self.suffix_index != node.suffix_index

# The Suffix-Tree
class SuffixTree:

  def __init__(self):
    # Initiate the tree
    self.strings = []
    self.last_new_node = None
    self.active_node = None

    # Active_edge is represeted as input txt character index (not the character
    # itself)
    self.active_edge = -1
    self.active_length = 0

    # Remaining_suffix_count tells how many suffixes yet to be added in tree
    self.remaining_suffix_count = 0

    self.size = []
    self.root = None

    self.global_ends = []

  def edge_length(self, node, string_index):
    print(node.end)
    return node.end[string_index].end - node.start[string_index] + 1

  def walk_down(self, current_node, string_index):
    # Walk down from current node.
    #
    # Active_Point Change For Walk Down (APCFWD) using Skip/Count Trick (Trick
    # 1). If active_length is greater than current edge length, set next
    # internal node as active_node and adjust active_edge and active_length
    # accordingly to represent same active_point.
    length = self.edge_length(node         = current_node,
                              string_index = string_index)
    if (self.active_length >= length):
      self.active_edge += length
      self.active_length -= length
      self.active_node = current_node
      return True

    return False

  def new_node(self, string_index, start, end = None, leaf = False):
    # For root node, suffix_link will be set to None. For internal nodes,
    # suffix_link will be set to root by default in current extension and may
    # change in next extension
    node = Node(leaf, string_index)
    node.suffix_link[string_index] = self.root
    node.start[string_index] = start

    if leaf:
      node.end[string_index] = self.global_ends[string_index]
    else:
      node.end[string_index] = LeafEnd(end)

    # suffix_index will be set to -1 by default and actual suffix index will be
    # set later for leaves at the end of all phases
    node.suffix_index[string_index] = -1
    return node

  def extend_suffix_tree(self, pos, string_index):
    # Extension Rule 1, this takes care of extending all leaves created so far
    # in the tree
    self.global_ends[string_index].end = pos

    # Increment remaining_suffix_count indicating that a new suffix added to
    # the list of suffixes yet to be added in tree
    self.remaining_suffix_count += 1

    # Set last_new_node to None while starting a new phase, indicating there is
    # no internal node waiting for it's suffix link reset in current phase
    self.last_new_node = None

    # Add all suffixes (yet to be added) one by one in tree
    while (self.remaining_suffix_count > 0):
      if (self.active_length == 0):
        # Active_Point Change For Active Length Zero (APCFALZ)
        self.active_edge = pos

      # There is no outgoing edge starting with
      # active_edge from active_node
      if (self.active_node.children.get(self.strings[string_index][self.active_edge]) is None):
        # Extension Rule 2 (A new leaf edge gets created)
        self.active_node.children[self.strings[string_index][self.active_edge]] = \
          self.new_node(string_index = string_index,
                        start        = pos,
                        leaf         = True)

        # A new leaf edge is created in above line starting from  an existng
        # node (the current active_node), and if there is any internal node
        # waiting for it's suffix link get reset, point the suffix link from
        # that last internal node to current active_node. Then set
        # last_new_node to None indicating no more node waiting for suffix link
        # reset
        # TODO this must be done when the next node does not contain this string
        # yet
        if (self.last_new_node is not None):
          self.last_new_node.suffix_link[string_index] = self.active_node
          self.last_new_node = None

      # There is an outgoing edge starting with active_edge from active_node
      else:
        # Get the next node at the end of edge starting
        # with active_edge
        next_node = self.active_node.children.get(self.strings[string_index][self.active_edge])

        assert string_index in next_node.start # TODO test

        if self.walk_down(current_node = next_node,
                          string_index = string_index):  # Do walkdown
          # Start from next_node node (the new active_node)
          continue

        # Extension Rule 3 (current character being processed is already on the
        # edge)
        if (self.strings[string_index][next_node.start[string_index] + \
                                       self.active_length] == self.strings[string_index][pos]):
          # If a newly created node waiting for it's suffix link to be set,
          # then set suffix link of that waiting node to curent. active node
          if ((self.last_new_node is not None) and (self.active_node != self.root)):
            self.last_new_node.suffix_link[string_index] = self.active_node
            self.last_new_node = None

          # Active_Point Change For Extension Rule 3 (APCFER3)
          self.active_length += 1

          # STOP all further processing in this phase and move on to next_node
          # phase
          break

        # We will be here when activePoint is in middle of the edge being
        # traversed and current character being processed is not on the edge
        # (we fall off the tree). In this case, we add a new internal node and
        # a new leaf edge going out of that new node. This is Extension Rule 2,
        # where a new leaf edge and a new internal node get created

        # New internal node.
        # The suffix_link and suffix_index of the previous strings are incorrect
        # for this internal node. The suffix_link is not used anymore so that
        # doesn't matter. The suffix_index is only valid for leaf nodes so that
        # doesn't matter for this new node
        split = Node(leaf = False)
        split.start = next_node.start.copy()
        split.end = {key : LeafEnd(next_node.start[key] + self.active_length - 1) for key in next_node.end}
        split.suffix_link = next_node.suffix_link.copy()
        split.suffix_index = next_node.suffix_index.copy()
        split.leaf = {key : False for key in next_node.leaf}

        split.suffix_link[string_index] = self.root
        split.suffix_index[string_index] = -1

        self.active_node.children[self.strings[string_index][self.active_edge]] = split

        # New leaf coming out of new internal node
        split.children[self.strings[string_index][pos]] = self.new_node(string_index = string_index,
                                                      start        = pos,
                                                      leaf         = True)
        next_node.start = {key : value + self.active_length for key, value in next_node.start.items()}
        split.children[self.strings[string_index][next_node.start[string_index]]] = next_node

        # We got a new internal node here. If there is any internal node
        # created in last extensions of same phase which is still waiting for
        # it's suffix link reset, do it now
        if (self.last_new_node is not None):
          # suffix_link of last_new_node points to current newly
          # created internal node
          self.last_new_node.suffix_link[string_index] = split

        # Make the current newly created internal node waiting for it's suffix
        # link reset (which is pointing to self.root at present). If we come
        # across any other internal node (existing or newly created) in next
        # extension of same phase, when a new leaf edge gets added (i.e. when
        # Extension Rule 2 applies is any of the next extension of same phase)
        # at that point, suffix_link of this node will point to that internal
        # node
        self.last_new_node = split

      # One suffix got added in tree, decrement the count of suffixes yet to be
      # added
      self.remaining_suffix_count -= 1

      # Active_Point Change For Extension Rule 2 Case 1 (APCFER2C1)
      if ((self.active_node == self.root) and (self.active_length > 0)):
        self.active_length -= 1
        self.active_edge = pos - self.remaining_suffix_count + 1

      # Active_Point Change For Extension Rule 2 Case 2 (APCFER2C2)
      elif (self.active_node != self.root):
        self.active_node = self.active_node.suffix_link[string_index]

  def walk_dfs(self, current_node, depth = 0):
    string_index = next(iter(current_node.start))

    start = current_node.start[string_index]
    end   = current_node.end[string_index].end
    yield self.strings[string_index][start:end + 1], depth

    for node in current_node.children.values():
      if node:
        yield from self.walk_dfs(node, depth + 1)

  def set_suffix_index(self, string_index, node, current_height):
    pass
    # TODO fix
    #if node.leaf == 1:
    #  node.suffix_index = self.size - current_height

    #for child_node in node.children.values():
    #  self.set_suffix_index(node           = child_node,
    #                        current_height = current_height + \
    #                                         self.edge_length(child_node))

  def add_string(self, txt):
    string_index = len(self.strings)

    # Setup the global end value
    self.global_ends.append(LeafEnd(-1))

    if self.root is None:
      # Root is a special node with start and end indices as -1, as it has no
      # parent from where an edge comes to root
      self.root = self.new_node(string_index = string_index,
                                start        = -1,
                                end          = -1)

    self.strings.append(txt)
    self.size.append(len(txt))

    # First active_node will be root
    self.active_node = self.root

    for i in range(self.size[string_index]):
      self.extend_suffix_tree(pos          = i,
                              string_index = string_index)

    self.set_suffix_index(string_index   = string_index,
                          node           = self.root,
                          current_height = 0)

  def print_dfs(self):
    for sub_string, depth in self.walk_dfs(self.root):
      if depth == 0:
        print(f"-'root'")
      else:
        print(f"{' |' * depth}-{sub_string}")

# Driver Code
if __name__ == "__main__":
  txt1 = "abcabxabcd$"
  txt2 = "banana$"

  tree = SuffixTree()
  tree.add_string(txt1)
  tree.print_dfs()

  tree.add_string(txt2)
  tree.print_dfs()
