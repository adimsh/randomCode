file_handle = open("hello.txt", "a")

to_write = [
    "Welcome my class\n",
    "It's a fun place\n",
    "You will learn and play"
]

file_handle.writelines(to_write)

file_handle.close
