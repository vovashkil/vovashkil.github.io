# Advanced Data Structures Part 2

* **back to AWS Cloud Institute repo's root [aci.md](../aci.md)**
* **back to repo's main [README.md](../../../README.md)**

## Trees

### Depth of a Node

The depth of a node is the distance from the root.

### Height of a Tree

The height of a tree is the depth of the deepest leaf node.

### Defining a TreeNode class

#### [Tree class practice](./files/W04_1_Tree.py)

### Knowledge Check

#### Data trees are a structure for storing data. Which statement describes data trees?

* Data is stored in a hierarchical relationship.

Wrong answers:

* Data in a data tree can only consist of string type data.
* A disadvantage of data trees is the increased time to search them.
* You can join two trees together using the concatenate method.

By definition, data in trees is stored in a hierarchical relationship where child nodes are related to the parent node above them. Each node of the tree can become a subtree if additional nodes are subcategories of that node.

Data in trees can consist of any type of data.

Trees have the advantage of decreased time to search, insert, or delete items in them because large portions of data are ignored at each node visited.

The concatenate method is only used for strings, not for data trees.

#### Which data storage structures is represented by a data tree? (Select TWO.)

* A table of contents for a textbook listing chapter headers and subheadings within each chapter.
* Listing all cars manufactured in 2023 organized in nested categories by manufacturer, then make, then model, and then trim level.

Wrong answers:

* A single line of people waiting to buy tickets for one of the five movies playing that night at the theater.
* A GPS coordinate system showing specific points on the map representing roads in a city.
* A stack of documents used by a teacher in the classroom, organized chronologically from oldest to most recently used.

Data trees hold data in a hierarchical relationship, where each level or category relates directly to the previous level or category.

Good examples of this include listing all cars manufactured in a specific year in categories by manufacturer, then make, then model, and then trim level. Using chapter titles and subcategories in a table of contents is another good example of a data tree structure.

A single line of people waiting to buy tickets and a stack of papers in chronological order represent queues. Processing data in the queue would require processing each data point individually, one at a time, in the order in which they are received.

A GPS coordinate system with points connected by roads in a city is an example of data stored in a graph, not a data tree.

#### Which option describes leaf nodes? (Select TWO.)

* Leaf nodes are connected by an edge to one other node.
* A leaf node does not have any children.

Wrong answers:

* Leaf nodes have no siblings.
* Leaf nodes can only appear at the highest level of the tree.
* A leaf node can be the parent of a subtree.

A leaf node does not have any children and is connected to only one other node, its parent.

Leaf nodes can appear at any level of the tree. One subtree can have leaf nodes at a different level than another subtree.

Multiple leaf nodes can be siblings to one another if they share the same parent.

A leaf node is not a parent, because it has no children. By definition, a node with children is not a leaf node.

### Summary

A tree data structure can be used to store **hierarchical** data.

Trees as data structures consist of nodes arranged with one **root node** at the top (called level 0) and each succeeding **level** of the tree containing one or more nodes. The succeeding levels represent hierarchical subcategories of the data identified in the root node key.

Nodes at the bottom level of the tree (with the highest number) or ones that do not have children at any level of the tree are called **leaf nodes**.

The **advantage** of organizing data into hierarchical data trees is the speed of searching, inserting, or deleting data. This increased speed is because you can ignore large quantities of data at each decision point or path. The rest of the data does not need to be processed.

Some **examples of trees as a data structure** include the following:

* Nested file folders in your computer directory
* Organizing cars by manufacturer, then by model, make, and trim level
* Organizing items sold in a store by department, then successively smaller subcategories within that department

To use a tree in Python, you will need to define a tree class with nodes that contain data and pointers to the parent node and children nodes.

## Binary Trees: AVL & Red-Black Trees

### Pre-assessment

#### Which option describes binary search trees?

* Both numbers and letters can be used as key values in binary search trees.

Wrong answers:

* All child nodes on the left subtree of any node are greater than the key value of the parent node.
* Every parent (internal) node must have exactly two child nodes to be called binary.
* All child nodes on the right subtree of any node are less than the key value of the parent node.

All binary search trees have these requirements:

* The parent nodes can have up to and including two child nodes. There is no requirement that it be exactly two nodes. A binary tree can have nodes that have only one child or no children.
* All nodes with a value lower than the key value are on the left subtree and all nodes with a value greater than the key value are on the right subtree.
* Numbers are typically used as key values, but any other key (including alphabetic characters) with a known cardinal order can be used as key values, such that it is clear whether a value is greater than or less than each key value.

#### Which option describes AVL trees?

* AVL trees are self-balancing.

Wrong answers:

* The height of left and right subtrees in any AVL tree can vary by no more than two.
* AVL trees are NOT binary search trees.
* AVL trees are always perfectly balanced, such that the size of each subtree for any two siblings is the same.

An AVL tree is a binary search tree with special properties designed specifically for its use case. As such, they are as follows:

* Self-balancing
* Have left and right subtrees whose height varies by no more than one

AVL trees are not perfectly balanced. They are set up to allow trees to exist in a good enough balance situation so that the searching, inserting, and deleting of elements can be improved.

#### Which options describes red-black trees?

* A **red-black tree** performs better than an AVL tree for **frequent insertions** or **deletions**.

Wrong answers:

* With red-black trees, the root and the leaf nodes are always red.
* A red parent node is allowed to have a red child node.
* An AVL tree is self-balancing, but a red-black tree is not.

Both AVL trees and red-black trees are self-balancing after every operation, using different rules for balancing.

Because of the differences in these rules, an AVL tree is best for a tree that will require frequent searches, whereas a red-black tree is best for one that will require frequent insertions or deletions of data.

The rules for establishing a red-black tree include that all roots and leaf nodes must be black and that a red parent node cannot have a red child node.

## Binary Search Trees

With binary search trees, you can hone your search by reducing the number of elements that need to be searched into smaller groups with each decision you make.

Binary search trees have many practical applications. One common use is a dictionary or phone book lookup, where elements in the dataset are arranged in numerical or alphabetical order. Binary search trees are used by spell checkers to search quickly for matching words. They can also be used to find the closest match in a dataset, such as finding the best match for a specific stock price.

**With a binary search tree, the number of steps taken to find any item in the tree is never more than the height of the tree.**

#### [Binary search tree practice]()

## AVL Trees
The AVL tree is named after its inventors Georgy Adelson-Velsky and Evgenii Landis.

An AVL is a form of a binary tree with the following characteristics:

* All nodes in the tree have the AVL property: the heights of their left and right subtrees differ by no more than 1.  
* The difference of heights of left and right subtrees is known as the “balance factor”.
* AVL trees are self-balancing and required to meet the AVL properties after every operation.

## Red-Black Trees

1. All nodes of a red-black tree are either red or black.
2. The root of the red-black tree is always black.
3. There are no two adjacent red nodes.
4. NIL nodes are the leaves and black.
5. All leaves (NIL nodes) have the same black depth.
6. An only child of any node is always red.

### AVL compared to red-black trees

Although AVL trees are more balanced as compared to red-black trees, this balancing comes at the price of causing more rotations during insertion and deletion.

To determine the best tree type for your use case, use the following qualifiers:

* If your application requires **frequent insertions or deletions**, then a **red-black tree** is preferred.
* If your application has more **frequent searches** (and less frequent insertions or deletions) then an **AVL** tree is preferred.

### Knowledge Check

#### Which statement describes red-black trees? 

* The black depth of any leaf NIL node is the same for all leaves.

Wrong answers:

* Each node MUST have two children.
* A red node can be a leaf node.
* The root of the tree is always red.

A red-black tree always has a black root node.  

Because it is a binary search tree, each node can have up to two children, but they are not required to have two children. A node could have one child or no children.

Leaves in a red-black tree are black NIL nodes. The black depth of any NIL node is the same for all leaves.

#### Which statement describes the comparison between AVL trees and red-black trees?

* Both AVL and red-black trees are self-balancing.

Wrong answers:

* AVL trees are binary search trees, but red-black trees are NOT.
* AVL trees are better for frequent insertions, and red-black trees are better for frequent searching.
* Both AVL and red-black trees require that the heights of left and right subtrees differ by no more than 1.

Both AVL and red-black trees are self-balancing binary search trees.

AVL trees are better for frequent searching because they are more balanced.  

Red-black trees are better for frequent insertions and deletions because their rules do not require rebalancing as often as AVL trees.

Only AVL trees require that heights of left and right subtrees differ by no more than 1.  Red-black trees balance based on the black depth of the NIL nodes.

### Summary

#### Binary search trees

Binary search trees are a specific data structure with the following characteristics:

* Each parent node can have up to two child nodes.
* The **left child** node is a subtree with values **less than the parent** node.
* The **right child** node is a subtree with values **greater than the parent** node.

To create binary search trees that increase speed and efficiency for insertion, deletion, or searching, there are specialized types of binary search trees that rebalance themselves after every operation according to specific rules. Each type is designed for a specific use case.

#### AVL trees

AVL trees have the following characteristics:

* All nodes in the tree have the AVL property, meaning the heights of their left and right subtrees differ by no more than 1.
* The difference of heights of left and right subtrees is known as the balance factor.

#### Red-black trees

Red-black trees have the following characteristics:

* Every node is either red or black.
* The root of the tree and all the leaves (NIL nodes) are always black.
* There are no two adjacent red nodes.
* All leaves have the same black depth.

## Trie Data Structures

