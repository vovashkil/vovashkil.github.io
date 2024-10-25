# Advanced Data Structures Part 1

* **back to AWS Cloud Institute repo's root [aci.md](../aci.md)**
* **back to repo's main [README.md](../../../README.md)**

## Linked Lists

### Use cases

* You don’t know how many elements your list will have or if you will want to reorder the elements of the list.
* You need to insert into or delete from the middle of the list without actually moving the data around. (Using a linked list means Python does not need to find a bigger contiguous block of memory to store the data.)
* You need to build a data structure, such as a stack or queue, that can efficiently add or remove elements from its front and back.

### Advantages

* The nodes of linked lists can be manipulated (added, deleted, or inserted into the front, middle, or end). This can be done without causing the data of the node to move or be copied in memory. Data never has to move though the nodes and can effectively move as the pointers change.
* Linked lists can grow and shrink dynamically. Adding to and removing nodes from the lists is efficient.
* Linked lists can be conveniently reorganized and resized without the data of the nodes having to be put in one contiguous block of memory. The data of the nodes can be scattered throughout memory.  
* Inserting and deleting elements in the middle of a linked list is generally more efficient than an array. This is because array implementations generally require elements to be copied and reordered after the deletion or insertion index.  

### Disadvantages

* Linked list nodes are not accessed directly by specifying an element index. This means that they are slow for indexing and searching. An application trying to search a linked list might have to traverse the entire collection to find what it's looking for. To access linked list data, you need to traverse its nodes, which means that you need to move up and down the list. 
* Linked list nodes require pointers, which point to the next or previous node in the list. Extra memory is required to store the node's pointers, in addition to the data in each node.

### Node

A node is an object that contains data and has one or more pointers to other nodes.

### Knowledge Check

#### Which statements are true about linked lists? (Select TWO.)

* They are linear data structures.
* They consist of nodes that contain data and have at least one pointer to another node.

Wrong answers:

* They are non-linear data structures.
* They have nodes that store data contiguously in memory.
* They cannot be implemented in Python.

Linked lists are linear data structures that consist of a collection of nodes, and each node contains data and at least one pointer. Pointers are node variables that point to the location of the next node in the list.

The other answers are incorrect because linked lists are not non-linear data structures, and they are not array based. Linked list nodes are not stored in contiguous memory blocks. Linked lists can be implemented in Python, although they are not built-in like some other data structures.

#### What can the following code snippet be used to do?

```
class SinglyLL:
def __init__(self):
        self.head = None
```

* Instantiate an empty linked list object that has a null head pointer

Wrong answers:

* Instantiate a linked list object that has one empty node.
* Instantiate several linked list objects with both head and tail pointers and an empty node.
* Instantiate a node object with a head pointer that points back to itself.

#### What is the nature of the pointer in the last node of a singly linked list? 

* It points to None (null pointer).

Wrong answers:

* It points to the previous node.
* It points to all the nodes.
* It points to its own node.

### Summary

A linked list is a data structure that consists of nodes and pointers. Nodes are objects that hold data, while pointers function as the links between nodes. Pointers point to next or previous nodes in the linked list. You learned about different types of linked lists and how they operate. Singly linked lists are traversed from the first node to the last node. Doubly linked lists can traverse from the first node to the last, and back. Circular singly linked lists, on the other hand, form a one-way loop, facilitating traversal from the first node to the last, and back to the beginning. Circular doubly linked lists can be traversed completely in both directions, forming a two-way loop.

Linked list data structures help solve many problems in computing and application development. For example, they can be used to implement queues or stacks, in addition to graphs. Linked lists are also useful for complex tasks, such as lifecycle management for an operating system application. Two of the main advantages of linked lists are their flexibility and efficient use of memory. They are an optimal data structure to choose when you need to traverse data linearly and prioritize the speed of insertions and removals.

## Hash Tables

### Pre-assessment

#### Which data types or structures are hashable? (Select TWO.)

* String
* Int

Wrong answers:

* List
* Dictionary
* Nested lists

Strings and integers are hashable because they are immutable in Python, meaning that they cannot be changed.

#### When does a hash collision occur?

