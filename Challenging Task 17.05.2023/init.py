# Challenging Task
# Defining the function to sort


def bubble_sort(arr):
    n = len(arr)
    # Traversing all the array elements
    for _ in range(n - 1):
        # Last _ elements are already in place
        for i in range(n - _ - 1):
            # Swap if the element found is greater than the next element
            if arr[i] > arr[i + 1]:
                arr[i], arr[i + 1] = arr[i + 1], arr[i]


# __main__
print("Program to print second largest number in a list")
# Defining a list
num = [5, 2, 8, 8, 9, 1, 1, 7, 3, 4, 6]
# Printing the desired output
print("The List is:", num)
modified_num = list(set(num))
print("Removing the duplicate elements from the list", modified_num)
bubble_sort(modified_num)
print("Sorted list:", modified_num)
print("The second largest number in a list is:", modified_num[-2])
