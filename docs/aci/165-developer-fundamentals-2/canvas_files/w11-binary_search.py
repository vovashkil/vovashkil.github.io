'''
This method will search for an item in a list of ascending order.
It will retur the index of the item if found, or -1 if not found.
'''
def binary_search(arr, search_value):
    # initialize the start and end of our loop, which will be updated as the search progresses
    start = 0
    end = len(arr) - 1

    # continue the loop as long as start is <= to end. If we "cross over", and the end is smaller
    # it will mean that we never found the item
    while start <= end:
        # split the search space in half, by getting the middle value between the current start and end
        middle = (start + end) // 2

        # if the search value is equal to the middle value, then we found it, so return the index
        if arr[middle] == search_value:
            return middle
        # else, if the search value is less than the middle value, update the end to look at the lower half
        elif arr[middle] < search_value:
            start = middle + 1
        # else, the search value is greater than the middle value, so update the start to look at the upper half
        else:
            end = middle - 1

    # if we get here, we never found the item, so return -1
    return -1

# Driver Code
if __name__ == '__main__':
    print("-------------------- Python Binary Search --------------------\n");

    # even numbers from 0 to 30
    even_arr = [0, 2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30]

    # Search for an even value, which will be in the list
    val = 14
    idx = binary_search(even_arr, val)
    # display message depending on search result
    if (idx == -1):
        print(f"FAIL   : {val} is NOT the array")
    else:
        print(f"SUCCESS: {val} is in the array")

    # Search for an odd value, which will not be in the list
    val = 17
    idx = binary_search(even_arr, val)
    # display message depending on search result
    if (idx == -1):
        print(f"FAIL   : {val} is NOT the array")
    else:
        print(f"SUCCESS: {val} is in the array")