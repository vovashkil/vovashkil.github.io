using System;

class BinarySearch {
    // Returns index of val if it is present in arr[].
    int binarySearch(int [] arr, int search_value)
    {
        // initialize end and start values for the search
        int start = 0;
        int end = arr.Length - 1;

        // search until end is smaller then start
        while (start <= end) {
            // calculate middle value between end and start
            int middle = (start + end) / 2;

            // Check if val is found at middle
            if (arr[middle] == search_value)
                return middle;

            // If val greater, update to search upper half
            else if (arr[middle] < search_value)
                start = middle + 1;

            // If val is smaller, update to search starter half
            else
                end = middle - 1;
        }

        // If we reach here, then vale was not present
        return -1;
    }


    // Driver code
    public static void Main()
    {
        Console.WriteLine("-------------------- C# Binary Search --------------------\n");

        int val, idx;

        // even numbers from 0 to 30
        int [] even_arr = {0, 2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30};

        // create binary search class
        BinarySearch binSearch = new BinarySearch();

        // Search for an even value, which will be in the list
        val = 14;
        idx = binSearch.binarySearch(even_arr, val);
        // display message depending on search result
        if (idx == -1)
            Console.WriteLine("FAIL   : " + val + " is NOT the array");  
        else
            Console.WriteLine("SUCCESS: " + val + " is in the array");  

        // Search for an odd value, which will not be in the list
        val = 17;
        idx = binSearch.binarySearch(even_arr, val);
        // display message depending on search result
        if (idx == -1)
            Console.WriteLine("FAIL   : " + val + " is NOT the array");  
        else
            Console.WriteLine("SUCCESS: " + val + " is in the array");  
    }
}
