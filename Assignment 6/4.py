# Question 4
# Creating function for binary search
def b_search(my_list, key):
    initial = 0
    last = len(my_list) - 1
    while initial <= last:
        mid = (initial + last) // 2
        if my_list[mid] == key:
            return mid
        elif my_list[mid] < key:
            initial = mid + 1
        else:
            last = mid - 1
    else:
        return -1


# __main__
# printing the initial information
print("Program to search for index of an element using \"Binary Search\"")
li = [1, 9, 7, 8, 6, 5, 4, 2, 3]
li.sort()
print(li)
# taking input from user whose index is to be searched
x = int(input("Enter the number whose index you want to search in the above list: "))
result = b_search(li, x)
if result != -1:
    print("The element", x, "is present at ", result, "th index")
else:
    print("The element", x, "is not present in the List")
