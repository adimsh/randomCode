# create a dict of odd numbers where: key = numerals, value = spellings & perform the following operations-

# (a) Display the keys
# (b) Display the values
# (c) Display the items
# (d) Find the length of the dictionary
# (e) Check if 7 is present or not
# (f) Check if 2 is present or not
# (g) Retrieve the value corresponding to the key 9
# (h) Delete the item from the dictionary corresponding to the key 9

my_dict = {
    1: 'one',
    3: 'three',
    5: 'five',
    7: 'seven',
    9: 'nine'
}

# to display keys
for i in my_dict.keys():
    print(i, sep = " ")
print()

# to display values
for i in my_dict.values():
    print(i, sep = " ")
print()

# to display items
for i,j in my_dict.items():
    print("key- {}, value- {}".format(i, j))
print()

# to find length of dictionary
print("length of dictionary is- ", len(my_dict))
print()

# if 7 is present
if 7 in my_dict:
    print("7 is present in this dict")
else:
    print("7 is not present in this dict")
print()

# if 2 is present
if 2 not in my_dict:
    print("2 not in here brodi...")
else:
    print("there is indeed a 2 in there, good sir...")
print()

# retrive value corresponding to key 9
print("the value corresponding to the key value 9 is: ", my_dict.get(9))
print()

# delete item corresponding to key 9
del my_dict[9]
print(my_dict)