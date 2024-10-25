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