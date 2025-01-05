#!/usr/bin/env python
# coding: utf-8

# # <span style="color:blue">Recursion
# AWS CLOUD INSTITUTE: PROVIDED FOR EDUCATIONAL INSTRUCTIONAL PURPOSES ONLY.

# **Recursion** is a concept in computer science where a **function calls itself**. A recursive function generally has **two parts**, a recursive portion and a base case:
# - The **recursive portion** is the **part of the **code** that **repeats each time**, and **calls itself**
# - The **base case** is the **part of the code** that **checks for** a **condition to end** the **recursion**
# 
# We will look at several examples of recursion.

# # Example: Calculating Factorial
# **Factorial** is **one of the most common examples** of a **recursive solution**, though as we'll see, it's not one without issues.

# In[ ]:


def factorial(n):
    '''
    Recursive implementation of factorials
    '''
    # Base case: factorial of 0 or 1 is 1
    if n < 2:
        return 1
    # Recursive case: n! = n * (n-1)!
    else:
        return n * factorial(n-1)


# ## Basic test

# In[ ]:


for n in range(21):
    print(f"Factorial of {n}: {factorial(n)}")


# Ok, that **works well** enough for these **small numbers**.
# 
# But we **may run into problems** for a **bigger number**.

# ## Recursion and infinite loops
# **Recursions depend on** a **base case to stop** them. **If** you **make a mistake** on that end case, you **may end up going on forever** ... (or until you **hit the recursion limit**).

# ### A broken factorial
# Let's make a **small change to our base case**. **Instead of** checking for **n < 2**, we'll check for **n == 1**. That's reasonable, since n will eventually get to 1.

# In[ ]:


def bad_factorial(n):
    '''
    Recursive implementation of factorials
    '''
    # Base case: factorial of 1 is 1
    if n == 1:
        return 1
    # Recursive case: n! = n * (n-1)!
    else:
        return n * bad_factorial(n-1)


# In[ ]:


n = 5


# In[ ]:


print(f"Factorial of {n} is {bad_factorial(n)}")


# No problem. What was I worried about?
# 
# Well, let's try factorial of 0 now. That's a valid operation.

# <span style="color:red">**WARNING: This next step will probably crash your Python kernel**</span>
# <span style="color:red"> Save your notebook if you made changes.</span>

# In[ ]:


#n = 0


# In[ ]:


print(f"Factorial of {n} is {bad_factorial(n)}")


# <span style="color:red">**Kaboom!!!**</span> **If** you **don't want to keep crashing**, make sure you **change *n* to** something **greater than 0**.

# You may think that you wouldn't make a simple mistake like that in your base class, and that may be true for a simple problem like factorial. However, **for some recursions**, the **base case may not be** as **obvious**, so you **need to be carefull**.

# ## Recursion and stack memory
# **When** an **application makes a function call**, it **requires stack memory** to be allocated to maintain local variables. The **memory** will be **released when** the **function is completed**. 
# 
# In the case of recursion, **each recursive call** will **require additional** stack **memory**, and the **memory will not be released until** the **recursion stops**, and **all** the cascading **calls complete**. If the recursion level is very deep, this **can be extremely costly in terms of memory**, so **Python** will **impose** a **limit on recursions**. Let's see this in action.

# ### The recursion limit

# <span style="color:red">**WARNING: This next step will probably crash your Python kernel**</span>
# <span style="color:red"> Save your notebook if you made changes.</span>

# Let's see **what happens if we do** the **factorial of 10,000**.
# 
# We use a little **fancy if statement** here, because **factorials get so big** so fast, we **don't want to fill up** our **screen** with numbers. So we'll **cap** our **printable results at 1 trillion**.

# In[ ]:


n = 10


# In[ ]:


# calculate the factorial
result = factorial(n)

# print factorial, or a message if the number is bigger than 1 trillion
if (result > 1000000000000):
    print(f"Wow! Factorial of {n} is bigger than one trillion!")
else:
    print(f"Factorial of {n}: {result}")


# <span style="color:red">**Kaboom!!!**</span> (if you didn't crash your notebook, try 100000)
# You'll **probably need to retart your notebook**.
# 
# **If** you **don't want to keep crashing**, make sure you **change *n* to** something smaller like **10**.

