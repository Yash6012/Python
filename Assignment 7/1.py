# Question 1
# Creating the required function
def remove_keys(mydict, keylist):
    for i in range(0, len(keylist)):
        try:
            mydict.pop(keylist[i])
        except:
            print("The key", keylist[i], "is not present in the Dictionary")
    return mydict


# __main__
# initialising the dictionary and list
my_dict = {"Harry": 98, "Hermione": 95, "Ronald": 90, "Draco": 80, "Nevil": 85, "Dumbledore": 100, "Sirius": 90}
key_list = ["Snape", "Draco", "Nevil"]
print("The defined Dictionary is:", my_dict)
print("The keys which is to be removed are", key_list)
# Calling the function
result = remove_keys(my_dict, key_list)
# Printing the result dictionary
print(result)
