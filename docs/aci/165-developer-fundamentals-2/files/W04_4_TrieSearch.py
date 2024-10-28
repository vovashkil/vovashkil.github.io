class TrieNode: 
	def __init__(self):
		self.children = dict()
		self.is_end_of_word = False

class Trie:
	def __init__(self):
		self.root = TrieNode()
	def search(self, word: str):
		node = self.root

		for char in word: 
			if char not in node.children: 
				return False
			node = node.children[char]
		return node.is_end_of_word