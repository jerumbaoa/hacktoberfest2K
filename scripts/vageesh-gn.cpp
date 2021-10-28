// A C++ Program To Print the sum of the elements of an Array

#include <iostream>

int main()
{
    // Creating an Integer Array
    int arr[] = {
        1,
        4,
        2,
        3,
        5,
        6,
        3,
        6,
        5,
        4,
    };
    // Storing the length of the array in the variable len
    int len = sizeof(arr) / sizeof(arr[0]);
    // Initializing the sum as 0 which will be incremented
    // by element present in the array once the following loop starts
    int sum = 0;

    // A Loop to iterate through the given array
    for (int i = 0; i < len; i++)
    {
        // Incrementing the value of the sum with the element found from the array
        sum += arr[i];
    }

    // Printing the sum of the elements of the Array
    std::cout << "The sum of the elements in the given array is: " << sum << std::endl;
}