# Write a Python program to create a dictionary from a string.

inp_str = input("Enter a string: ")

freq_dict = {} # the character is key and the frequency of that character(in the given string) is the value

for ch in inp_str:
    if ch in freq_dict:          # to collapse this logic ladder in a single, more efficient if statement-
        freq_dict[ch] += 1       # for ch in inp_str:
    else:                           # freq_dict[ch] = freq_dict.get(ch, 0) + 1
        freq_dict[ch] = 1
    
print(freq_dict)