# ### Why did I crash?
# As I mentioned, **recursion uses** extra **memory to maintain** the **call stack**. We don't want a misbehaving program to take over all of our memory, so **there is a system limit**. The **value can vary**, but you can **verify it using** the ***sys.getrecursionlimit()***

# In[ ]:


import sys

# print the recursion limit
print(f"My current recursion limit is: {sys.getrecursionlimit()}")


# So **in my case**, my **recursion limit was 3000**, so the **number of recursions required to calculate 10,000!** (which is 10,000 recursions) was **over the limit**. You **can update** that **limit** with a ***sys.setrecursionlimit()*** call, **but** that would mean you are **taking up a lot of memory.**

# # Example: Binary Tree Traversal
# We have already looked at a binary search tree (BST) before. Just to recal, it is a **tree data structure** with the following properties:
# - **No duplicate** elements.
# - **Each node** has no more than **two children**, a left child and a right child
#     - **Left** child value is always **less than** the current node.
#     - **Right** child value is always **greater than** the current node.
# 
# There are **multiple recursive methods** used in it, but **for this discussion**, we will **focus primarily on** the **tree traversal**. Traversing a tree means walking through every node of the tree. For a BST, the **most common traversal** is what we call an **in-order** traversal, which will r**eturn the nodes in sorted order**.

# ### TreeNode Class

# In[ ]:


class TreeNode:
    '''
    Node for a binary tree
    '''
    def __init__(self, key):
        '''
        Parameters:
            key: The key to be stored in the node
            left: Pointer to the left child node
            right: Pointer to the right child node
        '''
        self.key = key
        self.left = None
        self.right = None
        
    def __str__():
        return self.key


# ### BinarySearchTree Class
# The binary search tree class will perform the basic operations required to implementain and maintain the properties we defined. **For our discussion**, **pay close attention** to the ***traverse* method**. Not how simple it is.

# In[ ]:


class BinarySearchTree:
    '''
    A Binary Search Tree
    '''
    def __init__(self):
        # initialize the root of the tree
        self.root = None

    def traverse(self):
        '''
        Returns a list of the tree's data, in order from smallest to largest
        '''

        # kick off a recursive traversal of the tree, starting at the root
        return self._traverse(self.root, [])

    def _traverse(self, node, result):
        '''
        This method will recursively traverse a tree in order from lowest to highest, 
        starting from the input node.
        '''

        # if the node is not None
        if node is not None:
            # recursively traverse the left sub-tree first for the smaller items
            self._traverse(node.left, result)

            # now append current node to result list
            result.append(node.key)

            # recursively traverse the right sub-tree for the larger items
            self._traverse(node.right, result)

        return result
    
    def _insert_node(self, curr_node, new_key):
        '''
        This method will insert a node in the binary tree, by recursively trying to insert 
        on the left or right subtree, depending on whether the key is smaller or larger 
        than the current node.

        Returns the node that was inserted.
        '''
        # if the current node is None, than we found the right place to insert, so create a node for the key
        if curr_node is None:
            return TreeNode(new_key)
        
        # else, if the new key is less than the current key, recursively try to insert on the left
        elif new_key < curr_node.key:
            curr_node.left = self._insert_node(curr_node.left, new_key)
            
        # else, if the new key is greater than the current key, recursively try to insert on the right
        elif new_key > curr_node.key:
            curr_node.right = self._insert_node(curr_node.right, new_key)
            
        # if we went through both comparisons, then the key is equal to the current key, so do nothing

        # return the updated node
        return curr_node


    def insert(self, new_key):
        '''
        Starting at the root, invoke recursive method to insert node for this key
        '''
        self.root = self._insert_node(self.root, new_key)
        
    def _search(self, curr_node, search_key):
        '''
        Search for a value in the binary search tree, by recursively looking for it on the left and right subtree,
        depending on whether the value is smaller or larger than the current node.
        '''
        # if the current node is None, then the value is not in the tree
        if (curr_node is None):
            return False

        # if the current node value is the same as the search value, return True
        elif (curr_node.key == search_key):
            return True

        # else, if the search value is larger, then try to find on the right
        elif (search_key > curr_node.key):
            return self._search(curr_node.right, search_key)

        # else the search value is smaller, so try to find on the left
        else:
            return self._search(curr_node.left, search_key)

    def search(self, search_key):
        '''
        Search for a value in the binary search tree.
        This will trigger a recursive lookup, starting at the root of the tree.
        '''
        return self._search(self.root, search_key)
        
    def _to_str(self, curr_node, level):
        '''
        Recursive function that will print elements of a tree, indenting to the right based on level
        '''
        # initialize return string
        curr_str = ""
        edge_indicator = ""
        
        # if the current node is not None ...
        if curr_node:
            # set an indicator to help visualize which children nodes
            if (curr_node.left and curr_node.right):
                edge_indicator = "<"
            elif (curr_node.left):
                edge_indicator = "\\"
            elif (curr_node.right):
                edge_indicator = "/"
            else:
                edge_indicator = ""
                
            # recusively add the right sub-tree, incresing the level (indentation)
            curr_str += self._to_str(curr_node.right, level + 1) 

            # add the data in this node
            curr_str += "          " * level + str(curr_node.key) + edge_indicator + "\n"

            # recusively add the left sub-tree, incresing the level (indentation)
            curr_str += self._to_str(curr_node.left, level + 1)

        # return string for this node/sub-tree
        return curr_str

    def __str__(self):
        '''
        Call internal method that will recursively print all nodes, starting with the root
        '''
        # starting add the root, generate string recursively
        return self._to_str(self.root, 0)


