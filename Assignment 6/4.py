# Question 4
# Creating function for binary search
def b_search(my_list, key):
    print(my_list)
    low = 0
    high = len(my_list) - 1
    while low <= high:
        mid = (low + high) // 2
        if my_list[mid] == key:
            return mid
        elif my_list[mid] < key:
            low = mid + 1
        else:
            high = mid - 1
    else:
        return -1


li = [1, 9, 7, 8, 6, 5, 4, 2, 3]
li.sort()
result = b_search(li, 0)
if result != -1:
    print(f"Element is present at index {result}")
else:
    print("Element is not present in array")


