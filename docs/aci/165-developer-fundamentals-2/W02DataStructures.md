# Data Structures

* **back to AWS Cloud Institute repo's root [aci.md](../aci.md)**
* **back to repo's main [README.md](../../../README.md)**

## Comparison of Built-in Python Data Structures

### Lists

#### Summary

* Lists are linear collections of objects that are indexed by sequence starting with zero.
* They are mutable in that they can be changed after creation. For example, lists can start empty but can grow and shrink later.
* Lists are created with square brackets [ ] and commas between elements.
* Lists can consist of mixed-value types.

#### Selected methods

* **append()** adds an element to the end of the list.
* **clear()** removes all elements from the list.
* **count()** returns the number of elements with a specified value in the list.
* **insert()** adds an element at the specified position.
* **pop()** removes the element at the specified position. If no position is specified, **pop()** will remove the last item in a list.
* **remove()** removes the first item with the specified value.
* **reverse()** reverses the order of the list.

#### Examples

```
my_list = [' band ', 'singer' , 4 , 'anycompany']
print(my_list)
my_list.append('234')
my_list.insert(1,'red')
print(my_list.pop(0))
my_list.reverse()
print(my_list)
```

### Dictionaries

#### Summary

* Dictionaries are collections of mapping objects that map keys to values, and the collection is indexed by using the keys. Although the values can be any objects, the keys must be immutable.
* Dictionaries are created with curly braces {  }. A dictionary can contain any type of object, but the keys must be immutable (hashable).

#### Selected methods

* **clear()** removes all the elements from a dictionary.
* **copy()** returns a shallow copy of the dictionary. This means that the new dictionary has a copy of all key and value object references of the original dictionary, but the underlying objects themselves are not copied.
* **get()** returns the value of the specified key. Note that this would return the same value as my_dictionary['brand'].
* **items()** returns a list containing a tuple for each key-value pair.
* **keys()** returns a list of the dictionary’s keys.
* **pop()** takes a key name as a parameter and removes the item with the specified key.
* **values()** returns a list of all the values in the dictionary.

#### Examples

```
my_dictionary = {'brand ': 'AnyCompany', 'model': 'example', 'year': 1965}
print(my_dictionary)
print(my_dictionary.keys())
print(my_dictionary.values())
print(my_dictionary.pop('model'))
```

### Tuples

#### Summary

* Tuples are created with parentheses (  ) and consist of one or more elements separated by commas.
* They can contain mixed-type elements, such as strings and numeric values or any other type of object.
* After it is created, the tuple cannot be modified, in that it cannot grow or shrink. However, mutable objects stored in the tuple can be modified. For example, you access a dictionary inside a tuple and modify the contents of the dictionary.

#### Selected methods

* **count()** returns the number of times that a specified value occurs in a tuple.
* **index()** searches the tuple for a specified value and returns the position of where it was found.

#### Examples

```
my_tuple = ('Wei', 3.001, 'Wyoming', 3.001, 1990)
print(my_tuple)
print(my_tuple.index(1990))
print(my_tuple.count(3.001))
```

### Sets

#### Summary

* Sets are created with curly braces {  }.
* Empty sets are allowed, and the number of elements in a set can be modified by using methods that add or remove terms or combine multiple sets.
* Sets contain only immutable (unchangeable) individual elements, like tuples, numbers, and strings. Therefore, dictionaries and lists, which are mutable and can be changed, cannot be elements of sets.
* Sets can consist of elements of different types. For example, one set could include both string elements and number elements.
* Sets are unordered and contain unique elements. Duplicate elements when combining multiple sets are only represented in the set once.

#### Selected methods

* **set()** creates a set.
* **len()** returns the number of elements in a set.
* **x1.union(x2)** returns the union of two sets, which is the combination of both sets. This type of union works even if **x2** is not a set. It would convert **x2** to a set and then create the union with **x1**.
* **x1.intersection(x2)** yields the set that contains all elements that two sets have in common.
* **x1.difference(x2)** returns all elements that are in x1 but not in **x2**. It works like subtraction by subtracting the elements from x1 that exist in **x2**.

#### Examples

```
my_set = {1, 'red', 3.2}
my_set2 = {1, 'yellow', 3.2, 'true'}
print(my_set, 'and', my_set2)
print(len(my_set))
print(my_set.intersection(my_set2))
print(my_set.difference(my_set2))
print(my_set.union(my_set2))
```

### Comparison of lists, dictionaries, tuples, and sets 

#### Lists

Lists provide quick access to elements in them. Lists are ordered, so if you know an element's position, you can access the element directly by its index. Insertions and removals can be efficient if they happen at the end of the list. Lists are useful when you need an ordered collection of elements that can be updated.

#### Dictionaries

Dictionaries provide rapid lookup times for key lookup. They can also be used if you need to find items rapidly and retrieve data quickly. The keys in a dictionary can be any arbitrary key, not just an integer.

#### Tuples

Tuples are immutable and useful when the size of the collection and its object references do not change. Note that the underlying objects can be any arbitrary, mutable object. However, if you make a tuple with all immutable data like numbers and strings, it can represent data that should not change, like a banking transaction.

#### Sets

Sets are useful when you have collections of objects that are all unique and you need to perform set operations, like intersection and union. This is very helpful in many scenarios, such as removing duplicate items from a list.

## Memory and Data Storage

Python has a memory manager that handles how memory is allocated and deallocated, and garbage is collected.

### Stack memory

This part of memory grows when one function calls another function and shrinks as the functions return. Function calls and their local variables are usually stored in the stack. The stack can run out of room if functions make too many recursive calls.

### Heap memory

The rest of memory is called the heap and is where dynamic objects created by the program are stored. To help keep the heap from running out of room, the garbage collector keeps the heap area free of obsolete objects.

### Garbage collector

The garbage collector automatically handles memory deallocation and frees memory for reuse. The garbage collector removes an object when it detects that the object is no longer being used.

## Stacks and Queues