# #### Create and add data
# Add a few simple nodes and print it

# In[ ]:


# create a new binary tree
test_tree= BinarySearchTree()

# add data to the tree
test_tree.insert(4)
test_tree.insert(6)
test_tree.insert(2)
test_tree.insert(5)
test_tree.insert(7)
test_tree.insert(1)

print(test_tree)


# #### Test tree traversal

# In[ ]:


tree_nodes = test_tree.traverse()
print(tree_nodes)


# # To recurse or not to recurse, that is the question
# I'm referencing a little Shakespeare here to bring an often asked question. **When should I use recursion?**
# 
# As we've just seen, **recursion can raise** a number of **concerns** in terms of **resource utilization**. So **why should you use it at all?** Well, the **fact is** there are **some problems** which **are solved much easier and ellagantly with recursion**. So my personal suggestion, and that's not an official AWS position, is ... **use recursion when you need to**.
# 
# Yes, that may sound like a silly answer, but it's not. **If there is** an **equivalent iterative solution** (something something using a regular loop), which is **still relatively simple**, I would **suggest using that**. **Save** the **recursion for** those **cases where** a **non-recursive solution** is **very complex**.
# 
# Let's look at some examples.

# ## Factorial without recursion
# We've seen a recursive implementation of factorial, but it **can** just as **easily be done with simple iteration**.

# In[ ]:


def factorial_nr(n):
    '''
    Non-recursice implementation of factorials
    '''

    result = 1
    for i in range(2, n + 1):
        result = result * i

    return result


# ### Basic test

# In[ ]:


for n in range(21):
    print(f"Factorial of {n}: {factorial_nr(n)}")


# ### Testing with a big number
# Remember that **10,000 broke our recursive solution**. Will it work here?

# In[ ]:


n = 10000


# In[ ]:


# calculate the factorial using recursion
result = factorial_nr(n)

# print factorial, or a message if the number is bigger than 1 trillion
if (result > 1000000000000):
    print(f"Wow! Factorial of {n} is bigger than one trillion!")
else:
    print(f"Factorial of {n}: {result}")


# **No problem!** The code above doesn't print out the result of 10000!, because that would be a huge value going across multiple pages of our notebook. But the the code worked without an error.

# ### Conclusion
# This **solution** seems **just as simple**, **doesn't use extra memory**, and **doesn't** run the **risk** of **breaking my kernel**. So other than being a good academic example, the plain factorial recursive solution doesn't seem like a good option here.

# ## Binary Search Tree Traversal without recursion
# Let's return to our Binary Search Tree. We will now show an **updated implementation**, where the **traversal** is performed **without using recursion**. 

# This is **mostly the same class** as the one seen earlier **except for the traverse method**. That method was **changed to implement traversal without using recursion**. **Note** the level of **complexity** required.

# In[ ]:


