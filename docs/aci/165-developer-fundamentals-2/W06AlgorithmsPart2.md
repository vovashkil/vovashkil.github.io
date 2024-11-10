# Algorithms Part 2

* back to AWS Cloud Institute repo's root [aci.md](../aci.md)
* back to repo's main [README.md](../../../README.md)

## Sorting Algorithms

### Pre-assessment

#### Which sorting algorithm is relatively straightforward to understand and implement and provides a foundation to learn more advanced sorting algorithms?

* Bubble sort

Wrong answers:

* Quick sort
* Selection sort
* Merge sort

Bubble sort is relatively straightforward to understand and implement. However, because of low efficiency with larger data sets it is not often used. Yet, it is still introduced to new learners to help them understand the process of sorting in computation.

#### Which scenario guarantees the performance level of the algorithm will NOT drop below a certain level?

* Worst-case scenario

Wrong answers:

* Best-case scenario
* Average-case scenario
* Amortized-case scenario

The worst-case scenario guarantees the performance level won't drop below a certain level. The worst-case scenario occurs when the algorithm faces the most challenging input or condition.

#### What is the term for the time complexity when the algorithm's runtime remains constant and does NOT depend on the size of the input?

* Constant time complexity

Wrong answers:

* Linear time complexity
* Exponential time complexity
* Quadratic time complexity

In constant time complexity, even with the increase in the input, the time taken to complete the task is constant. The algorithm with constant time complexity is considered the most efficient and fastest of all.

### What is Sorting?

**Sorting** is the process of arranging items in a specific order. Libraries use sorting extensively to organize books. A library employs sorting to arrange books alphabetically by author, title, or subject. This helps library visitors to conveniently locate the books they are looking for. Imagine you walk into a library and want to find a book on a specific topic. Without sorting, finding a specific book would be very challenging.

In computer science, sorting puts elements of a list into a specified order. The most frequently used orders are ascending or descending. Efficient sorting is important for optimizing the efficiency of other algorithms that require input data to be in sorted lists.

### Sorting requirements

The output of any sorting algorithm must satisfy the following conditions: 

* Sorting must be done as per the prescribed order.
* The number of elements in the input and the number of elements in the output must be equal.

### Sorting Algorithms and Their Benefits

### Sorting algorithms

A sorting algorithm is a sequence of steps that sorts the elements in a list in the desired order. There are many different ways to sort a list, which is why there are different sorting algorithms. The following sorting algorithms will be covered in this topic: 

* Bubble sort
* Selection sort
* Insertion sort
* Merge sort
* Quicksort

### Benefits of sorting algorithms

There are four main purposes for using sorting algorithms when you are writing code. They are as follows:

* **Searching:** Searching for an item in the list is much more convenient and efficient when the list is sorted.
* **Selection:** Sorting helps you quickly select items from a list.
* **Finding duplicates:** Sorting helps to find duplicate entries in a list.
* **Analyzing distribution:** Analyzing the frequency distribution of items is more convenient when the list is sorted.

### Benefits of sorting with real-life examples

#### Searching

Finding a book in the library becomes more convenient because the books are sorted first by genre or theme, and then alphabetically.

#### Selection

A teacher can conveniently identify the highest or lowest scorer on a test if the answer sheets are sorted in ascending or descending order by score.

#### Finding duplicates

Sorting makes it more convenient to find out how many students in the class have the same name.

#### Analyzing distribution

Sorting students in the class according to their favorite subject helps to analyze how many students prefer one subject over another subject.

### Knowledge Check

#### What is the primary purpose of sorting algorithms in computation?

* Facilitating efficient searching and selection

Wrong answers:

* Enhancing code readability
* Optimizing memory allocation
* Minimizing code complexity

Sorting algorithms are used to organize data in a specific order, making it more convenient to search for items and quickly select them from the sorted list.

#### Which benefit does sorting provide for analyzing the frequency distribution of items?

* Convenient identification of repeated entries

Wrong answers:

* Improved code performance
* Enhanced code maintainability
* Streamlined code debugging

Sorting facilitates the identification of repeated entries in a list of items.

#### Which requirements must be fulfilled during the sorting process? (Select TWO.)

* The number of elements in the input and output must be equal.
* Sorting must be done as per the prescribed order.

Wrong answers:

* The number of elements in the output must be greater than those in the input.
* Sorting must be done using for-loops.
* The number of elements in the output must be less than those in the input.