### Pre-assessment

#### Which statement describes the trie data structure?

* Paths from any node to their children are called edges.

Wrong answers:

* Any node can have at most two children—left and right.
* Each node contains either a group of pointers to children or a Boolean value.
* Two pieces of data cannot share the same node.

A trie structure is a specialized tree that stores string data along paths between nodes called edges.

Each edge contains a character of the string, and multiple pieces of similar data can share paths and nodes along the path.

Each node contains a group of pointers to possible children and a Boolean value that signals if the word or string has ended at that node.  

There is no arbitrary limit to the number of children each node can have, which will depend on the characteristics of the data stored.

#### Which type of data is stored in a trie?

* String

Wrong answers:

* Numeric
* Boolean
* List

Data in a trie is string data, which is stored one character at a time in nodes.  

Any other data type would need to be converted to a string before storing it in a trie structure. For example, if you used a trie to store phone numbers so that you could search by area code, the phone numbers would need to be converted from the number format to a string format.

#### Which statement describes inserting new items into an existing trie? 

* Each node will contain one character of a string, and the same nodes can be shared between different data strings.

Wrong answers:

* All nodes you need will already be built. You will just need to traverse them to the correct place.  
* If the Boolean flag is set to false at any node you visit, you should stop the process because it is not possible to insert the new string into this trie.
* There will be no two nodes in the same trie that hold the same character. When a node with a character is added, all strings containing that character will add a path to travel through that node.

As strings are added to an existing trie, each node will contain one character of that string. If the node containing the needed character is already in the correct place along the path of the string, two or more strings can share the same nodes.

Nodes are only built as they are used, and new nodes will need to be built along paths if they do not already exist as new strings are added to the trie. 

If the Boolean flag is set to false, it means that the string or word is not yet complete at that node and that additional nodes are coming that will complete the string.  

Because nodes are part of paths that spell the strings with one character per node, there can be multiple nodes containing the same character as the key value along the same or different paths.  

#### How does autocomplete work with a trie data structure?  

* Using a prefix of the search term, it returns all possible strings in the trie that start with that prefix.

Wrong answers:

* It uses online search engines to figure out what you are searching for.
* It uses a self-balancing binary search tree to optimize the time spent searching.
* It searches every object in the tree to determine if the string you are looking for exists before inserting it.

Using a prefix search, autocomplete works with a trie data structure to reduce the time spent searching for strings in a trie.

Although online search engines often use a trie data structure to store previous searches and to offer suggestions for your search, a trie does not access the internet to complete its search. 

Trie structures are not self-balancing.  Because they contain string data with pointers in each node to every possible character in a string, they are also not binary trees.

The advantage of using a trie to store string data is that each node traversed in a search eliminates large branches of the trie data that must be traversed. Only a few nodes must be searched to find the data. The number of nodes searched is no more than the length of the string, no matter how large the trie is.

### Trie Data Structure and Purpose

#### Tries defined

*Trie* is derived from the word *retrieval*, and it's pronounced either “tree” or “try.”

A trie is used for storing and searching data of a specific key from a set.

One of the advantages of using a trie to store the data is that the search complexity is always exactly the length of the key.

A trie is a special-use tree for any of the following:

* Print words in alphabetical order
* Search for a string in a large collection of strings, such as a dictionary or phone book
* Search for a prefix of a string
* Perform an autocomplete operation, such as the one you often see when typing in an online search field

#### Properties of trie data structure

* There is one root node in each trie.
* Each node of a trie represents a string type of data that can include alphabets, numbers, and special characters.
* Each edge of a trie represents a character.
* Each node consists of an array of pointers to child nodes plus a Boolean variable or flag to indicate if the string ends at the current node.
* Each path from the root to any node represents a word or string.

#### Review the steps to add a new string to a trie

1. Initialize the variable: currentNode = the root node.
2. For each character in the string you are adding, if there is not already a child node with that name, create the child node. Then, move the currentNode pointer to it.
3. When you reach the end of the string you are adding, change the Boolean flag variable at the last node to True, and add 1 to the WordCount counter.

### Defining a trie with a dictionary

#### Dictionaries

The data type dict is a standard data type in Python and has methods used to implement and use it.

Here are some of the key points to remember about dictionaries in Python:

* Dictionaries are used to store key-value pairs in the form of key:value.  
* The values in the dictionary can be of any data type, and one dictionary can contain multiple data types, including strings, integers, Boolean values, and lists.  
* As of Python 3.7, dictionaries are ordered, meaning that any values placed in them will have a distinct order and that order will not change.
* Duplicate items are not allowed in dictionaries. Dictionaries cannot have two items with the same key. (This makes them especially helpful for our trie because they will not accidentally allow you to duplicate data in the same node.)
* You can find the length of a dictionary using the len() method.

### Defining a TrieNode

Each TrieNode has two pieces of information—a dictionary (self.children) and a Boolean variable (self.is-end-of-word).

A dictionary always contains key:value paired sets. In this case, the key is the node name or the string character represented by that node. The value is the pointer to a TrieNode for that key value.

A dictionary can contain one or many key:value paired sets. In our case, it will contain one set for each pointer leaving that node. We will not create a paired set for any string character that has not yet been added to the tree.

Our Boolean variable, self.is-end-of-word, tells us whether we have reached the end of a word at that node. It is initially set to False, but it will be changed to true when the end of a string is reached.

```
class TrieNode:
    """Node class for Trie data structure""" 
 
    def __init__(self): 
        """TrieNode constructor""" 
        # Each node in the trie has a dictionary for child nodes 
        self.children = dict()  # type: dict[str, TrieNode] 
        # Is current node the end of a word 
        self.is_end_of_word = False  # type: bool
```

### Defining a trie

```
class Trie: 
    """Trie data structure""" 
 
    def __init__(self): 
        """Trie constructor""" 
        # Create empty root node 
        self.root = TrieNode() 
```

### Defining a method to insert into a trie

```
def insert(self, word: str) -> None: 

        node = self.root
```

Now, we iterate through each character in the string using a for loop. We use the not operator to test if the character char already exists in the dictionary of children, node.children, and if it does not, we add a node in that location. If it does, we move to the child node and loop back through the for loop until we reach the end of the word.

```
        # Iterate through each character in the word 
        for char in word: 
            # If the current character is not in the children of the current node, add it 
            if char not in node.children: 
                node.children[char] = TrieNode() 
            # Move to the child node 
            node = node.children[char]
```

After we reach the end of the word, we change the Boolean variable in that node (**node.is_end_of_word**) to True because that node contains the last character of our word.

```
        # Mark the end of the word 
        node.is_end_of_word = True 
```

### Defining methods to print or dump a trie

```
    def dump(self) -> None:
        """Visualize the trie structure"""
        self._dump_recursive(self.root, '')

    def _dump_recursive(self, node: TrieNode, current_prefix: str) -> None:
        """Recursively visualize the trie structure

        Args:
            node (TrieNode): The current node in the trie.
            current_prefix (str): The current prefix being built during visualization.

        Returns:
            None
        """
        # If the current node represents the end of a word, print it
        if node.is_end_of_word:
            print(f"{current_prefix} (end)")

        # Recursively traverse the child nodes
        for char, child_node in node.children.items():
            print(f"{current_prefix} - {char}")
            self._dump_recursive(child_node, current_prefix + "    ")
```

### Defining main program code to create and print a trie

```
if __name__ == '__main__':
    # Example:
    trie = Trie()

    # Insert words into the trie
    trie.insert('robot')
    trie.insert('root')
    trie.insert('roof')
    trie.insert('us')
    trie.insert('use')
    trie.insert('user')
    trie.insert('home')
    trie.insert('homie')
    trie.insert('house')

    # Dump the trie
    trie.dump()
```

### [True practice](./files/W04_3_Trie.py)

### [Searching for a Value in a Trie](./files/W04_4_TrieSearch.py)

### Autocomplete With the Trie Data Structure

#### Prefix searching

One common application of a trie is storing a dataset that is searched or retrieved often. In this type of dataset, pre-processing the data by storing prefixes instead of individual characters reduces search time and computing resources.

A prefix consists of the first few characters in a string or the first few words that begin a phrase.

For example, if the prefix **inter** was stored in a single node instead of five nodes, it would save four paths and four nodes visited each time someone searched for any of the following words:

* **inter**action
* **inter**national
* **inter**mission
* **inter**ject
* **inter**im
* **inter**ested
* **inter**active
* **inter**fere
* **inter**cept
* **inter**mediate
* **inter**rupt

#### Autocomplete with prefix search

```
def prefix_search(self, prefix: str) -> List[str]: 
        """Search for autocomplete suggestions with the given prefix 
 
        Args: 
            prefix (str): The prefix to search for 
 
        Returns: 
            List[str]: A list of autocomplete suggestions 
        """ 
        # Start from the root node 
        node = self.root 
 
        # Traverse the trie based on the given prefix 
        for char in prefix: 
            if char not in node.children: 
                # If the prefix is not in the trie, return an empty list 
                return [] 
 
            # Move to the child node 
            node = node.children[char] 
```

Now that we have determined that the prefix we entered shows up in at least one word in our trie, it is time to do a depth-first search to find all the words with a given prefix. We start by creating a list of strings (**words_with_prefix**) that will contain all the existing strings in our trie that contain the given prefix and initialize the list with an empty list. Then, we perform a **_depth_first_search**, (defined later) and feed it with three parameters—the current node, the prefix we are searching for, and a list of words containing that prefix.

