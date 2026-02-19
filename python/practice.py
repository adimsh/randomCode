# WAP to count frequency of every element in a given list

lst = [4, 5, 5, 88, 97, 22, 3, 2, 4, 5, 87, 33, 22]
new_lst = []

for i in lst:
    if i not in new_lst:
        count = 0
        for x in lst:
            if x == i:
                count += 1
        print(i, "occurs", count, "times in the given list.")
        new_lst.append(i)

print(new_lst)

# we can do this using a dictionary, making the numbers key and the frequency as their values

new_dict = {}

for i in lst:
    if i in new_dict:
        new_dict[i] += 1
    else:
        new_dict[i] = 1

for i in new_dict:
    print(i, "occurs", new_dict[i], "times in the given list")

# we can do this in one line as well

print({x: lst.count(x) for x in lst}) # basically says for every x in lst i want data in this format: x: lst.count(x)