This ensures that the sorting process does not alter the number of elements and orders those elements as specified.

### Summary

* Describe the characteristics of sorting.
* Identify the two conditions of sorted output.
* Describe the benefits of sorting.

## Built-in sorting algorithms

There are two built-in algorithms for sorting in Python. These algorithms are **sort()** and **sorted()**.

### The sort() method

The characteristics of the sort() method are as follows:

* sort() is a method in the list class in Python.
* sort() is used to sort the elements in the list.
* sort() sorts the list in place, so it modifies the original list.
* sort() returns None, because it modifies the original list.

#### Sorting in reverse order

sort(reverse=True)

#### Sorting by length

sort(key=len)

The **sort()** method can accept an optional **key** parameter to specify how to sort the elements in the list. You can pass in a function like the **len()** function that is used in this example with **key=len**. The function specified as the key will be called on each element in the list, and the value returned from the function will be used to compare and sort the elements. In this case, the string lengths returned from calling **len()** on each element are being used as the sort key to compare and sort the strings.

### The sorted() function

The characteristics of the sorted() function are as follows:

* sorted() is a built-in function in Python.
* sorted() is used for sorting any iterable, such as lists, tuples, and strings.
* sorted() creates a new list. It does not modify the original iterable.
* sorted() returns the new sorted **list** even the input is tuples or strings.

#### Sorting with lambdas

In case you're needing to sort by two keys: First, you need to sort the strings by their length, and then by alphabetical order if the string lengths are equal. The **key** parameter can only accept one function argument.

You can use a lambda function as your key. This allows you to write a custom function that returns one or more custom values to sort by, such as both string length and alphabetical order

```
string_list = ["apple", "orange", "banana", "grape", "kiwi"]
print("Input list of strings before sorting:")
print(string_list)

# Sorting the list using sorted function with a lambda function
sorted_strings = sorted(string_list, key=lambda x: (len(x), x))
print("Sorted list of strings based on their length:")
print(sorted_strings)
```

Expected output

```
Input list of strings before sorting:
['apple', 'orange', 'banana', 'grape', 'kiwi']

Sorted list of strings based on their length:
['kiwi', 'apple', 'grape', 'banana', 'orange']
```

Notice that the strings for "orange" and "banana" each have the same length of six characters. However, the lambda function sorts "banana" before "orange" because "banana" comes before "orange" in alphabetical order.

Unlike the sort() method, which can only be called on lists, the sorted() method can be called on any iterable. This includes calling it directly on strings.

### Knowledge Check

#### What is the purpose of the Python list sort() method? 

* To sort elements in place

Wrong answers:

* To create a new list
* To modify the original iterable
* To return a new sorted list

The **sort()** method is used to sort the elements in the list in place, which means it modifies the original list.

#### What value does the sort() method return after sorting the elements in the list?

* None

Wrong answers:

* New sorted list
* Original list
* Length of the list

The **sort()** method modifies the original list in place and returns **None**.

#### Which of the following statements is true?

* The sorted() function creates a new list.

Wrong answers:

* The sort() method creates a new list.
* The sorted() function modifies the original list.
* The sorted() function returns nothing.

The **sorted()** function creates a new list from an iterable, and it returns the new sorted list.

### Summary

* Describe the Python **sort()** method and its application for sorting data.
* Describe the Python **sorted()** function and its usage for sorting data.
* Identify the differences between the **sort()** method and the **sorted()** function.

## Importance of algorithm analysis

The goal of algorithm analysis is to forecast the performance of an algorithm without the need for actual implementation. Predicting the precise behavior of an algorithm is challenging due to various influencing factors. However, algorithm analysis can help to predict the approximate behavior of an algorithm.

Algorithm analysis provides two primary benefits:

* Firstly, when you focus on prediction rather than running the algorithm for every conceivable input type and size, it conserves time and effort. This approach avoids the necessity of implementing the algorithm each time you modify the input.
* Secondly, algorithm analysis empowers you to make informed decisions regarding which algorithm to use in a particular problem-solving scenario.

For analyzing the algorithm, you conduct a performance analysis based on external and internal factors.

### External Factors

In the analysis of external factors, elements to consider include response time, throughput, resource utilization, the efficiency of the compiler, and the overall effectiveness of the system. The outcome of this evaluation depends on how well the system can run the algorithm. External factors are variables influenced by machine configurations and the proficiency of compilers.

