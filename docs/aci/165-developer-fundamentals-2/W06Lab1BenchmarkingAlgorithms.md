# Benchmarking Your Algorithms

## Lab overview

This lab gives you hands-on experience in benchmarking the performance of sort algorithms. You learn how to create a benchmark function, generate input data, and interpret the benchmark results.

Objectives
By the end of this lab, you should be able to do the following:

Build a function to benchmark the time performance of sort algorithms.
Generate ordered, random, and reverse ordered input data for the benchmark.
Run the benchmark and print out the results.
Compare the time performance of sort algorithms for different types of data.
Technical knowledge prerequisites
This hands-on lab assumes that you have completed the Developer Fundamentals 1 (DF1) course and the associated labs.

Duration
This lab requires approximately 2 hours to complete.

Icon key
Various icons are used throughout this lab to call attention to different types of instructions and notes. The following list explains the purpose for each icon:

 Command: A command that you must run
 Expected output: A sample output that you can use to verify the output of a command or edited file
 Note: A hint, tip, or important guidance
 Hint: A hint to a question or challenge
 Task complete: A conclusion or summary point in the lab
Start lab
To launch the lab, at the top of the page, choose Start lab.

 Caution: You must wait for the provisioned AWS services to be ready before you can continue.

To open the lab, choose Open Console .

You are automatically signed in to the AWS Management Console in a new web browser tab.

 Warning: Do not change the Region unless instructed.

Common sign-in errors
Error: Choosing Start Lab has no effect
In some cases, certain pop-up or script blocker web browser extensions might prevent the Start Lab button from working as intended. If you experience an issue starting the lab:

Add the lab domain name to your pop-up or script blocker’s allow list or turn it off.
Refresh the page and try again.
AWS services used in this lab
AWS Cloud9
AWS Cloud9 is a cloud-based integrated development environment (IDE) that offers a rich code editing experience with support for several programming languages and runtime debuggers. It has a built-in terminal. It contains a collection of tools that you use to code, build, run, test, and debug software, and it helps you release software to the cloud.

Task 1: Establish the development environment
In this task, you connect to the AWS Cloud9 IDE.

To open the AWS Cloud9 environment, copy the Cloud9Environment URL value that is listed to the left of these instructions, and paste it into a new browser tab.

 Expected output: A new browser tab opens and displays the AWS Cloud9 IDE.

 Task complete: You have successfully connected to the AWS Cloud9 IDE.

Task 2: Write the benchmark function
In this task, you write the benchmark_sort() function, which is used to benchmark sort algorithms. Then you test the function by using it to benchmark Python’s built-in sorted() function.

Task 2.1: Calculate the time it takes for an algorithm to run
Open the benchmark_sort.py file, which contains the benchmark_sort() function.

Take a moment to inspect the benchmark_sort() function. Be sure to read the comments within the function to understand what it does, what are its parameters, and what it prints.

 Note: To help you navigate the following coding tasks, the task numbers are listed within the file’s code comments. Use the comments as a step-by-step guide on how to write your code.

Add code to track the start time and end time when a sort algorithm runs.
 Hint: To find the start and end times, use Python’s time library, which is imported at the top of the file.


for i in range(num_iterations):

    ## Task 2.1

    # Create a copy of the input data, because you do not want to overwrite it.

    # Store the start time.

    # Perform sort on the copy of the input data.

    # Store the end time.
To see the solution code, expand this section.
Add code to calculate the time taken for sorting, and print the result.

# Calculate the time taken for sorting.

# Print the current iteration's number and the duration taken for sorting.
To see the solution code, expand this section.
Task 2.2: Track the fastest, slowest, and total time
In this task, you track the fastest and slowest times that it takes to run a sorting algorithm. By tracking the fastest and slowest times, you can see how wide of a range exists within the test results.

Add code to track the fastest and slowest times.

## Task 2.2

# Update the fastest time.

# Update the slowest time.
To see the solution code, expand this section.
Add code to track the total time. This tracks the cumulative time across all iterations that have ran. This will be used later to calculate the average time.

