with open("inputfile.txt", "w+") as my_obj:
    while True:
        inp_line = input("Enter a line to add to the file: ")
        my_obj.write(inp_line) # the input doesn't add a newline character at the end, so everything is written in a single line in the file
                                # to tackle this we can simply do: my_obj.write(inp_line + "\n" )
        cont = input("Do you wish to enter more data(y/n): ")
        if cont.lower() == 'n':
            break

another_obj = open("inputfile.txt", "r+")
for i in another_obj: # due to the abovementioned reason this loop only runs once, since the iterator stops at a new line and there is no new line in the text file we create
    print(i)

x = another_obj.read()
print(x)