class BinarySearchTreeNR:
    '''
    A Binary Search Tree
    '''
    def __init__(self):
        # initialize the root of the tree
        self.root = None

    def traverse(self):
        '''
        Traverse the tree in order without using recursion
        '''
        # initialize the result list
        result = []

        # initialize the current node to the root
        curr_node = self.root

        # while the current node is not None
        while curr_node:
            # if the current node has no left child
            if curr_node.left is None:
                # append the current node's value to the result list
                result.append(curr_node.key)

                # move to the right child
                curr_node = curr_node.right
            else:
                # find the inorder predecessor of the current node
                pre = curr_node.left
                while pre.right and pre.right != curr_node:
                    pre = pre.right

                # if the inorder predecessor's right child is the current node
                if pre.right == curr_node:
                    # append the current node's value to the result list
                    result.append(curr_node.key)

                    # move to the right child
                    curr_node = curr_node.right

                    # remove the inorder predecessor's right child
                    pre.right = None
                else:
                    # set the inorder predecessor's right child to the current node
                    pre.right = curr_node

                    # move to the left child
                    curr_node = curr_node.left

        # return the result list
        return result

    
    def _insert_node(self, curr_node, new_key):
        '''
        This method will insert a node in the binary tree, by recursively trying to insert 
        on the left or right subtree, depending on whether the key is smaller or larger 
        than the current node.

        Returns the node that was inserted.
        '''
        # if the current node is None, than we found the right place to insert, so create a node for the key
        if curr_node is None:
            return TreeNode(new_key)
        
        # else, if the new key is less than the current key, recursively try to insert on the left
        elif new_key < curr_node.key:
            curr_node.left = self._insert_node(curr_node.left, new_key)
            
        # else, if the new key is greater than the current key, recursively try to insert on the right
        elif new_key > curr_node.key:
            curr_node.right = self._insert_node(curr_node.right, new_key)
            
        # if we went through both comparisons, then the key is equal to the current key, so do nothing

        # return the updated node
        return curr_node


    def insert(self, new_key):
        '''
        Starting at the root, invoke recursive method to insert node for this key
        '''
        self.root = self._insert_node(self.root, new_key)
        
    def _search(self, curr_node, search_key):
        '''
        Search for a value in the binary search tree, by recursively looking for it on the left and right subtree,
        depending on whether the value is smaller or larger than the current node.
        '''
        # if the current node is None, then the value is not in the tree
        if (curr_node is None):
            return False

        # if the current node value is the same as the search value, return True
        elif (curr_node.key == search_key):
            return True

        # else, if the search value is larger, then try to find on the right
        elif (search_key > curr_node.key):
            return self._search(curr_node.right, search_key)

        # else the search value is smaller, so try to find on the left
        else:
            return self._search(curr_node.left, search_key)

    def search(self, search_key):
        '''
        Search for a value in the binary search tree.
        This will trigger a recursive lookup, starting at the root of the tree.
        '''
        return self._search(self.root, search_key)
        
    def _to_str(self, curr_node, level):
        '''
        Recursive function that will print elements of a tree, indenting to the right based on level
        '''
        # initialize return string
        curr_str = ""
        edge_indicator = ""
        
        # if the current node is not None ...
        if curr_node:
            # set an indicator to help visualize which children nodes
            if (curr_node.left and curr_node.right):
                edge_indicator = "<"
            elif (curr_node.left):
                edge_indicator = "\\"
            elif (curr_node.right):
                edge_indicator = "/"
            else:
                edge_indicator = ""
                
            # recusively add the right sub-tree, incresing the level (indentation)
            curr_str += self._to_str(curr_node.right, level + 1) 

            # add the data in this node
            curr_str += "          " * level + str(curr_node.key) + edge_indicator + "\n"

            # recusively add the left sub-tree, incresing the level (indentation)
            curr_str += self._to_str(curr_node.left, level + 1)

        # return string for this node/sub-tree
        return curr_str

    def __str__(self):
        '''
        Call internal method that will recursively print all nodes, starting with the root
        '''
        # starting add the root, generate string recursively
        return self._to_str(self.root, 0)


# #### Create and add data
# Add a few simple nodes and print it

# In[ ]:


# create a new binary tree
test_tree= BinarySearchTreeNR()

# add data to the tree
test_tree.insert(4)
test_tree.insert(1)
test_tree.insert(6)
test_tree.insert(3)
test_tree.insert(5)
test_tree.insert(2)
test_tree.insert(7)

