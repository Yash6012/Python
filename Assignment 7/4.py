# Question 4
def invert_dict(d):
    inverted = {}
    for k, v in d.items():
        inverted.setdefault(v, []).append(k)
    return inverted


my_dict = {"apple": 1, "banana": 2, "orange": 3, "pear": 4}
# print(len(my_dict))
# print(my_dict["apple"])
inverted_dict = invert_dict(my_dict)
print(inverted_dict)
