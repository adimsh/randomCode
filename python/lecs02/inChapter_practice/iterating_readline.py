#to read all the lines from the file- myfile.txt using an iterator and the getline() function

with open("myfile.txt", "r+") as file_handle:
    for line in file_handle:    # line iterates over each line in consecutive iterations
        print(line, end = '') # previously i did print(file_handle.readline()) which just skipped alternate lines as the line stored in 'line' iterator variable wasn't used


# other ways to do this iteration

# 1. using the while loop
# with open("myfile.txt", "r") as f:
#     line = f.readline()
#     while line:
#         print(line, end='')
#         line = f.readline()

# 2. using the getlines() to get a list of lines- inefficient
# with open("myfile.txt", "r") as f:
#     for line in f.readlines():
#         print(line, end='')
