# import io # the open() function is basically an alias for the io.open() function in python3
            # (both return same file object types- _io.TextIOWrapper or BufferedReader depending on the access mode- b/t) but open() is built-in and preferred

# file_object = open("hello", "w")
# print(type(file_object))

# with open("hello") as message: # message is the file object(file handle) here
#     content = message.read()
#     print(content)


with open("myfile.txt", "w+") as my_obj:
    lines = ["This is the first line\n", "This is the second line\n", "This is the last line"]
    my_obj.writelines(lines)

    my_obj.seek(0)
    a = my_obj.read(10)
    my_obj.seek(0)
    b = my_obj.readlines(10)
    my_obj.seek(0)
    c = my_obj.readline(10)
    my_obj.seek(0)
    d = my_obj.read(-1)
    my_obj.seek(0)
    e = my_obj.readline()
    my_obj.seek(0)
    f = my_obj.readlines()
    print(a, b, c, d, e, f, sep = "\n")