The following code is part of the previous **prefix_search** method.

```
        # Perform a depth-first search to find all words with the given prefix 
        words_with_prefix = []  # type: List[str] 
        self._depth_first_search(node, prefix, words_with_prefix) 
        return words_with_prefix 
```

Finally, we define the method **_depth_first_search**, which takes the following three parameters:

* The current **node** in the tree that we are searching
* The **current_prefix**, which is being added to each time we iterate this method
* The **result**, which is a list where we will store all the autocomplete suggestions for strings currently in our trie that start with the prefix

Each time this method is called, we check to see if the Boolean variable in the current node, **is_end_of_word**, is true. If it is, we append the **current_prefix**, which is the word we are currently on, to the result list.

Next, using a for loop, we traverse through each character (**char**) in the **node.children.items**, calling the method **_depth_first_search** recursively and concatenating the current **char** to the **current_prefix** each time as we travel to the end of the string.

```
def _depth_first_search(self, node: TrieNode, current_prefix: str, result: List[str]) -> None: 
        """Perform a depth-first search to find all words with the given prefix 
 
        Args: 
            node (TrieNode): The current node in the trie 
            current_prefix (str): The current prefix that is being built during the search 
            result (List[str]): The list to store autocomplete suggestions 
 
        Returns: 
            None 
        """ 
        # If the current node represents the end of a word, add it to the result 
        if node.is_end_of_word: 
            result.append(current_prefix) 
 
        # Recursively traverse the child nodes 
        for char, child_node in node.children.items(): 
            self._depth_first_search(child_node, current_prefix + char, result) 
```

The last two methods that we will define in our class **Trie** are **dump** and **_dump_recursive**, which work together to recursively travel through the trie and print out the list of strings that are suggested autocomplete options for the prefix we entered.

```
def dump(self) -> None:
        """Visualize the trie structure"""
        self._dump_recursive(self.root, '') 
 
    def _dump_recursive(self, node: TrieNode, current_prefix: str) -> None: 
        """Recursively visualize the trie structure 
 
        Args: 
            node (TrieNode): The current node in the trie
            current_prefix (str): The current prefix being built during visualization
 
        Returns: 
            None 
        """ 
        # If the current node represents the end of a word, print it 
        if node.is_end_of_word: 
            print(f"{current_prefix} (end)") 
 
        # Recursively traverse the child nodes 
        for char, child_node in node.children.items(): 
            print(f"{current_prefix} - {char}") 
            self._dump_recursive(child_node, current_prefix + "    ") 
```

Now that we have built the class and the methods to use **Trie** and **TrieNode**, we can perform the following actions:

* Insert words into the tree
* Dump (or print) the tree
* Perform a search
* Show results

Refer to the following code block to view an example of these actions.

```
if __name__ == '__main__': 
    # Example: 
    trie = Trie() 
 
    # Insert words into the trie 
    trie.insert('robot') 
    trie.insert('root') 
    trie.insert('roof') 
    trie.insert('us') 
    trie.insert('use') 
    trie.insert('user') 
    trie.insert('home') 
    trie.insert('homie') 
    trie.insert('house') 
 
    # Dump the trie 
    trie.dump() 
 
    # Perform the search 
    prefix_to_search = 'ro' 
    autocomplete_suggestions = trie.prefix_search(prefix_to_search) 
 
    # Show the results 
    print( 
        f"Autocomplete suggestions for '{prefix_to_search}': {autocomplete_suggestions}" 
    )
```

### Knowledge Check

#### Which statements are TRUE about the structure of a trie? (Select TWO.)

* A trie saves storage space by sharing nodes among multiple strings.
* The height of the tree equals the length of the longest string stored in it.

Wrong answers:

* Common use cases for a trie include formulas and numerical calculations.
* An array is more efficient than a trie as a data structure for large sets of strings.
* A trie is a specialized type of binary decision tree.

A trie is a data structure that stores strings and saves space by sharing nodes among multiple strings. They are commonly used for storing large sets of strings, such as dictionaries, lookup tables, and phone books.  

Because a trie only stores and retrieves strings, it is not a good option for formulas or calculations.

An array is less efficient than a trie for large sets of strings because arrays require each string to be stored individually, rather than sharing memory space with similar strings.

A trie is not a binary tree because each node can be the parent of dozens of child nodes.

#### What does the method do if it finds that a word is not yet in the tree when inserting it?

* It adds needed nodes one at a time until it reaches the end of the word.

Wrong answers:

* It drops out of the method and returns an empty list variable.
* It returns the Boolean variable as False because the word is not present.
* It subtracts 1 from the wordCount variable.

When adding a new word into a trie, the method will traverse the existing trie one character at a time, adding nodes for any characters needed that do not already exist at the proper location. When the method reaches the end of the word, the Boolean variable is changed to True to signify that the end of the word has been reached at that node, and the wordCount variable is increased by 1.

### Summary

A trie is a specialized data tree structure that is often used to store strings. Each node of the tree is a separate string character. A trie can share nodes between strings. The height of the tree (and thus the searching complexity) is exactly the length of the longest string stored in it.

This trie example stores the following 13 strings: "are", "art", "arts", "and", "ant", "dog", "do", "dad", "daddy", "dam", "dare", "dark", and "dart".

A trie is often used for storing and searching dictionaries, phone books, or other similar string-type data that is accessed frequently.

Because there is not a standard trie class in Python, the developer can create the class in a way that best works for the data and searching methods that will be used with that data. In this lesson, we used a dictionary of pointers to create a trie. Other methods might also be possible. 

Each node in a trie contains string data for that node, plus pointers to possible child nodes, and a Boolean variable that is changed to True when a word or string is completed at that node.

Often in implementation, there is also an integer variable that is incremented to count the number of completed words or strings that are entered into the trie.

When searching through a trie, one common practice is to use prefixes as search terms. If the prefix is found, you can continue searching, but if it is not found, you can end your search. When using prefixes, you can create methods of depth-first traversal of the trie that can provide you with a list of autocomplete suggestions. These are strings in the trie that contain the prefix used for the search. Autocomplete options are often seen in internet browser search windows.

## Graph Data Structure

### Pre-assessment

#### Which kind of data would be stored in a graph data structure?

* Data points that are related to other data points in weight or distance

Wrong answers:

* Data that needs to be searched frequently because graphs are best for retrieval
* Only numerical data so that tables and bar charts can be made
* Graphs have the greatest flexibility about how data is stored, so they are best for almost all data structure needs

Graphs are best for storing data that has a relational weight or distance to other data points.  

Although the relationship between data points can be shown in a pictorial representation, graph data structure does not represent bar charts or line graphs you might create in a spreadsheet program with numerical data.

Because graphs are a special use case for specific data, they are not good for widespread use with all data stored.

#### Like trees, graphs have nodes of data and relationship connections between the data. What are the nodes and relationships called in a graph?

* Vertices and edges

Wrong answers:

* Nodes and leaves
* Nodes and methods
* Arcs and blocks

The nodes of a graph are referred to as vertices. The connections between the vertices are edges if they are undirected and arcs if they are directed.

#### What is the degree of a vertex in a graph?

* Total number of edges that connect to a vertex

Wrong answers:

* Angle at which the edges connect to the vertex  
* Difference between the length of the longest edge and the length of the shortest edge that connects to that vertex
* Difference between the number of incoming edges and outgoing edges

The degree of a vertex is the total number of edges that connect to that vertex.  

No connection angle is measured on the graph.  

The number of incoming edges is referred to as the in-degree, and the number of outgoing edges is referred to as the out-degree of a vertex.

### Graph Data Structure and Uses

At its simplest form, a graph is a pictorial representation of a set of objects where some pairs of objects are connected by links. The links that connect the objects are called edges. The graph has many similarities to the tree data structure, but also some important distinctions.

### Comparing trees and graphs

Both trees and graphs are non-linear data structures, but they have distinct differences.

### Definition and structure

#### Trees

* A collection of **node**s and **edges**.
* The nodes are **connected**.
* Each tree has a **root** node.

#### Graphs

* A collection of **vertices or nodes** and **edges**.
* The nodes can be **connected** or **disconnected**.
* Graphs do **NOT** have a root node.

### Cycles and loops

#### Trees

* Edges are always directed away from the root.
* There will not be any loops or cycles within a tree.

#### Graphs

* Edges can be directional or undirected.
* With directed edges, loops or cycles can be formed.

### Relationships between nodes

#### Trees

* Relationships between nodes are hierarchical in a parent-child relationship from one level to the next. Each node can have at most one parent, except for the root node, which has no parent.
* Nodes at the same level can be siblings to each other if they share the same parent. Child nodes can also become parent nodes as the root of their own subtree.

#### Graphs

Relationships between nodes are links or edges, which can be multi-directional. There is no hierarchical relationship. Graphs can have any number of connections to other nodes and there is no parent-child relationship.

### Applications and common uses

#### Trees

* Trees are used in decision trees where one decision might change the path of the next decision.
* Trees are also used to represent data with hierarchical structure such as file systems, organization charts and family trees.

#### Graphs

Graphs are used to model complex systems or relationships, and are often used for finding the shortest path in a networking application, such as social networks, transportation networks and computer networks.

### Review of graph vocabulary

#### Vertex

Represents an individual data point that can be connected to another data point through an edge. The vertices in this graph are A, B, C, D, and E.

#### Edge

A simple connection between two vertices, which is usually represented as a straight-line segment between two points.

