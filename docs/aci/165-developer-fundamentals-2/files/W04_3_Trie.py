print ("Visualize Trie Data Structure")
from typing import List
from functools import reduce

class TrieNode:
    def __init__(self):
        self.children = dict()  # type: dict[str, TrieNode]
        self.is_end_of_word = False  # type: bool

class Trie:
    def __init__(self):
        self.root = TrieNode()
        self.word_count = 0

    def insert(self, word: str) -> None:
        node = self.root
        for char in word:
            if char not in node.children:
                node.children[char] = TrieNode()
            node = node.children[char]
        if not node.is_end_of_word:
            node.is_end_of_word = True
            self.word_count += 1
    
    
    def dump(self) -> None:
        self._dump_recursive(self.root, '')
        print(f'Total number of words in the Trie is: {self.word_count}.')

    def _dump_recursive(self, node: TrieNode, current_prefix: str) -> None:
        if node.is_end_of_word:
            print(f"{current_prefix} (end)")

        for char, child_node in node.children.items():
            print(f"{current_prefix} - {char}")
            self._dump_recursive(child_node, current_prefix + "    ")

if __name__ == '__main__':
    trie = Trie()

    trie.insert('robot')
    trie.insert('root')
    trie.insert('roof')
    trie.insert('us')
    trie.insert('use')
    trie.insert('user')
    trie.insert('home')
    trie.insert('homie')
    trie.insert('house')
    trie.insert('hone')
    trie.insert('horizon')
    trie.insert('hoorah')
    trie.insert('root')
    trie.insert('root')
    trie.insert('root')

    trie.dump()