# Update the total time.
To see the solution code, expand this section.
Task 2.3: Calculate the average time
Add code to calculate the average time. Then print the results for fastest time, slowest time, and average time.
 Hint: Remember to write your code outside of the for loop.


## Task 2.3

# Calculate the average time.

# Print the results for fastest time, slowest time, and average time.
To see the solution code, expand this section.
From the File menu, choose Save.

 Command: Run the following command in the bash terminal:


python benchmark_sort.py
 Expected output: Your time results might not be exactly the same as the time results in the expected output, because the time to run a function also depends on external factors such as randomly generated input data and system resource load.


Sort benchmark for 10000 elements and 10 iterations:
--------------------------------------------------
Iteration 1 took: 0.002575 seconds
Iteration 2 took: 0.002572 seconds
Iteration 3 took: 0.001544 seconds
Iteration 4 took: 0.001549 seconds
Iteration 5 took: 0.001538 seconds
Iteration 6 took: 0.001024 seconds
Iteration 7 took: 0.001028 seconds
Iteration 8 took: 0.000515 seconds
Iteration 9 took: 0.001025 seconds
Iteration 10 took: 0.001020 seconds
--------------------------------------------------
Fastest time: 0.000515 seconds
Slowest time: 0.002575 seconds
Average time: 0.001228 seconds
Although you ran the benchmark_sort() function, you haven’t actually benchmarked the implemented algorithms in this lab yet. You’ve only benchmarked Python’s built-in sorted() function with randomly generated input data. You can see this if you inspect the if __name__ == "__main__": section at the end of the file.

In the next task, you run the benchmark for the actual algorithms contained in the lab files, such as bubble_sort.py, merge_sort.py, quick_sort.py, etc.

 Task complete: You have successfully written and ran the benchmark function.

Task 3: Benchmark the sort algorithms
In this task, you write code in the benchmark.py file to test the various sort algorithms. First, you generate three sets of input data: ordered, random, and reverse ordered. After that, you call the benchmark_sort() function to benchmark the sort algorithms with each type of input data.

To better understand the source code for the sort algorithms used in this benchmark, you can inspect their files, such as bubble_sort.py, insertion_sort.py, selection_sort.py, merge_sort.py, and quick_sort.py.

Task 3.1: Generate the input data
Open the benchmark.py file.

Take a moment to inspect the code and comments. At the top of the file, all the functions and libraries that you will use have already been imported.

 Note: To help you navigate the following coding tasks, the task numbers are listed within the file’s code comments. Use the comments as a step-by-step guide on how to write your code.

Find the line with the comment # Generate the ordered sample.

 Note: You can also press Ctrl+F on Windows or Cmd+F on macOS to search for the line.

Add code that will generate a list of 10,000 ordered integers.

 Hint: The sample size has already been set in the sample_size variable. How can you use this variable to generate the ordered sample?


## Task 3.1

# Generate the ordered sample.
To see the solution code, expand this section.
Add code that will generate a list of 10,000 random integers.
 Hint: The random module has already been imported. It has a function random.randint(), which takes two parameters and generates a random integer between the two parameters inclusively.


# Generate the random sample.
To see the solution code, expand this section.
Add code that will generate a list of 10,000 reverse ordered integers.
 Hint: Use Python’s reversed() method, which takes a single argument.


# Generate the reverse ordered sample.
To see the solution code, expand this section.
Task 3.2: Benchmark results
Now that the input data is ready, continue to work in the benchmark.py file to write the code that calls the benchmark_sort() function with each of the sort algorithms. The benchmark_sort() function and the sort algorithms have already been imported.

Add code that calls the benchmark_sort() function, which takes three parameters: sort_func, input_data, and num_iterations. Call the function once for each type of input data, and pass bubble_sort as its argument.

## Task 3.2

print("Bubble sort\n")
print("Benchmark with ordered sample:")
# Call benchmark_sort with ordered sample.

print("\nBenchmark with random sample:")
# Call benchmark_sort with random sample.

print("\nBenchmark with reverse ordered sample:")
# Call benchmark_sort with reverse ordered sample.