print(test_tree)


# #### Test tree traversal

# In[ ]:


tree_nodes = test_tree.traverse()
print(tree_nodes)


# ### Conclusion
# This **works ... but** if we look at the **code**, it is **very long**, and **difficult to follow**. **Tree operations** are one of those cases where **recursion generates** far **simpler code than iteration**. So in this case, I would **favor the recursive solution**.

# # N-Queens Problem

# The N-Queens problem is a puzzle that involves **placing N chess queens on an N×N chessboard** so that **no two queens threaten each other**. In other words, **no two queens should share** the **same row, column, or diagonal** line. 

# #### Main recursive function implementing backtracking

# In[ ]:


QUEEN = 'Q'
FREE_SPACE = '-'

def _queens_helper(board, row):
    """
    Recursive solver function. This solution attempts to position queens, top to bottom, row by row.
    As we recurse, we'll move down one row.

    Parameters:
    - board(List[List[int]]): chess board
    - row(int): current row

    Returns:
    - bool
    """

    # This is the exit condition. 
    # If we reached the end of the board, and have not backtracked, than we have a solution
    if row >= len(board):
        return True
    
    # for the current row, start looking for a possible column, from left to right
    for col in range(len(board)):
        # if placing a queen in this column would be valid so far ... 
        if _is_valid_position(board, col, row):           
            # Place the queen on given position (for now), and recursively call for the next row
            board[row][col] = QUEEN
            
            # if all the recursive calls ultimately return true. The found a solution, stored in the board variable
            if _queens_helper(board, row + 1):
                return True

            # If the placement didn't lead to solution, backtrack by marking the posiion empty
            # the algorithm will move to the next column and try again
            else:
                board[row][col] = FREE_SPACE

    return False


# #### Evaluate if current position is a valid position

# In[ ]:


def _is_valid_position(board, curr_col, curr_row):
    """
    Checks if a queen could be placed on given position. This alogorith assumes that queens are being placed
    top to bottom row by row. Therefore, it only checks for queens above the current row, since rows below 
    would be empty.

    Parameters:
    - board(List[List[str]]): chess board
    - row(int): row to check
    - col(int) column to check

    Returns:
    - bool
    """

    # set row and col variables that we'll use to iterate to current position we're checking
    row, col = curr_row, curr_col
            
    # Check if the left diagonal has any queen
    while row > -1 and col > -1:
        if board[row][col] == QUEEN:
            return False

        row -= 1
        col -= 1
        
    # reset row and col variables that we'll use to iterate to current position we're checking
    row, col = curr_row, curr_col
    
    # Check if the right diagonal has any queen
    while row > -1 and col < len(board):
        if board[row][col] == QUEEN:
            return False

        row -= 1
        col += 1

    # reset row and col variables that we'll use to iterate to current position we're checking
    row, col = curr_row, curr_col

    # Check if the columns have any queen
    while row > -1:
        if board[row][col] == QUEEN:
            return False

        row -= 1

    return True


# #### Initializes an empty board of the specified size

# In[ ]:


def _initialize_board(size):
    """
    Initialize empty chess board

    Parameters:
    - size(int)

    Returns:
    - List[List[str]]
    """
    return [[FREE_SPACE for _ in range(size)] for _ in range(size)]


# #### Print board
# Prints a board. Not needed for solution, but good for troubleshooting and verifyin results.

# In[ ]:


def print_board(board, indent = 0):
    """
    Prints chess board.

    Parameters:
    - board(List[List[str]])
    - indent(int): number of spaces to indent the board
    """
  
    for row in board:
        print("".rjust(indent), end='')
        for col in row:
            print(col, end=' ')
        print(flush=True)


# #### Main Function
# This is the function that is **called to start the solution process**.
# It initializes the board, and initiates the algorithm.

# In[ ]:


def queens(size):
    """
    Solves Queens problem if possible

    Parameters:
    - size(int)

    Returns:
    - bool: is any solution found
    - List[List[str]]: chess board with queens placed
    """

    # initialize the board variable with an empty board
    board = _initialize_board(size)

    # Call method to recursively find solution
    # Method tries top to bottom, so start it at row 0
    solved = _queens_helper(board, 0)
    
    return solved, board


# #### Test
# Let's try our algorithm.