External factors can change based on how the machine is set up and how good the compiler is at its job. Considering external factors means checking how well the whole computer setup works with the algorithm to get the job done.  

### Internal Factors

Internal factors examine how much time and space an algorithm needs to get a job done. 

1. **Time complexity:** This is about figuring out how fast the algorithm can complete its task. You want to know how many operations it needs to complete and how long each operation takes.
2. **Space complexity:** This is about understanding how much memory (space) the algorithm requires while it's performing its task. You want to know how efficiently it uses computer memory.

The internal analysis examines the algorithm itself. You're not thinking about the outside world or the computer it's running on; you're just focused on the algorithm's characteristics. It's a bit like looking at how well a car engine runs without considering the road or traffic—it's all about what's happening inside the engine.

### Complexity analysis

#### Time complexity

Time complexity estimates the amount of time an algorithm takes to complete as the input size grows bigger.

#### Space complexity

Space complexity estimates the amount of memory an algorithm takes to complete as the input size grows bigger.

Both time and space complexities are often expressed using Big-O notation.

These complexities are used to describe the performance of an algorithm under different conditions, or scenarios.

The following are three different scenarios to consider when analyzing time and space complexities:

* Best case
* Worst case
* Average case

### Best, worst, and average case example

#### Best Case

The best-case scenario refers to the minimum amount of resources (in terms of time and space) that an algorithm requires to solve a problem under ideal conditions. It represents the most favorable input for the algorithm, where it performs optimally. Best-case time complexity provides a lower bound on the algorithm's efficiency.

#### Worst Case

The worst-case scenario represents the maximum amount of resources an algorithm might need to solve a problem. It occurs when the algorithm faces the most challenging input or condition. Worst-case time complexity provides an upper bound on the algorithm's efficiency.

#### Average Case

The average-case scenario considers the expected performance of an algorithm when applied to a random or typical input. It provides a more realistic measure of efficiency than best-case or worst-case alone. Average-case time complexity is often more complex to analyze and might involve probabilities.

### Computational example

Take the linear search algorithm as an example, where the task is to find a particular element within an unsorted array.

Consider the array: [2, 7, 6, 5, 8, 9, 3].

In the **worst-case scenario**, searching for the target 3 would be the most time-consuming, given it is placed at the end of the array. Every single element in the array must be checked before finding the target.

Conversely, the **best-case scenario** occurs when the target is 2, which is positioned at the beginning of the array. Only one element had to be checked before finding the target.

For the **average case**, imagine searching for the target 5, which is in the middle of the array. About half of the elements must be checked before finding the target.

When describing the time complexity of an algorithm, it usually means the worst-case scenario. This is because the worst-case scenario guarantees that the time required to complete the function will not be more than the worst case. This way, you know that the performance of the algorithm won't drop below a certain level.

### Knowledge Check

#### What are the two main advantages of algorithm analysis?

* Save time and effort during implementation and make informed algorithmic choices.

Wrong answers:

* Save time and effort during implementation and improve system proficiency.
* Predict exact algorithm behavior and make informed algorithmic choices.
* Improve the proficiency of the system and analyze internal factors affecting performance.

An algorithm analysis helps save time and effort during actual implementation. It also assists in making informed decisions about which algorithm to use in a particular problem-solving scenario.

#### What is the best-case scenario in terms of algorithm complexity analysis?

* The algorithm performs optimally.

Wrong answers:

* The algorithm faces the most challenging input.
* The algorithm's efficiency provides an upper bound.
* The algorithm's efficiency is more realistic.

The best-case scenario refers to the minimum number of resources, in terms of time and space, that an algorithm requires to solve a problem under ideal conditions. It represents the most favorable input for the algorithm, where it performs optimally.

#### During the performance analysis of an algorithm, the team evaluates the response time, throughput, and overall effectiveness of the system. Which aspect of algorithm analysis is this focusing on?

* External factors

Wrong answers:

* Internal factors
* Time complexity
* Space complexity

The team is focusing on external factors because they are assessing elements such as response time, throughput, and overall system effectiveness. These factors are influenced by machine configurations and the proficiency of compilers, making them external to the inherent characteristics of the algorithm itself.

### Summary

* Identify the internal and external factors that influence the performance of algorithms.
* Understand time and space complexities to evaluate algorithm efficiency.
* Understand the best-case, worst-case, and average-case scenarios for analyzing time and space complexities.

## Big O Notation