* The hash function attempts to assign the index to data that is already used. 

Wrong answers:

* The hash function attempts to assign data to a variable that has not been used. 
* The hash function attempts to assign data to an index that is already used. 
* The hash function attempts to discard duplicate indexes if the index is already used.

#### The modulo operator is % in Python. What value does the modulo operation return?

* Remainder after division

Wrong answers:

* Product after multiplication
* Sum after addition
* Difference after subtraction

### What is a hash table?

A hash table is a data structure with index values generated by a hash function.

* **A data structure:** A data structure stores, organizes, and allows you to retrieve data.
* **With index values generated by a hash function:** A hash function uses a mathematical hashing formula to compute where to store an object and later, where to find the data.

Hash tables are also referred to as hash maps. In some programming languages, there are subtle differences between the two. In Python, they do the same things and are implemented in the same ways.

### Real-world hash table examples

#### Enzymes and indexes

You are assigned a research project about enzymes. You go to the library to do some research, and you find a textbook. You could open the textbook, start at page one, and keep reading until you see the word enzymes. Eventually, you might find the information you want, but you might be in the library for a long time. A better option would be to use the book’s index, and then turn directly to the page that has the information you want.

The index is a bit like a hash table. A hash table keeps a unique set of keys, which are all mapped to various other objects called values. In the book index, the topics, such as enzymes, are the keys. The values are the page numbers you want to read. With a book index, the keys are unique. And while the enzymes topic may or may not be included in the index, it's not repeated in the index twice.

#### Uniqueness and voting

Millions of people vote in an election. A rule states that a person may choose to vote or not vote, but no person is allowed to vote twice. To enforce this rule, the election officials need to know who has voted and who has not. They need a has voted list.  

However, after thousands of people have already voted, the next person checking in to the polling station would not want to wait while the officials go through the list from top to bottom. The officials need a data structure that can quickly find and retrieve elements while ensuring there are no duplicates. This means all the elements are unique.

As you will see, a hash table would be an ideal data structure for solving this problem. It allows for fast lookups and no duplicates, and it can handle large amounts of data efficiently. Adding or deleting a new voter from the list is also very efficient with hash tables.

### Advantages and disadvantages of hash tables

#### Advantages

* A hash table is an efficient way to implement a dictionary, or key and value map. 
* Hash tables can look up objects very quickly.
* Hash tables eliminate duplicate entries.
* Hash tables can handle large amounts of data efficiently.
* Hash tables can use any immutable data types as a key. This provides flexibility in how data is organized and accessed.

#### Disadvantages

* Hash tables are inefficient when there are many collisions.  
* Hash tables can be slow for traversing elements in a linear fashion if they use chaining and linked lists to resolve collisions.
* Hash tables have a limited capacity and will eventually fill up.
* Hash tables do not maintain the order of elements, which makes it difficult to retrieve elements in a specific order.

### Terminology

#### Equality

Objects are equal if they have the same values. A copy of an object will be equal to the original, even though they are two separate objects that are stored at two different memory addresses. In Python, you can use the == operator to test for value equality of most built-in types, such as strings, dictionaries, and lists. 

#### Hashing function

A hashing function is a function that returns a value that identifies an object. In Python, the hash() function does the calculation. Two objects with the same value will hash to the same identifier. You can use the hash function to compare keys in a dictionary.

#### Immutable

An immutable object's value never changes after it is created. Immutable objects are often used for safety, simplicity, and data integrity, and they include integers, strings, and tuples.

#### Modulo operation

The modulo operation is a mathematical operation that returns the value of the remainder in division. It is used in hash tables to convert hash values into valid indexes for efficient storage and retrieval of data.

### Handling Collisions

1. Chaining
2. Open addressing and probing

#### Chaining

Data with the same index number would be added as a node in the linked list.

Lookups include traversing the linked list that matches the hash. This preserves the data, but it can hurt performance. This is because, to find the value, the linked nodes have to be traversed in order. Traversing thousands or even millions of nodes could take a very long time.

#### Open addressing and probing

Open addressing stores all values in the same hash table. Also called closed hashing, this technique probes to find open slots to store the value.