#### Adjacent vertices

Two vertices that are connected by one edge are adjacent.

#### Undirected graph

An undirected graph has edges that can be traversed in a path going in either direction.

#### Directed graph

A directed graph has paths or edges that only flow in one direction that is represented by an arrow.

#### Arc

An arc is an edge defined with a specific direction of travel from one vertex to another.

#### Path

In a graph, a path is an alternating set of vertices and edges. Each vertex is connected by an edge.

Paths can start at one vertex and arrive at another vertex several degrees removed.

There might be more than one path to arrive at the same destination. 

#### Simple path

A simple path has no cycles and does not repeat vertices.

#### Cycle

A cycle is a path that begins and ends at the same vertex. It is also known as a loop.

#### In-degree

The number of arcs or edges that point toward a given vertex is the in-degree of that vertex. 

#### Out-degree

The number of arcs or edges of a vertex that point away from the given vertex is the out-degree of that vertex.

#### Source vertex

A source vertex does not have any arcs coming into it, and only arcs that leave it or point away from it. A source vertex has an in-degree of zero.

#### Sink vertex

A sink vertex does not have any arcs leaving it. All arcs or paths touching it point towards it. We say that a sink vertex has an out-degree of zero.

#### Bridge

A bridge is an edge connecting two parts of a graph, which if removed would separate the tree into two disconnected graphs.

#### [Review of Graph Vocabulary.pdf](./files/Week04-ReviewOfGraphVocabulary.pdf)

### Graphs in the Real World

#### Uses of graphs

* Social media analysis
* Network monitoring for potential bottlenecks
* Financial trading analysis for decision making
* Management of Internet of Things (IoT)
* Modeling environment for autonomous vehicles
* Tracking disease outbreaks and containment
* Tracking links between web pages on the internet

#### Advantages

Structuring data in graph format has advantages for the right kinds of data. A graph is great for the following use cases.

* **Network analysis:** This could be networks of any kind, not just computer networks. It can include utilities, social media connections, wiring diagrams, transportation routing, and cost analysis for multiple options.
* **Pathfinding:** Graph algorithms can help identify the shortest path within a network that is represented in your graph.
* **Visualization:** Graphs are ideal to use for quick communication of complex data relationships.

#### Disadvantages

* **Limited representation:** Although graphs are great at representing relationships between objects, they cannot represent the properties and attributes of each object. For example, a graph can show the distances between multiple cities in Massachusetts, but it does not show population, income level, property taxes, fun things to do in each city, weather patterns, or the hundreds of other data points someone might need when researching a city.
* **Difficulty in interpretation:** If a graph is large or complex, it can be difficult to interpret its information. For example, a graph containing distances between your home, your workplace, and the grocery store would be easy to interpret. But if the graph contained distances for a self-driving vehicle from its current location to every other crossroad and driveway in a given town, the graph could require advanced analytical techniques.
* **Scalability issues:** Because many graph algorithms require traversing vertices in the graph to make decisions or insert or delete information, graphs are not easily scalable. As they increase in size and complexity, the time to process or work with them increases.
* **Lack of standardization:** Because there are numerous kinds of graphs, graphing algorithms, rebalancing rules and methods used to traverse them, and comparing data from one graph to another can be difficult.

### Graphs in Python Code

Because each vertex is unique, the vertex will be the key to our dictionary pairs, and the list of edges that connect to that vertex will be the values for that key.

We start by naming a variable graph for our dictionary and list the vertices as the keys.

The values stored for each key are the names of adjacent vertices. For example, in the following code, vertex 'a' has two edges in its value list—one connecting it to 'b' and one connecting it to 'c'. Later, we will use this information to print the line segment names.

```
# Import the Dict, List, and Tuple types from the typing module 
from typing import Dict, List, Tuple

# Initialize a graph of type Dict
# Its keys are strings, values are lists of strings
graph: Dict[str, List[str]] = { 
    'a': ['b', 'c'], 
    'b': ['a', 'd'],
    'c': ['a', 'd'], 
    'd': ['b', 'c', 'e'], 
    'e': ['d'], 
    'f': [] 
```

Now that we have a graph defined, we need a method to add_edge to that graph. It will be fed parameters of the start_vertex, the end_vertex, and a dictionary that represents the existing graph to which we would like to add an edge.

In the add_edge method, our first step will be to check if the edge we want to add already exists in the graph. If it does, we will print a message letting the user know that the edge already exists and return the original graph.

```
# Add this function to your code
def add_edge(start_vertex: str, end_vertex: str, graph: Dict[str, List[str]]) -> Dict[str, List[str]]:
    # Check if the edge is already in the graph
    if start_vertex in graph.keys() and end_vertex in graph[start_vertex] and end_vertex in graph.keys() and start_vertex in graph[end_vertex]: 
        print(f'Edge {start_vertex} -> {end_vertex} is already present') 
        # If so, just return the graph without adding a duplicate edge
        return graph 
```

Next, to continue building out the add_edge function, we check to see if there is already a list in the dictionary for the nodes indicated by start_vertex and end_vertex. If there is not, we create one using an empty list [ ].

Lastly, in the add_edge function, we add the edge by appending the start_vertex and end_vertex to the lists for those nodes, and return the graph.

```
def add_edge(start_vertex: str, end_vertex: str, graph: Dict[str, List[str]]) -> Dict[str, List[str]]:
    if start_vertex in graph.keys() and end_vertex in graph[start_vertex] and end_vertex in graph.keys() and start_vertex in graph[end_vertex]: 
        print(f'Edge {start_vertex} -> {end_vertex} is already present') 
        return graph 

    # Add the following logic to your code
    # If there is no list for given vertex, create it 
    if start_vertex not in graph.keys(): 
        graph[start_vertex] = [] 
    if end_vertex not in graph.keys(): 
        graph[end_vertex] = [] 

    # Add given edge 
    graph[start_vertex].append(end_vertex) 
    graph[end_vertex].append(start_vertex) 
 
    return graph 
```

If we want to see what the new graph looks like after we added a new edge, we can use a print_graph method that will use a nested for loop to print the vertices and edges.

The outer loop will cycle through the vertices, which are key values in our dictionary graph.

At each vertex, the nested inner loop will cycle through the list of adjacent vertices that can be reached from that key vertex.

Each edge will be listed as a pair of vertices, (vertex, item) starting with the key-value vertex and followed by the item in the values list of adjacent vertices. 

Using an if statement to test if the item already exists in the list, it will append each pair of adjacent vertexes to the list of edges. You will notice in the following code that we are attempting to add an edge that already exists in our graph—the edge from vertex A to vertex B. When we run the code, we should get a statement from the add_edge method that tells us the edge already exists.

To see the list of vertices or edges, use the print command with these variables. 

```
# Add this function to your code
def print_graph(graph: Dict[str, List[str]]) -> None: 
    vertices: List[str] = list(graph.keys()) 
    edges: List[Tuple[str, str]] = [] 
 
    for vertex in graph: 
        for item in graph[vertex]: 
            if (vertex, item) not in edges: 
                edges.append((vertex, item)) 
 
    print(f'Vertices: {vertices}') 
    print(f'Edges: {edges}') 
```

To print the new graph:

```
if __name__ == '__main__': 
    print('Original graph') 
    print_graph(graph)     
 
    print('---') 

    graph = add_edge('a', 'b', graph) 
    graph = add_edge('d', 'f', graph) 
    graph = add_edge('x', 'y', graph) 
 
    print('---') 

    # Add this code:
    print('Graph after adding new edges') 
    print_graph(graph) 
```

#### [Graph practice](./files/W04_5_Graph.py)

### Knowledge Check

#### Which data structure always has a root node?

* Trees

Wrong answers:

* Graphs
* Edges
* Vertices

Trees always have a root node, and the relationship between nodes is hierarchical.

Graphs do not have a root node. Nodes in a graph are called vertices. The links between the vertices are called edges. The relationship between vertices in a graph is not required to be hierarchical.

#### Which data structures have edges between the nodes or vertices?

* Graphs and trees

Wrong answers:

* Graphs
* Trees
* Tries and trees

Both graphs and trees have edges that connect the data points. In trees, those data points are called nodes. In graphs, the data points are called vertices.

#### Which data structure can have nodes or vertices that are not connected?

* Graphs

Wrong answers:

* Trees
* Tries
* Edges

Only graphs can have unconnected vertices. All nodes in trees are required to be connected to the tree.

#### Which data structure is used for storing only numerical data?

* Neither graphs nor trees

Wrong answers:

* Graphs ONLY
* Trees ONLY
* Both graphs and trees

Trees and graphs store a wide variety of data, including strings, arrays, Booleans, lists, dictionaries, and numbers.

#### Which data structure is allowed to have paths that loop or cycle?

* Graphs

Wrong answers:

* Trees
* Both graphs and trees
* Neither graphs nor trees

Only graphs can have cyclical paths.

Because the information stored in trees is hierarchical, there are no loops or cycles allowed.

### Summary

#### Connected or disconnected graphs

Graphs are constructed of **vertices** (nodes or data points) and **edges** that connect the data points to each other. Unlike trees, **disconnected graphs** can have vertices that are not connected to any other vertices.

#### Directed or undirected edges

The edges can be **directed**, showing the path of travel from one vertex to another, or **undirected**, showing travel in both directions. If the edges are directed, they are called **arcs**.

#### Sink vertex and source vertex

