# taking a string as input, writing it to a textfile and then reading it from that file and printing it as output

# taking the string input
inp = input("Enter a string...\n")

# opening/creating the file in read, write mode
file_obj = open("newfile.txt", "w+")

# writing in the file
file_obj.write(inp)
file_obj.seek(0)

# reading from the file
content = file_obj.read()

# printing the file contents
print(content)

#closing the file
file_obj.close()