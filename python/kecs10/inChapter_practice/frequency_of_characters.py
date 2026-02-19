# WAP to count the number of times a character appears in a given string

d_str = input("Enter a string: ")
freq_dict = {} # keys are the character and values are there count

for i in d_str: # checks if it's the first occurence of this char in d_str
    if i in freq_dict:
        freq_dict[i] += 1
    else:
        freq_dict[i] = 1
    # or we can do-
    # for i in d_str:
    # freq_dict[i] = freq_dict.get(i, 0) + 1


print(freq_dict)

