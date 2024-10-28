from typing import Any, Optional, Iterator, List


class TreeNode:
    def __init__(self, data: Any, parent: Optional['TreeNode'] = None):
        self.data: Any = data
        self.parent: TreeNode = parent
        self.children: List['TreeNode'] = []
        if parent:
            parent.children.append(self)

    def insert_child(self, data: Any) -> 'TreeNode':
        return TreeNode(data, parent=self)

    def __iter__(self) -> Iterator[Any]:
        result: List[Any] = [self.data]  # Start with the current node's data
        for child in self.children:
            result.extend(child)  # Recursively add data from each child
        return iter(result)

    def dump(self, indent: int = 0):
        print(
            "    " * indent + str(self.data)
        )
        for child in self.children:
            child.dump(indent + 1)


if __name__ == '__main__': 
    
    # Create a root node of the tree 
    root = TreeNode('Márcia') 
 
    # Insert children 
    child1 = root.insert_child('Diego') 
    child2 = root.insert_child('Nikhil') 
    child3 = root.insert_child('Terry')

    # Insert grandchildren 
    child21 = child2.insert_child('Jane') 
    child22 = child2.insert_child('Arnav') 
    child23 = child3.insert_child('Wei')

    # Insert 2nd gen grandchildren 
    child31 = child21.insert_child('Diego') 
    child32 = child22.insert_child('Armando') 
    child33 = child23.insert_child('Maradona')
    child34 = child23.insert_child('Vasia')

    # Insert 3rd gen grandchildren 
    child41 = child31.insert_child('Ruud') 
    child42 = child31.insert_child('Marco') 
    child43 = child32.insert_child('Pupkin')
    child44 = child33.insert_child('Petia')

    # Dumping the tree
    root.dump()

    # Traverse over the tree
    for node_data in root:
        print(node_data)

    child2.dump()