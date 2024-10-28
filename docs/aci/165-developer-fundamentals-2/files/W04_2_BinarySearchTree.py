from typing import Optional, Iterator, List

class Node:
    def __init__(self, key: str):     
        self.key: str = key
        self.left: Optional[Node] = None
        self.right: Optional[Node] = None

class BinaryTree:
    def __init__(self):
        self.root: Optional[Node] = None

    def insert(self, key: str) -> None:
        self.root = self._insert(self.root, key)

    def _insert(self, root: Optional[Node], key: str) -> Node:
        if root is None:
            return Node(key)
        else:
            if key < root.key:
                root.left = self._insert(root.left, key)
            else:
                root.right = self._insert(root.right, key)
            return root

    def __iter__(self) -> Iterator[int]:
        return iter(self.inorder_traversal())

    def inorder_traversal(self) -> List[int]:
        result = []
        self._inorder_traversal(self.root, result)
        return result

    def _inorder_traversal(self, node: Optional[Node], result: List[int]) -> None:
        if node is not None:
            self._inorder_traversal(node.left, result)
            result.append(node.key)
            self._inorder_traversal(node.right, result)

    def dump(self) -> None:
        self._dump_tree(self.root, 0)

    def _dump_tree(self, node: Optional[Node], level: int) -> None:
        if node is not None:
            self._dump_tree(node.right, level + 1)
            print("    " * level + str(node.key))
            self._dump_tree(node.left, level + 1)


if __name__ == "__main__":
    # Example of usage
    points = ['Blake','Frank','Ava','111','Chloe','Ezra','Gale','Diego','Vasia','222','David',]

    # Create a binary tree
    phone_book = BinaryTree()

    # Insert points into the binary tree
    for point in points:
        phone_book.insert(point)

    # Dump the tree
    print("Binary tree with indentation")
    phone_book.dump()

    # Print the points using in-order traversal

    print("In-order traversal:")
    for point in phone_book:
        print(point)
