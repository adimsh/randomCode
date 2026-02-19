# Write a program to input your friends’ names
# and their Phone Numbers and store them in the
# dictionary as the key-value pair. Perform the
# following operations on the dictionary:

# a) Display the name and phone number of all your
# friends
# b) Add a new key-value pair in this dictionary and
# display the modified dictionary
# c) Delete a particular friend from the dictionary
# d) Modify the phone number of an existing friend
# e) Check if a friend is present in the dictionary or
# not
# f) Display the dictionary in sorted order of names

my_dict = dict()
n = int(input("Enter total number of friends: "))

for i in range(n):
    name = input(f"Enter name {i + 1}: ")
    my_dict[name] = int(input("Enter phone number: "))

# a)
for key, value in my_dict.items():
    print("Name - {}\tPhone no. - {}".format(key, value))

# b)
new = input("Enter a new name: "), int(input("Enter phone no: "))
my_dict[new[0]] = new[1]
print(my_dict)

# c)
remove = input("Enter name of the friend to delete: ")
try:
    del my_dict[remove]
except KeyError:
    print("no one named", remove, "in the dict")
print(my_dict)

# d)
# minor bug- if the friend doesn't exist, this creates a new friend...
modify = input("Enter the name of friend whose number is to be changed: ")
my_dict[modify] = int(input("Enter the new number: "))
print(my_dict)

# e)
check = input("Enter a name to check presence: ") 
if check in my_dict:
    print("The mans in here brodi...")
else:
    print("He ain't here frfr")

# f)
sorted_dict = dict(sorted(my_dict))
print(sorted_dict)