A vertex that only has incoming edges (pointing toward the vertex) is called a **sink**. A vertex that only has outgoing edges (pointing away from the vertex) is called a **source**.

#### Paths and loops or cycles

Paths are a series of vertices and edges that can travel from one vertex to another. Graphs with directed edges can have loops or cycles that visit a vertex more than once in a path. 

#### Weighted edges

Edges of graphs can have weights that tell the time, cost, distance, or other measure of traveling from one vertex to another. Using weighted graphs, edges can even be negative. For example, some travel between vertices such as in financial transactions or chemical reactions can reduce money or energy.

#### Common applications of graphs

Graphs are commonly used in network operations, such as connecting telecommunication lines, keeping track of social network connections, or using airline route maps. Graphs have many common uses when data points have relational values to other data points.

## Graphing Algorithms

### Pre-assessment

#### Which graph traversal algorithm is used with negative weights to find the shortest path from one vertex to another?

* Bellman-Ford

Wrong answers:

* Dijkstra
* Algorithms cannot show a negative weight on a graph
* Both Bellman-Ford and Dijkstra

Negative weights can be used in graphs for certain instances such as chemical reactions or financial transactions where moving from one node or vertex to another can reduce the cost, distance, money, or other weight on the edge.  

For negative weights, the Bellman-Ford algorithm is the only one that will yield correct shortest path between two vertices.

#### How does the Dijkstra shortest path algorithm work?  

* By finding the shortest sub path to all nodes visited along the path

Wrong answers:

* By eliminating all the highest weight edges first, no matter which vertices they are connected to
* By visiting each node multiple times and iterating to find the shortest path
* By approximating the shortest path

The Dijkstra algorithm guarantees to find the shortest path between two nodes. It does this by visiting each node one time and finding the shortest path from that node to the starting node, successively building a subpath graph containing the shortest paths from the starting node to each node in the tree.

#### Which statements are TRUE of minimum spanning trees? (Select TWO.) 

* They are undirected graphs with no cycles.
* They include all vertices in the graph.

Wrong answers:

* They are directed graphs with weighted edges.
* If the graph is unweighted, there is only one possible minimum spanning tree for any graph.
* The number of vertices is the same as the number of edges.

A minimum spanning tree is an undirected graph without cycles.

Minimum spanning trees must have weighted edges and the sum of the weights must be the least possible while still maintaining all vertices and (v-1) edges with no cycles.

A minimum spanning tree has one less edge than the number of vertices in the graph.

#### How many possible routes can a traveling salesperson take if they wanted to visit four cities and return home to their starting point?

* 24

Wrong answers:

* 4
* 8
* 16

With four choices, the first time they would have four possible choices. After choosing one, there would be three left, so they would have three choices, then two choices, and then one choice. This can be represented as 4! = 4*3*2*1 = 24.

#### Which algorithm will always produce an optimal solution when applied to the traveling salesman problem?

* Brute force

Wrong answers:

* Branch and bound
* Nearest neighbor
* Markov chain

The brute force method tries every possibility of paths between the starting point and all additional vertices. Only this method will consider all permutations of tour paths and thus produce accurate results.

However, because it must consider so many solutions, the time and processing resources to calculate it are prohibitive for large datasets.  

Many other solutions have been proposed, but they are only approximations, and while they might produce better-than-average results for the shortest path, they cannot guarantee the shortest path.

### Shortest Distance: Dijkstra Algorithm

An algorithm is a process or set of rules to be followed in calculations or problem-solving operations. The goal of any algorithm is to give the user a set of steps to help them accomplish the task.

In graph data structure, we use algorithms to help find the following:

* Path between two nodes
* Shortest, least costly, or lowest weight path between two nodes
* Cyclical paths in a graph
* One path that reaches all nodes

### Dijkstra algorithm

The Dijkstra algorithm is the fastest algorithm with lowest time complexity. However, it is important to remember that it does not work correctly with negative edge weights. Negative weights can occur in chemical reactions and in financial transactions where there is a cost, loss, penalty, or fee. Because of the type of checking it does, the Dijkstra algorithm would yield an incorrect path weight in graphs with negative edge weights.

The Dijkstra algorithm works to find the shortest path from a starting node by finding the shortest subpaths between each node visited along the path.

For example, in the graph that follows, the shortest path from B to F will include the shortest path from B to E. The shortest path from B to E will include the shortest path from A to E.

The Dijkstra algorithm visits each node one time to find the shortest path from it to all adjoining nodes, each time updating the total length from the starting node to all other nodes reachable from each node.

#### Steps of the algorithm

1. Choose the starting node. This is the node we will use to find the shortest path to all other nodes.
2. Create a list_of_nodes to visit, which consists of every node in your graph. As you visit each node, you cross it off or remove it from the list.
3. Create a shortest_path dictionary with key:values of node_name:shortest_distance.
4. Initialize your values with the longest possible path = infinity. Each time you visit a node and find a shorter path, you will update the dictionary value with the length of the shortest path you have found so far from the starting node to each key value in the dictionary.
5. For each node in your list_of_nodes, find the weight of the shortest path between your starting node and any adjacent nodes, and update the dictionary value of shortest_distance. Then, remove the current node from the list_of_nodes and repeat this step for the new current node.
6. When you have visited each node once and updated the shortest_distance from the starting node, the values in your dictionary will contain the shortest_distance from the starting node to each node in the graph.

### Dijkstra algorithm in Python code

We start by defining a class called **Graph** and initializing the nodes that are defined using a dictionary.

Next, we define a method **add_edge that** takes the following three parameters:

* The starting node of the edge, **from_node**
* The ending node of the edge, **to_node**
* The **weight**, which is the distance or cost associated with the edge

The **add_edge** method uses an **if** statement to determine if the starting node (**from_node**) is already in the dictionary of nodes. The following are the results of the if statement.

* If it is not already in the dictionary, it returns an empty set.
* If it is in the dictionary, it appends the node to the ending node and the weight of the edge to the starting node within the dictionary.

```
from typing import Dict, List, Tuple

class Graph:
    def __init__(self): 
        self.nodes: Dict[str, List[Tuple[str, int]]] = {}

    def add_edge(self, from_node: str, to_node: str, weight: int) -> None: 
        if from_node not in self.nodes: 
            self.nodes[from_node] = [] 
        self.nodes[from_node].append((to_node, weight)) 
```

Next, we define a **dijkstra** method to find the shortest path from the starting node to all other nodes. It will return a dictionary that stores the path traveled. This method uses **priority_queue**, which stores a list of nodes to test with weight listed first and followed by the name of the node. It also uses a dictionary of **distances** between each node and the next. These variables are initialized with information from the **start_node**.

```
def dijkstra(self, start_node: str) -> Dict[str, Tuple[int, List[str]]]:
       
        distances: Dict[str, Tuple[int, List[str]]] = {node: (float('inf'), []) for node in self.nodes} 
        distances[start_node] = (0, []) 
 
        priority_queue = [(0, start_node)]
```

We continue the **dijkstra** method with a **while** loop that continues iterating while there are still objects in the **priority_queue**. It starts by sorting the tuples in the **priority_queue** by ascending weight of the edges. Then, it uses **pop(0)** to remove the first item in the **priority_queue** and assigns its values to **current_distance** and **current_node**.

If the distance of the first item in the **priority_queue** is greater than the distance to the **current_node**, we use the **continue** statement to skip the remaining portion of the **if** statement. Otherwise, we append the node and update the distance by adding the **current_distance** to the previous weight. And then, we append a new neighbor tuple to our priority queue before returning to the top to continue the **while** loop.

When the **priority_queue** is empty, we drop out of the **while** loop and return the dictionary of distances.

```
while priority_queue:
            priority_queue.sort() 
            current_distance, current_node = priority_queue.pop(0) 
 
            if current_distance > distances[current_node][0]: 
                continue 
 
            for neighbor, weight in self.nodes[current_node]: 
                distance = current_distance + weight 
 
                if distance < distances[neighbor][0]: 
                    distances[neighbor] = (distance, distances[current_node][1] + [current_node]) 
                    priority_queue.append((distance, neighbor)) 
 
        return distances 
```

Now that you have seen how to create the code for the Dijkstra algorithm, look at the following examples of how you might use it.

```
# Example of usage 
g = Graph()
 
# Add edges 
g.add_edge('A', 'B', 1) 
g.add_edge('A', 'C', 4) 
g.add_edge('B', 'C', 2) 
g.add_edge('B', 'D', 5) 
g.add_edge('C', 'D', 1) 
g.add_edge('D', 'A', 7) 
 
# Run the Dijkstra algorithm 
start_node = 'A' 
shortest_paths = g.dijkstra(start_node) 
     
print("Shortest paths from", start_node, ":") 
for node, (distance, path) in shortest_paths.items(): 
    print(f"To {node}: Distance = {distance}, Path = {' -> '.join(path + [node])}"
```

### Shortest Distance: Bellman-Ford Algorithm

The Bellman-Ford algorithm guarantees to find the shortest path in a graph, as does the Dijkstra algorithm. However, the Bellman-Ford algorithm has the advantage that it can handle negative values for edge weights, which Dijkstra cannot. Negative edge weights can occur in a variety of real-life applications. For example, the negative weight of the edge could be related to the following:

* Series of financial transactions where positive values add to your balance and negative values reduce your balance
* Chemical reaction where weights are used to represent the heat produced during a chemical reaction
* Any other relationship between data points that could be positive or negative in value