Handling collisions is an important topic because if they are not handled properly, collisions can lead to data loss and slow lookups. When different keys hash the same index and overwrite each other, this leads to data loss. Also, having too many collisions and handling them with either open chaining or probing impacts the speed of lookups, including search and retrieval.

One of the limitations of linked lists is that they are not the best data structure for lookups. It is much quicker to go directly to an index to get the data than having to traverse through many nodes, as would be needed with chaining. It is also slower to find data that is stored in a different place than the prescribed index, as is what happens during open addressing and probing. While probing and open addressing can be faster than chaining, it is still slower than reducing the probability of collisions. Probing and open addressing causes slower performance due to the need to traverse the table to look for open indexes.

### Increase table size to reduce the probability of collisions 

One way to reduce the probability of collisions is to increase the table size.

Frequent collisions can degrade hash table performance, especially if you are having to continually traverse many linked list nodes to store and find data. To reduce the probability of collisions, the optimal hash table size for a given dataset is usually considered first.

### Hash Tables and Equality

* If two objects are equal, they must yield the same hash.
* If two hash values are unequal, the objects must be unequal.
* If two objects are unequal, it would be nice if they have different hashes. This does not always happen, and unequal objects that result in the same hashes can lead to collisions, as you have seen.

Hashing functions are one-way functions that take in an object and return a number. One-way means you can get the hash value from the object, but you cannot re-create the object from the hash value.

You can create your own hash function by using the Python built-in hash() function or a function from the Python hashlib library.

Hashing is something you can only perform on immutable objects. If an object is mutated, it would effectively be a different object and return a different hash value. The hashing data structures expect that the hash will remain the same throughout the lifecycle of the object. Only immutable objects are hashable.

Notice that the list is an unhashable type, and you cannot put a list into a set (or hash table).

```
print({[1, 2, 3]})
```

```
File "<exec>", line 1, in <module> 
TypeError: unhashable type: 'list' 
```

#### Object equality

If you need to override **__eq__**, make sure that you also override **__hash__**. Also, make sure that the **__eq__** methods of the **__hash__** function are based on the same member values. Here, the **__eq__** method is written to check for the equality of ids. The **__hash__** method should also be based on ids. It should be the hash value of ids.

### Knowledge Check

#### What is the formula for determining the index for the object x in the hash table table based on the hash value of x?

* hash(x) % len(table)

Wrong answers:

* len(table) % hash(x)
* % hash(x) * len(table)
* hash(table)% hash(x)

#### Which data structure is an implementation of a hash table in Python? 

* Set

Wrong answers:

* Tuple
* List
* Array

#### How can a hash table collision be handled? (Select TWO.)

* Chaining
* Probing

Wrong answers:

* Create a smaller table
* Create a bigger table
* Add more values

### Summary

In Python, a set is a built-in implementation of a hash table. A hash table maps objects to their corresponding indexes using a hashing function.

The hashing function converts immutable data, such as strings or numbers, into fixed-size values known as hash values or hash codes. For custom classes, like **User** or **Person**, you can override the **__eq__** and **__hash__** methods to determine equality and hash values based on specific instance attributes. The **__eq__** and **__hash__** methods have a tight relationship. If you override one, you must override the other.  

In hash tables, the hash value of an object is used to compute an index. This index value indicates the table location at which different items are inserted, searched for, or removed. This makes data lookups quicker and more efficient.

Sometimes, two different items yield the same hash value, and thus the same index. This results in a hash collision. There are different approaches to resolving these. One common approach is chaining, in which multiple items can be stored at the same index in a linked list. Another common approach to resolving hash collisions is probing, in which the hash table is traversed until the next open index is found.

The chances of hash collisions occurring can be minimized by ensuring the hash table is right-sized for the data load. The optimal performance of the hash table can then be balanced with responsible use of available application memory. 

In summary, hash tables are data structures optimized for fast lookups and storing unique values.

## Heaps

A heap is another data structure that is used to quickly find the smallest or largest element.

A heap is implemented internally as a tree data structure. Trees are non-linear data structures that store hierarchical data that can be searched in an organized way. Some common examples of trees include organizational charts, family trees, and the directory structure on your computer.

