# Write a program to accept string/sentences from the user till the user enters “END” to. Save the data in a text
# file and then display only those sentences which begin with an uppercase alphabet

with open("jus_anotha_file.txt", "w+") as d_file:
    while True:
        print("TO EXIT, ENTER 'END'")
        a_string = input("Enter a string >> ")
        d_file.write(a_string + "\n")
        if a_string.upper() == "END":
            break

    d_file.seek(0)
    for line in d_file:
        if line[0:1].isupper():
            print(line, end = "")

# gemini:

# # Step 1: Input and Save
# with open("data.txt", "w") as f:
#     while True:
#         line = input("Enter a sentence (type 'END' to finish): ")
#         if line.upper() == "END":
#             break
#         f.write(line + "\n")

# # Step 2: Read and Filter
# print("\nSentences starting with an Uppercase letter:")
# with open("data.txt", "r") as f:
#     for sentence in f:
#         # Check the first character of the string
#         if sentence[0].isupper():
#             print(sentence.strip())