This algorithm will be iterated v-1 times, where v is the number of vertices or nodes in the graph. This is not an arbitrary number of iterations, but it represents the most possible nodes that could be visited without repeating any nodes and creating a cycle. With negative edge lengths, creating a cycle could artificially reduce the distance between two points if a negative cycle were revisited numerous times. This is why this algorithm only iterates v-1 times because this prevents traversing the same edge twice in a path.

### Steps of the algorithm

1. Choose a starting vertex. This is the one from which you are seeking the shortest path to any other vertex in the graph. Let’s call our starting vertex S.
2. Create a dictionary of key:value. Key is the name of each node or vertex in your graph. Value is the shortest distance from the starting vertex to each key vertex.
3. Initialize the values in the dictionary. The value of the starting vertex is zero (0) because there is no distance from the starting node to itself. The value of all other nodes is infinity. As we iterate, these values will be replaced each time we find a path to the vertex that is shorter than the current value saved in the dictionary.
4. Begin the first iteration. Find outgoing vertices adjacent to the starting vertex. Update their distance value in the dictionary if the new distance is less than the one currently stored in the dictionary. Visit each additional vertex in the dictionary one at a time, looking for outgoing edges leading to additional vertices. Calculate the distance to each of these new vertices by adding the distance of the current vertex to the weight of the edge leading to the new vertices. Update the distance values in the dictionary for each new vertex if it is smaller than the value currently stored for that vertex’s distance from the starting node. For each iteration, you will visit each vertex once.
5. Iterate, or repeat, Step 4 v-1 times. V is the number of vertices in your graph. If you find a smaller distance value, update the dictionary distance value for the vertex. If you find that any complete iteration, or visit to all vertices, does not change any distance values stored in the dictionary for any vertex, you know you have completed the process of finding shortest distances and can drop out of the loop early.

### Bellman-Ford algorithm in Python code

Let’s examine one implementation of the Bellman-Ford algorithm in Python. We start as we did with the Dijkstra algorithm by defining a **Graph** class. We initialize it with the **__init__** method. This sets up a graph with an integer number of **vertices** and creates a variable **self.graph** that is a list of integer-based tuples. Each tuple will contain three integers. The first two integers are the source and destination vertices, and the third integer is the weight of the edge connecting those two vertices. In our **__init__** method, we initialize the **self.graph** with an empty list. This list will be added to each time we add an edge to our graph.

```
from typing import List, Tuple

class Graph: 
    def __init__(self, vertices: int) -> None: 
        self.vertices = vertices 
        self.graph: List[Tuple[int, int, int]] = [] 
```

The next method in our **Graph** class is **add_edge**. This method receives the following three integer variables:

* **u** – Name of the source vertex
* **v** – Name of the destination vertex
* **w** – Integer weight of the edge connecting vertex u and vertex v.

The only operation in this method is to **append** a tuple containing the three variables onto the list of tuples in the graph. Remember that each tuple in **self.graph** represents the edge between two vertices and contains the source, destination, and weight.

```
    def add_edge(self, u: int, v: int, w: int) -> None: 
         self.graph.append((u, v, w)) 
```

#### Initialize the bellman_ford method

Next, we define the **bellman_ford** method, which applies the Bellman-Ford algorithm to find the shortest paths from the **source** vertex to every other vertex in the graph. The parameter fed to this method is the starting vertex, **source**. When we finish the method, our resulting graph will contain a list of the shortest distances from our starting vertex, **source**, to every other vertex in the graph.

We initialize the method by setting up a list of **distances**. Then, we insert the numeric value of infinity (using the **float('inf')** command) into the distance list once for each of the **vertices** contained in our graph. If we have six vertices, we will end up with a list containing six values of infinity. Remember that **vertices** is an integer variable that is fed in to the **Graph** class when we create an instance of the graph.

```
    def bellman_ford(self, source: int) -> None: 
        distances = [float('inf')] * self.vertices 
        distances[source] = 0 
```

#### Iterate through the bellman_ford method

Now that we have initialized our **bellman_ford** method, the next step is to iterate through each vertex (**n-1**) times, or one less time than the number of vertices in our graph. This is not an arbitrary number of times. It prevents cycles.

Our nested **for** loops accomplish the task. The outer **for** loop iterates one less time than the number of vertices. The inner **for** loop compares the distances currently stored in the graph from our source vertex to the destination vertex (**v**). If the current edge weight (**w**) added to the shortest distance stored to get to vertex **u** is shorter than the currently known shortest distance to vertex **v**, then it updates the shortest distance stored in the list for that vertex.

The second **for** loop is not implemented until the updated values are in the **distances** list. This second **for** loop tests each possible edge weight to see if adding it would reduce the new lowest weight. By this time, the distances list contains the lowest possible path weight; therefore, if the value of any edge is negative, it will decrease the traversal path weight. If so, this **for** loop will alert you that you have negative edge weights by printing a notice: "Graph contains negative weight cycle."

The third **for** loop will cycle through the range of vertices and print each vertex and the shortest distance from that vertex to the starting vertex.

```
        for _ in range(self.vertices - 1): 
            for u, v, w in self.graph: 
                if distances[u] != float('inf') and distances[u] + w < distances[v]: 
                    distances[v] = distances[u] + w 
 
        for u, v, w in self.graph: 
            if distances[u] != float('inf') and distances[u] + w < distances[v]: 
                print("Graph contains negative weight cycle") 
                return 
 
        print("Shortest distances from source vertex:") 
        for i in range(self.vertices): 
            print(f"Vertex {i} -> Distance: {distances[i]}") 
```

#### Define methods to print the graph

The last methods we define for our **Graph** class are **dump** and **dump_graphviz**, which print or visualize the graph.

The method **dump** will print a list of vertices and weights contained in the final shortest distances spanning graph.

```
    def dump(self) -> None: 
        for u, v, w in self.graph: 
            print(f"{u} --({w})--> {v}") 
```

The **dump_graphviz** method will output the list of shortest distances from the source vertex to each vertex in the graph.

```
    def dump_graphviz(self, filename: str = 'graphviz_output.dot') -> None:
        with open(filename, 'w') as f: 
            f.write('digraph G {\n') 
            for u, v, w in self.graph: 
                f.write(f'  {u} -> {v} [label="{w}"];\n') 
            f.write('}\n') 
```

#### Call the methods from the main program

The last code we will explore is the code used in the main program to create an instance of the graph. We will create a graph, called g, with five vertices. These vertices will be labeled vertices 0, 1, 2, 3, and 4.

We will add six edges using the method **add_edge** and list the starting node, ending node, and edge weight.

Then, we will run the **bellman_ford** method and **dump** the results.

```
if __name__ == '__main__': 
    # Example usage: 
    g = Graph(5) 
 
    # Add edges 
    g.add_edge(0, 1, 2) 
    g.add_edge(0, 2, 4) 
    g.add_edge(1, 3, 2) 
    g.add_edge(2, 4, 3) 
    g.add_edge(2, 3, 4) 
    g.add_edge(4, 3, -5) 
 
    # Visualize the graph 
    g.dump() 
    g.dump_graphviz() 
 
    # Run the Bellman-Ford algorithm 
    source_vertex = 0 
    g.bellman_ford(source_vertex) 
```

####  [Bellman-Ford algorithm practice](./files/W04_6_Bellman-Ford_algorithn.py)

## Minimum Spanning Tree Algorithms

Minimum spanning trees are used in planning telecommunications networking, copper plumbing lines, sewer and utility services, and many other practical applications where you want to reduce expenses while maintaining connectedness to all points.

A minimum spanning tree is a type of graph used to plan the minimum weight of all edges while still maintaining connectedness of the graph.

### Directed and Undirected

* **Directed graphs** have one-way arrows that point the direction of travel on the path.
* **Undirected graphs** can be traveled in both directions on the same edge.

### Connected and disconnected

* A **connected graph** has a path from any one vertex to any other vertex in the graph.
* A **disconnected graph** has one or more vertices that are not reachable from some other vertices in the graph.

### Spanning trees

The following details describe a spanning tree:

* Is a subgraph of an undirected connected graph
* Includes all the vertices of the graph
* Has one less edge than the number of vertices in the graph
* Has weighted or unweighted edges
* Has no cycles

Any graph can have multiple spanning trees that meet the criteria.

### Minimum spanning trees

The following details describe a minimum spanning tree:

* Must be a spanning tree – a connected and undirected graph with no cycles, whose number of edges is (n-1)
* Must have weighted edges
* Must have the least sum of edge weights possible to meet the other criteria

### Prim's algorithm to find the minimum spanning tree fpr a graph

Because it is considered a greedy algorithm, Prim’s algorithm finds the local optimum solution in hopes of finding the global optimum solution. A greedy algorithm always looks for the locally optimal best solution at each step.

It takes as input a weighted, connected, and undirected graph and finds a subset of that graph that is the minimum spanning tree.

#### Prim's algorithm steps

1. Initialize the spanning tree by choosing any random vertex as the current_tree. 
2. Find all edges from the current_tree that would connect the tree to new vertices not already connected to the current_tree. 
3. Of those edges, choose the one with minimum weight and add it (and its connected vertex) to the current_tree.
4. If not all vertices are connected to current_tree, repeat beginning with Step 2.

### Minimum spanning tree compared to shortest distance

Although the shortest paths between two points are not guaranteed with a minimum spanning tree, the minimum spanning tree does provide the overall lowest total weight possible for the graph while still maintaining connectedness to all vertices.