### Which heap operation do you use to add an element to a heap without altering the heap?

* heappush()

Wrong answers:

* heapify()
* heappop()
* heapreplace()

The other answers are incorrect because heapify() is used to create a heap from an array. Use heappop() to return the smallest element in the array, and use heapreplace() to replace the smallest element of the heap with a new value.

#### Which sentences are true about binary trees? (Select TWO.)

* The tree can be asymmetrical.
* Nodes are filled from the left.

Wrong answers:

* The tree must have two children.
* Nodes are filled from the left and right.
* Nodes can have more than two children.

The other answers are incorrect because binary trees can have no children, one child, or two children. Nodes are always filled from left to right, not from the right.

### Tree data structure

#### Nodes and edges

Nodes are hierarchical and connected to one another by edges.

#### Values and data

Each node in a tree typically contains a value or data.

#### Root nodes and leaf nodes

The root node is the topmost value in the tree.

A leaf node is a node that has no descendants. They do not branch out into any further nodes.

#### Parent and child nodes

A node can be a parent, a child, or both. Parent nodes have descendants, or children, that are further down on the tree. Child nodes are the descendants of parent nodes.

### Binary trees

There are different types of trees depending on how many children a parent can have. Heaps are often implemented using binary tree structures.

In a binary tree, any parent can have, at most, two children. A binary tree is considered complete when all the levels are completely filled except possibly the last level. In the last level of a complete binary tree, all the nodes are as far left as possible. The left-to-right sequential filling of a binary tree is how a binary heap array is made. This straightforward and efficient mapping of a binary tree into an array provides convenient access to parent and child nodes. It also facilitates operations such as insertion, deletion, and heapify, while preserving heap properties.

### Terminology Review

#### Node

A node is a hierarchical data structure part that contains data and is connected to the rest of the tree by edges.

#### Root

A root is the first node in a tree. The root node has no parent. All other nodes have a parent.

#### Parent

A parent is a node that has a child.

#### Child

A child is a node that has a parent.

#### Leaf

A leaf is node that has no children.

#### Binary tree

A binary tree is a tree where each node has zero, one, or two children.

#### Complete binary tree

A complete binary tree is a tree where all levels of the tree are fully filled and the nodes on the last level are filled from the left side.

### Heap Data Structure

Heap is a fundamental data structure that provides efficient access to the maximum or minimum element of a collection. It is a binary tree that satisfies the heap property. This means that for every node in a tree, the value is greater than or equal to its children in a max heap. In a min heap, the value is less than or equal to its children.

Two of the main uses of heap data structures are for sorting algorithms, like heapsort, and priority queue implementations. They provide a fast way to access and manipulate the maximum or minimum elements of a collection. This is useful in many real-world applications, such as job scheduling, event processing, and pathfinding algorithms.

### Types of heap data structures

#### Max heap

In a max heap, the value of the parent is greater than or equal to its children. Therefore, the root node is the greatest of all nodes.

#### Min heap

For a min heap, the value of each parent is less than or equal to its children. Therefore, the root node is the least of all nodes.

Several operations are used in heap data structures. Some common operations include heapify, heappush, heappop, heapreplace, and reheap.

### Heap operations

#### heapify

heapify is a process of creating a heap from an array.

#### heappush

The heappush function adds a data element to the heap.

#### heappop

The heappop function returns the smallest data element from the heap.

#### heapreplace

The heapreplace function replaces the smallest data element with a new value supplied in the function.

#### reheap

The reheap function causes the heap to reorganize so that the minimum (or maximum) node becomes the root. It is required whenever the root node is deleted or new nodes are added.

### Activity: Implementing a Heap

Python has a heap library, heapq, with ready-to-use methods and functions.

One technique used by the heapq library to reheap is known as the heap queue algorithm, or the priority algorithm. Because complete binary trees are nicely represented in array-like structures, the heapq library uses a Python list to hold the heap.

**heapq heapify()** function can be used to sort a list of numbers so that element 0 becomes the minimum value.

