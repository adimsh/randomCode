#count number of times an element occurs in a list

my_list = [45, 32, 40, 123, 121, 43, 45, 67, 420, 6969, 45]

#counting 45s
count = 0
for i in my_list:
    if(i == 45):
        count += 1
print("45 appears", count, "times in", my_list)

#alternatively we can also just use the count() function
print(my_list.count(45))