### Prim’s algorithm in Python code

Let’s start by defining a class called **Graph**. We will give it as parameters the number of vertices in the graph. We define the following two variables:

* **self.vertices** – Number of vertices
* **self.adjacency_list** – List of adjacent edges

Then, we define a method called **add_edge**, which is given the following three parameters:

* **u** – Name of the source vertex
* **v** – Destination vertex
* **weight** – Weight of the edge

The **add_edge** method will create two lists of adjacent edges, one list for the source vertex **u** and one list for the destination vertex **v**. These lists will consist of tuples, where each tuple has the name of the adjacent vertex and the weight of the edge connecting to that vertex.

When this method is called, it will add the edge by creating a tuple containing the name of the adjacent vertex and the weight to that vertex. This newly created tuple will be appended to the existing **adjacency_list** for each of the added two vertices on the edge.

```
from typing import List, Tuple

class Graph: 
    def __init__(self, vertices: int) -> None: 

        self.vertices = vertices 
        self.adjacency_list = [[] for _ in range(vertices)] 
  
    def add_edge(self, u: int, v: int, weight: int) -> None: 
       
        self.adjacency_list[u].append((v, weight)) 
        self.adjacency_list[v].append((u, weight)) 
```

Next, we define a method, called **prim_mst**, which will find the minimum spanning tree using Prim’s algorithm. It will return a list of tuples, where each tuple has three objects: **u**, **v**, and **weight**.

We initialize this method with a list, **priority_queue**, containing one empty tuple. This tuple contains zeroes to represent the number of the vertex and the weight of the edge to that vertex. It represents the starting vertex because the distance or weight from itself to itself is zero.

We also initialize a variable, **visited**, using the **set()** constructor. This will create an empty list because we have not visited any vertices yet. As we visit vertices, we will add the name of the vertex to this visited list.

Lastly, we define the variable **mst_edges** as an empty list.

```
def prim_mst(self) -> List[Tuple[int, int, int]]: 

        priority_queue = [(0, 0)]  # (weight, vertex) 
        visited = set() 
        mst_edges = [] 
```

Now that we have initialized the method and defined our variables, let’s start working through creating the minimum spanning tree.

We do this with a **while** loop that iterates through the list of tuples in the **priority_queue**.

It starts by sorting the list of tuples by weight, using the built-in list method **sort()** that sorts them into ascending order with the lowest value first. Because our tuples are given as (**weight**, **vertex**), this **sort()** method will return a list of tuples with the lowest weight listed first. The first time this iterates, the **priority_queue** will only contain the starting vertex.

Now that our **priority_queue** list has been sorted, we use **pop(0)** to remove the first object in the list and assign the values contained in that tuple to our variables weight and **current_vertex**.

```
   while priority_queue:
            priority_queue.sort()  # Sort the priority queue by weight 
            weight, current_vertex = priority_queue.pop(0)
```

If the **current_vertex** is not in the list of visited vertices, we add it to the list. Notice that the first time through, this will add the starting vertex to the list.

```
           if current_vertex not in visited:
                visited.add(current_vertex)
```

Using a **for** loop, we iterate through each of the neighbors in the **adjacency_list** of the **current_vertex**, and if the neighbor is not already in the list of vertices we have visited, then we **append** that neighbor to the **priority_queue** list of tuples checked in the **while** loop and **append** a tuple containing the edge (with the **current_vertex**, **neighbor** and **edge_weight**) to our list of **mst_edges**.

When the **priority_queue** is empty, the method exits the while loop and returns **mst_edges**, which is a list of tuples containing the edges in the minimum spanning tree.

```
       if current_vertex not in visited: 
          visited.add(current_vertex) 
 
          for neighbor, edge_weight in self.adjacency_list[current_vertex]: 
               if neighbor not in visited: 
                  priority_queue.append((edge_weight, neighbor)) 
                  mst_edges.append((current_vertex, neighbor, edge_weight)) 
 
    return mst_edges
```

In the following example, we create an instance of the class **Graph** and create a graph with five vertices. Then, we add edges using the **add_edge** method and pass the starting vertex, ending vertex, and weight of the edge for each edge we add. Lastly, we call the **prim_mst** method for the graph we have created and then print out the resulting edges for the minimum spanning tree it produces.

```
# Example usage: 
if __name__ == "__main__": 
    # Example of usage 
    g = Graph(5) 
 
    # Add edges 
    g.add_edge(0, 1, 2) 
    g.add_edge(0, 2, 4) 
    g.add_edge(1, 2, 1) 
    g.add_edge(1, 3, 5) 
    g.add_edge(2, 3, 8) 
    g.add_edge(2, 4, 3) 
    g.add_edge(3, 4, 7) 

    # Print adjacency list for each vertex 
    for i in range(g.vertices):
        print(f"Vertex {i}: {g.adjacency_list[i]}")
 
    # Find the Minimum Spanning Tree (MST) using Prim's algorithm 
    mst_edges = g.prim_mst() 
    print("Minimum Spanning Tree (MST) Edges:") 
    for edge in mst_edges: 
        print(edge) 
```

### Expected output

```
Vertex 0: [(1, 2), (2, 4)]
Vertex 1: [(0, 2), (2, 1), (3, 5)]
Vertex 2: [(0, 4), (1, 1), (3, 8), (4, 3)]
Vertex 3: [(1, 5), (2, 8), (4, 7)]
Vertex 4: [(2, 3), (3, 7)]
Minimum Spanning Tree (MST) Edges:
(0, 1, 2)
(0, 2, 4)
(1, 2, 1)
(1, 3, 5)
(2, 3, 8)
(2, 4, 3)
(4, 3, 7)
(2, 3, 8)
```

#### P[rim's algorithm practice](./files/W04_7_MinimalSpanningTree_PrimAlgorthm.py)

### Kruskal’s algorithm for Minimum Spanning Tree

Kruskal's algorithm differs slightly from Prim’s algorithm, but it still can produce a minimum spanning tree.

The following are the steps of Kruskal's algorithm.

1. Sort all the edges in ascending order by weight.
2. Pick the smallest edge. Check if it forms a cycle with the spanning tree so far. If a cycle is not formed, include this edge. If a cycle is formed, discard the edge.
3. Repeat Step 2 until there are (v-1) edges in the tree.

## Traveling Salesperson Algorithms

### Evaluating number of edges in a graph

* First node requires zero edges.
* Second node adds one additional edge.
* Third node adds two additional edges.
* Fourth node adds three additional edges.
* Fifth node adds four additional edges.
* Sixth node adds five additional edges.
* The nth node adds (n-1) additional edges.

Hence, the number of edges connecting all nodes to every other node in a graph with n nodes is (n-1) + (n-2) + (n-3) + ….... + (n-n).

### Brute-force method

The brute-force method ensures that we will calculate the correct answer because it calculates the distances from each city to every other city. Then, it builds all the possible paths from the home city to visit every other city. It works well with small datasets, but it's very time consuming to run when the number of vertices increases.

The following are the steps for the brute-force method.

1. Determine all possible routes from one city to every other city. Calculate the distance or cost for each pair of cities. These can be stored in an adjacency matrix.
2. Determine all possible permutations of routes, or tours, from the home city to every other city and return back to the home city.
3. For each of these possible tours, add up the distance between each city to arrive at the total distance if you took that route.
4. Compare the total distances found for each route in Step 3 and choose the shortest route.

### The brute-force method for eight cities

#### Calculate distances between all cities (edges)

The first step is to determine all possible pairs of cities and calculate the distance between each pair. Including the home base, we have nine total cities that need to have the distances between them calculated. That means there will be 8 + 7 + 6 + 5 + 4 + 3 + 2 + 1 + 0 = 36 unique paths, where each path represents an edge between two different cities in the graph. Each of these distances must be calculated and stored in an adjacency matrix like this one.

If the cost to travel in one direction is different than the cost to travel in the other direction, then the second half of the matrix would contain 36 additional data points.

#### Determine all possible tour paths to all cities

Because we know he will start and end in the home city, let’s start by calculating the number of permutations of routes he could have to visit the remaining eight cities.

This could be represented by 8! = 8 * 7 * 6 * 5 * 4 * 3 * 2 * 1 = 40,320 different routes.

Each of these 40,320 tours would need to have their total distance calculated and compared against the shortest route already calculated. 

#### Calculate total distance for each tour

Each of these 40,320 possible tours will now need to have their total distance calculated, using the distance we stored in the adjacency matrix for the 36 unique paths between the cities.

To that total, we will add the distance from the home city to the first city visited and the distance from the last city visited back to the home city.

As we total the distance for each possible route, we will compare that total distance to the shortest path we have already found.

If the new route is shorter than the shortest path, we will replace the value currently stored in the shortest path with the current path.

### Advantages of the brute-force method

The advantages of the brute-force method of exhaustive sequential search are as follows: 

* **Accuracy:** It always works to produce the shortest route because it checks all possibilities and leaves no room for overlooking potential solutions.
* **Adaptability:** It can be applied to a wide variety of problems, from simple tasks to complex computations.
* **No ambiguity:** It is a simple, straightforward approach.  

### Disadvantages of the brute-force method

The disadvantages of the brute-force method of exhaustive sequential search are as follows:

* **Inefficiency:** It can be highly inefficient, especially with large datasets.
* **Lengthy:** It can take a long time to process the data.

### Python code for brute-force algorithm

Establish a **TravelingSalesman** class and initialize it with the **num_cities** visited and an adjacency matrix representing the distances between cities.