print("End of bubble sort\n")
To see the solution code, expand this section.
Add code to repeat this block of print statements for each of the remaining sort algorithms: insertion_sort, selection_sort, merge_sort, and quick_sort.
To see the solution code, expand this section.
From the File menu, choose Save.

 Command: Run the following command in the bash terminal:


python benchmark.py
 Expected output: The benchmark runtime can take approximately 5 minutes. Your time results might not be exactly the same as the time results in the expected output, because the time to run a function also depends on external factors such as randomly generated input data and system resource load.


Bubble sort

Benchmark with ordered sample:

Sort benchmark for 10000 elements and 5 iterations:
--------------------------------------------------
Iteration 1 took: 6.123645 seconds
Iteration 2 took: 6.100205 seconds
Iteration 3 took: 5.918229 seconds
Iteration 4 took: 5.662011 seconds
Iteration 5 took: 5.604882 seconds
--------------------------------------------------
Fastest time: 5.604882 seconds
Slowest time: 6.123645 seconds
Average time: 5.881794 seconds

Benchmark with random sample:

Sort benchmark for 10000 elements and 5 iterations:
--------------------------------------------------
Iteration 1 took: 10.148934 seconds
Iteration 2 took: 10.429871 seconds
Iteration 3 took: 10.238776 seconds
Iteration 4 took: 10.995737 seconds
Iteration 5 took: 10.347384 seconds
--------------------------------------------------
Fastest time: 10.148934 seconds
Slowest time: 10.995737 seconds
Average time: 10.432140 seconds

Benchmark with reverse ordered sample:

Sort benchmark for 10000 elements and 5 iterations:
--------------------------------------------------
Iteration 1 took: 15.156157 seconds
Iteration 2 took: 13.569572 seconds
Iteration 3 took: 13.386972 seconds
Iteration 4 took: 13.719311 seconds
Iteration 5 took: 13.991776 seconds
--------------------------------------------------
Fastest time: 13.386972 seconds
Slowest time: 15.156157 seconds
Average time: 13.964758 seconds

Note: The print outputs will continue for the subsequent benchmarks of the other sort functions.
 Task complete: You have successfully written and ran the benchmark.

Task 4: Compare the benchmark results
In this task, you analyze the benchmark results that were printed out in the AWS Cloud9 terminal. To have a larger viewing space to read the results, you can expand the terminal vertically.

Compare the average times that it took the different algorithms to sort ordered, random, and reverse ordered data. For ease of comparison, you can track the results by manually recording them separately in a table format.

The following table is an example that shows the average time (in seconds) that it took for the algorithms to sort different data. Your time results might not be exactly the same as the time results in the table, but the relative performance patterns across different algorithms and input data types should be consistent with the expected results.

Algorithm	Ordered	Random	Reverse Ordered
bubble sort	5.900815	10.099952	13.560792
insertion sort	0.002762	4.824154	9.240840
selection sort	4.501341	4.376793	4.500488
merge sort	0.026757	0.049737	0.033277
quick sort	5.786818	0.025252	5.665889
For each algorithm, think about how its time performance differs based on the type of input data. Notice that this difference varies more drastically for some algorithms than for others. Here are some questions to think about:

Which algorithms show significant performance time increases when going from ordered to random and then to reverse ordered data?

Which algorithms show relatively little difference in performance across the various input data types?

Do the benchmark results support what you have learned about regarding the big O time complexities of the various sort algorithms?

 Task complete: You have compared and analyzed the results from the benchmark.

Conclusion
 Congratulations! You now have successfully done the following:

Built a function to benchmark the time performance of sort algorithms.
Generated ordered, random, and reverse ordered input data for the benchmark.
Ran the benchmark and printed out the results.
Compared the time performance of sort algorithms for different types of data.
End lab
Follow these steps to close the console and end your lab.

Return to the AWS Management Console.

At the upper-right corner of the page, choose AWSLabsUser, and then choose Sign out.

Choose End lab and then confirm that you want to end your lab.

For more information about AWS Training and Certification, see https://aws.amazon.com/training/.

Your feedback is welcome and appreciated.
If you would like to share any feedback, suggestions, or corrections, please provide the details in our AWS Training and Certification Contact Form.