```
import heapq as heap

# Create a random list of numbers.
original_nums = [11, 30, -5, 99, -7, 0, 2] 

# Make a copy of the list.
my_nums = original_nums.copy()

# Show list before heapify.
print('List of numbers before heapify:', my_nums) 

# Heapify the list and show results.
heap.heapify(my_nums) 
print('Original list after heapify:', my_nums) 
print('MINIMUM value of orginal list = ', my_nums[0]) 
```

```
Original list of numbers: [11, 30, -5, 99, -7, 0, 2] 
Original list after heapify: [-7, 11, -5, 99, 30, 0, 2] 
MINIMUM value of orginal list =  -7 
```

### Determine maximum value in a heap

The Python heapq module provides an implementation of the heap queue algorithm, also known as the priority queue algorithm. By default, it creates a min heap, where the smallest element is always at the root (index 0). This property is useful when you need to repeatedly remove the smallest element from a collection (for example, in a priority queue data structure).

The heapq module does not provide built-in support for max heaps.

```
import heapq as heap

# Create a random list of numbers.
original_nums = [11, 30, -5, 99, -7, 0, 2]
# Show list before heapify.
print('Original list of numbers:', original_nums)

# Negate original numbers
my_nums = [ -x for x in original_nums]
# Show list before heapify.
print('\nOriginal list with negated values:', my_nums)

# Heapify the list and show results.
heap.heapify(my_nums)
print('Negated values after heapify:', my_nums)
print('MAXIMUM value of original list = ', -my_nums[0])

```

```
Original list of numbers: [11, 30, -5, 99, -7, 0, 2]

Original list with negated values: [-11, -30, 5, -99, 7, 0, -2]
Negated values after heapify: [-99, -30, -2, -11, 7, 0, 5]
MAXIMUM value of original list =  99
```

#### Explanation

In this solution, the trick is to negate all the numbers in the list before creating the heap. Negating means that if you have a positive number, negation will make it negative. If you have a negative number, negation will make it positive. In Python, you can negate a number by prefixing it with a minus sign (-). Another way to do this is to multiply by negative one (-1). This results in a value with the same magnitude but with the opposite sign. This way, the largest number becomes the smallest, and it will be placed at the root of the heap. 

When you need to retrieve the maximum value, multiply the minimum of the min heap by negative on again. In the previous example, -99 * -1 = 99, which is the maximum of the original list of numbers.

### Knowledge Check

#### Which statements are true about tree nodes? (Select TWO.)

* Nodes are connected to one another by edges.
* Nodes contain data and edges.

Wrong answers:

* Nodes are always parents.
* Nodes are always children.
* Nodes contain data only.

Tree nodes are connected to one another by edges. All nodes contain data and at least one edge.

#### Which statements are true about the root node in a min heap? (Select TWO.)

* The root node's value is less than its child nodes' values.
* The root node contains the minimum value in the heap.

Wrong answers:

* The root node contains the median value in the heap.
* The root node contains the maximum value in the heap.
* The root node's value is greater than its child nodes' values.

#### What does the reheap function do after an element is inserted?

* Reorganizes the tree structure after an element is inserted so that the min or max values become the root

Wrong answers:

* Deletes the node values that are greater than the inserted element
* Organizes all the nodes in the heap data after an element is inserted so that the structure is in ascending order
* Reorganizes the tree structure after an element is inserted so that the mid value becomes the root

### Summary

Heaps are the fastest data structures for finding minimum or maximum values. They accomplish this by taking advantage of complete binary trees. 

In this section, you learned about heaps, a powerful data structure used for hierarchical data storage in a well-organized manner. Heaps are complete binary trees. Every node is either greater than or equal to all of its children in a max heap. In a min heap, every node is lesser than or equal to all of its children. 

Heaps provide fast search operations and are commonly used in algorithms and data structures. You also learned about the heapq library, which implements the heap queue functionality. There are several main functions, including heapify, heappush, and heappop. These functions are used to add elements to the heap, remove the smallest element, and maintain the heap property. Two additional functions are replace and reheap. The replace function replaces the smallest data element, and reheap reorganizes the heap so that the minimum or maximum node becomes the root. Understanding these functions is essential for efficient and effective programming when working with heaps in Python.
