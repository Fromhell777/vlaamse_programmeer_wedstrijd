
# Trie is a type of k-ary search tree used for storing and searching a specific
# key from a set
class TrieNode:
  def __init__(self):
    self.children = [None] * 26 # 26 letters
    self.is_end_of_word = False

def create_node():
  node = TrieNode()
  node.is_end_of_word = False
  return node

def insert(root, key):
  curr_node = root

  for i in range(len(key)):
    index = ord(key[i]) - ord('a')

    if curr_node.children[index] is None:
      curr_node.children[index] = create_node()

    curr_node = curr_node.children[index]

  curr_node.is_end_of_word = True

def search(root, key):
  curr_node = root

  for i in range(len(key)):
    index = ord(key[i]) - ord('a')

    if curr_node.children[index] is None:
      return False

    curr_node = curr_node.children[index]

  return curr_node and curr_node.is_end_of_word

def is_empty(root):
  for i in range(26):
    if root.children[i] is not None:
      return False

  return True

def remove(root, key, depth = 0):
  if root is None:
    return None

  if depth == len(key):
    if root.is_end_of_word:
      root.is_end_of_word = False

    if is_empty(root):
      del root
      root = None

    return root

  index = ord(key[depth]) - ord('a')
  root.children[index] = remove(root.children[index], key, depth + 1)

  if is_empty(root) and not root.is_end_of_word:
    del root
    root = None

  return root

def display_util(visited, node, txt):
  index = 0
  while index < 26: # 26 letters
    if node.children[index]:
      txt += chr(ord('a') + index)
      if not node.children[index].is_end_of_word:
        display_util(visited, node.children[index], txt)
        txt = txt[0 : (len(txt) - 1)]
      else:
        if txt not in visited:
          visited.append(txt)

        if not is_empty(node.children[index]):
          display_util(visited, node.children[index], txt)
          txt = txt[0 : (len(txt) - 1)]

    index += 1

def display(root):
  visited = []
  txt = ''
  display_util(visited, root, txt)

  print("Content of Trie:")
  for i in range(len(visited)):
    print(visited[i])

# Driver Code
if __name__ == "__main__":
  keys = ["the", "a", "there", "answer", "any", "by", "bye", "their", "hero", "heroplane"]
  root = create_node()

  for i in range(len(keys)):
    insert(root, keys[i])

  print(f"Input keys: {keys}")

  print()
  print(f"Does the trie contain the word \"the\": {search(root, 'the')}")
  print(f"Does the trie contain the word \"these\": {search(root, 'these')}")
  print(f"Does the trie contain the word \"heroplane\": {search(root, 'heroplane')}")

  print("We delete the word \"heroplane\" from the trie")
  root = remove(root, "heroplane")
  print(f"Does the trie contain the word \"heroplane\": {search(root, 'heroplane')}")

  print(f"Does the trie contain the word \"hero\": {search(root, 'hero')}")

  print()
  display(root)