# In[ ]:


size = 3

solved, board = queens(size)
if solved:
    print(f'\nSolved for a {size} X {size} board!')
    print_board(board)
else:
    print(f'\nSolution does not exist for a {size} X {size} board.')
    
size = 4

solved, board = queens(size)
if solved:
    print(f'\nSolved for a {size} X {size} board!')
    print_board(board)
else:
    print(f'\nSolution does not exist for a {size} X {size} board.')
    
size = 7

solved, board = queens(size)
if solved:
    print(f'\nSolved for a {size} X {size} board!')
    print_board(board)
else:
    print(f'\nSolution does not exist for a {size} X {size} board.')
    
size = 8

solved, board = queens(size)
if solved:
    print(f'\nSolved for a {size} X {size} board!')
    print_board(board)
else:
    print(f'\nSolution does not exist for a {size} X {size} board.')

size = 10

solved, board = queens(size)
if solved:
    print(f'\nSolved for a {size} X {size} board!')
    print_board(board)
else:
    print(f'\nSolution does not exist for a {size} X {size} board.')


# ### Modified version with print statements
# Let's create a **modified version**, **with print statements** to **visualize what happens** during the recursion  processing. We will **use indentation** to help **see**
# the various **levels of recursion**. We **add** the **"_wp" ("with print")** to the end of the function **to differentiate**. This is exactly the same version as above, but it adds several print statements to help visualize the recursion and backtracking. 
# 
# The **only function changed** at all is the **main recursive fuction** which adds the print statements. So we **won't reimplement** the **other ones**.

# #### Main recursive function implementing backtracking

# In[ ]:


QUEEN = 'Q'
FREE_SPACE = '-'

def _queens_helper_wp(board, row):
    """
    Recursive solver function. This solution attempts to position queens, top to bottom, row by row.
    As we recurse, we'll move down one row.

    Parameters:
    - board(List[List[int]]): chess board
    - row(int): current row

    Returns:
    - bool
    """

    print("".rjust(row*4) + f">>> Trying row {row}. Current board:")
    print_board(board, row*4)

    # This is the exit condition. 
    # If we reached the end of the board, and have not backtracked, than we have a solution
    if row >= len(board):
        return True

    # for the current row, start looking for a possible column, from left to right
    for col in range(len(board)):
        print("".rjust(row*4) + f"Checking row {row}, col {col} - ", end="")
        # if placing a queen in this column would be valid so far 
        if _is_valid_position(board, col, row):
            print("VALID")
            
            # Place the queen on given position (for now), and recursively call for the next row
            print("".rjust(row*4) + f"Adding queen to [{row}][{col}]. Update board:")
            board[row][col] = QUEEN
            print_board(board,row*4)
            
            # if all the recursive calls ultimately return true. The found a solution, stored in the board variable
            if _queens_helper_wp(board, row + 1):
                return True

            # If the placement didn't lead to solution, backtrack by marking the posiion empty
            # the algorithm will move to the next column and try again
            else:
                board[row][col] = FREE_SPACE

            print("".rjust(row*4) + f"<<< Backtracked row {row}, col {col}. Updated board: ")
            print_board(board,row*4)
        # added strictly for debugging
        else:
            print("NOT valid")

    print("".rjust(row*4) + f"---- FAIL ---- No way to place queen in row {row} in current board")
    return False


# #### Main Function
# This is the function that is called to start the solution process.
# It initializes the board, and initiates the algorithm.

# In[ ]:


def queens_wp(size):
    """
    Solves Queens problem if possible

    Parameters:
    - size(int)

    Returns:
    - bool: is any solution found
    - List[List[str]]: chess board with queens placed
    """

    # initialize the board variable with an empty board
    board = _initialize_board(size)

    # Call method to recursively find solution
    # Method tries top to bottom, so start it at row 0
    solved = _queens_helper_wp(board, 0)
    
    return solved, board


# #### Test and observer output
# Let's try our algorithm with the simple size of 4 first. You can see the board proggresively building from top to bottom, left to tight, and backtracking when it can't continue.

# In[ ]:


size = 4

solved, board = queens_wp(size)
if solved:
    print(f'\nSolved for a {size} X {size} board!')
    print_board(board)
else:
    print(f'\nSolution does not exist for a {size} X {size} board.')

