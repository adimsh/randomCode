# using the readlines() fun to return a list of string object(each string is a line from the file with the \n character at the end)
# also converting this list of lines into a list of words...

with open("myfile.txt", "r+") as f:
    line_list = f.readlines()
    print(line_list)

    word_list = []
    for line in line_list:
        x = line.split() # It automatically ignores leading/trailing whitespace, including \n, if we want to include \n we can use split(' ')
        word_list.extend(x)
    print(word_list)


# a much more elegant solution--------
# with open("myfile.txt", "r") as f:
# word_list = [word for line in f for word in line.split()]
# print(word_list)