```
from typing import List, Tuple

class TravelingSalesman: 
   
    def __init__(self, num_cities: int, graph: List[List[int]]) -> None: 
      
        self.num_cities = num_cities 
        self.graph = graph 
```

Define a **solve_tsp** method that uses a submethod, **generate_permutations**, which will call itself recursively to cycle through the list of cities visited and create all possible permutations that represent the order of visitation of those cities.

```
def solve_tsp(self) -> Tuple[List[int], int]: 
       
        def generate_permutations(arr): 
            if not arr: 
                return [[]] 
 
            permutations = [] 
            for i in range(len(arr)): 
                remaining = arr[:i] + arr[i + 1:] 
                for p in generate_permutations(remaining): 
                    permutations.append([arr[i]] + p) 
 
            return permutations 
 
        # Generate all possible permutations of cities 
        city_permutations = generate_permutations(list(range(self.num_cities))) 
```

Continue the **solve_tsp** method by initializing variables. Use **optimal_tour** to store the order in which the cities are visited. Use **min_distance** to store the minimum distance to take the tour.

Then, use a nested **for** loop to iterate through the possible **permutations** of your tour, calculating the distance traveled for each tour by adding the distances between each city on the tour. If the distance traveled in the current tour is less than the **min_distance** variable, update the minimum distance variable to reflect the smaller distance, and update the **optimal_tour** to contain the current permutation of your tour.

When you drop out of the loop, it will return the **optimal_tour** and the min_distance.

```
# Initialize variables to store the optimal tour and total distance
        optimal_tour = None 
        min_distance = float('inf')

# Iterate through all permutations and calculate the total distance 
        for permutation in city_permutations: 
            distance = 0 
            for i in range(self.num_cities - 1): 
                distance += self.graph[permutation[i]][permutation[i + 1]] 
            distance += self.graph[permutation[-1]][permutation[0]]  # Return to the starting city 

# Update optimal tour if current permutation is shorter distance 
            if distance < min_distance: 
                min_distance = distance 
                optimal_tour = permutation 
 
        return optimal_tour, min_distance 
```

The following shows example data you might feed into this code and some ways to call the data in your code.

```
# Example of usage 
    num_cities = 4 
    distance_graph = [ 
        [0, 10, 15, 20], 
        [10, 0, 35, 25], 
        [15, 35, 0, 30], 
        [20, 25, 30, 0] 
    ] 
 
    tsp = TravelingSalesman(num_cities, distance_graph)
# Solve and print the optimal tour and total distance 
    optimal_tour, total_distance = tsp.solve_tsp() 
    print("Optimal tour:", optimal_tour) 
    print("Total distance:", total_distance) 
```

#### [Brute-force algorithm practice](./files/W04_8_BruteForceAlgorithm.py)

### Nearest neighbor algorithm

Although the brute-force method always produces an optimized path, in most cases, programmers need a quicker method to find a path that, although not optimized, is generally good enough. The nearest neighbor method is one of many such algorithms. The following are the steps for the nearest neighbor algorithm.

1. **Initialize variables:** You will need a variable representing the sequence of nodes visited on the tour path. You will also need a variable representing the weight of the path between those nodes. Initialize both of these to zero, or empty, sets.
2. **Choose start node:** Begin at a randomly selected starting point. Or, if you have a home base that this tour must start at, such as the traveling salesperson, begin at a home base node. Add this starting node to the sequence.
3. **Add nearest neighbor:** Find the closest unvisited node. This is the node with the lowest path weight adjacent to the current node. Add it to the sequence.
4. **Update path weight:** Add the path weight from current node to nearest neighbor.
5. **Repeat until all nodes are visited:** Move to the neighbor just added to the sequence. If there are still unvisited nodes, loop back to Step 3 and repeat until all nodes have been visited and added to the sequence.
6. **Add final distance to home node:** When all nodes have been visited, return to the start node. Add it to the sequence. Also add the path weight from the most recently visited node to the start node to the total weight.

#### Advantages of nearest neighbor

* **Simplicity:** This algorithm is simple and easy to use. 
* **Speed:** The algorithm provides a quick and reasonable solution as a starting point to feed to a more sophisticated algorithm.

#### Disadvantages of nearest neighbor

* **Not guaranteed:** This algorithm rarely finds the optimal solution. 
* **Inaccurate:** The solution found with this algorithm can be significantly larger than the optimal route.

### Other algorithms to consider

The traveling salesperson problem has intrigued mathematicians and network engineers for decades. We have introduced the brute-force algorithm and the nearest neighbor algorithm to solve this problem. They are not the only ones available. The following is a short list of possible algorithms for you to consider researching, especially if you want to find a better solution than those already suggested. There are also many others not listed that are being explored and proposed.

* **Branch and bound:** This algorithm takes an initial route from the starting city to the first node and systematically compares different permutations to extend the route one node at a time. As it finds a route that is not optimal, it prunes that branch of the exploration. 
* **Pairwise exchange:** This algorithm removes two edges and replaces them with two different edges that reconnect the fragments into a shorter tour.
* **3-opt:** This algorithm removes three edges and reconnects them to form a shorter tour. 
* **Markov chain:** This algorithm uses local searching sub-algorithms to find a route extremely close to optimal.
* **Ant colony optimization:** This algorithm simulates an ant colony behavior of real ants to find short paths between food sources and their nest using trail pheromones deposited by other ants. This algorithm sends out virtual ant agents to explore possible routes on the map and deposit pheromone on each edge they cross until they complete the tour.

### Knowledge Check

#### Which options describe both the Bellman-Ford and the Dijkstra algorithm? (Select TWO.)

* Both create a dictionary used to hold the values.
* Both allow you to choose the starting vertex at random.

Wrong answers:

* After choosing a starting vertex, the next step on both of them is to visit the closest node first.
* Both are iterated (v-1) times where v is the number of vertices in the graph.
* Both algorithms will find the minimum spanning tree of a graph.

Both algorithms allow you to choose the starting vertex at random and also store their values in a dictionary.

The Dijkstra algorithm has you visit the next closest vertex first.

The Bellman-Ford algorithm iterates (v-1) times.

These algorithms help you find the shortest path from your starting node to any other node in the tree. This is not the same as minimum spanning tree.

#### Which options are true when comparing the Dijkstra and the Bellman-Ford algorithms? (Select TWO.)

* The Bellman-Ford produces the most accurate results with negative weights because it checks for cycles.
* The Dijkstra algorithm produces the fastest result because it only iterates on each node once.

Wrong answers:

* The Dijkstra is the only one that guarantees the shortest path. The Bellman-Ford comes close but is better for large datasets because it takes less time.
* The Bellman-Ford is fastest because the order in which the nodes are visited is pre-decided in the dictionary, so the algorithm does not need to process which node to visit next.
* The minimum spanning tree is faster to find with the Dijkstra algorithm.

The Dijkstra algorithm produces the fastest result because it only iterates on each node once.

The Bellman-Ford produces the most accurate results with negative weights because it checks for cycles.

Both algorithms guarantee the shortest path.

Neither algorithm calculates the mininmum spanning tree.

### Summary

#### Shortest distance

We explored two algorithms that are used to calculate the shortest distance between points on a graph—Bellman-Ford and Dijkstras. Both algorithms create a spanning tree that keeps only the edges representing the minimum weight or shortest distance between two points. Both algorithms produce accurate results, but they have different methods of finding the result.

* Dijkstra’s algorithm is generally faster because it only visits each node or vertex once. However, it cannot work with negative edge weights because it can produce inaccurate results by creating a cycle.
* Bellman-Ford algorithm will work with negative edge weights, although it is often more time consuming to implement because it visits each vertex (v-1) times to iterate for the shortest distance.

#### Minimum spanning tree

Graphs are also used to find the minimum spanning tree. This is a connected graph that includes all vertices and (v-1) edges. It has the lowest total edge weight possible while still meeting the other requirements.

Minimum spanning trees can be used to plan for utility, sewer, and other connections where it is important that all vertices are connected to the graph at the least possible cost.

The two algorithms we reviewed to find a minimum spanning tree are Kruskal's and Prim's. Both have different steps to find the minimum spanning tree, but they both yield accurate results.

#### Traveling salesperson problem

The last application of graphs we considered in this module was the traveling salesperson problem. The goal is to connect all vertices by a continuous loop that starts and ends at the same vertex and has the least weight or distance possible for the tour. Common uses for this graphing solution include mapping DNA, routing delivery trucks or school buses, designing microchips, scheduling robotic machining, and logistics of moving heavy equipment and personnel between job sites.

We examined the exponential nature of the number of possible tour paths as the number of vertices increased. We also examined two algorithms that have been proposed and discussed the ongoing interest among mathematicians to solve this problem in a simple way. The two algorithms we considered were the brute-force method and the nearest neighbor method. 

* The brute-force method will consider every possible permutation of the path and will give an accurate result every time. However, because of its exhaustive approach, it is very time consuming and so other algorithms attempt to create a result that is better than a random guess that is good enough to use without the time and computer resources required for the brute-force method.
* The nearest neighbor method seeks to find the shortest path from any node in the existing tree to any unvisited vertex in the tree. Although it generally produces better results than random guessing, it produces different results depending on which vertex is the starting vertex. It can often produce results that are significantly longer distances than the actual shortest path.

### [Lab: Finding the Shortest Path With Directed and Undirected Graphs](./W04Lab1.md)
