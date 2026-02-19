file_handle = open("hello.txt", "r")

for line in file_handle:
    print(line, end = "") # kyunki hr line ke end me pehle se ek \n character h...

file_handle.seek(0)
for line in file_handle.readlines():
    print(line, end = "")

file_handle.seek(0)
while True:
        a = file_handle.readline()
        print(a, end = "")
        if a == "":
            break