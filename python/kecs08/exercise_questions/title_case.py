def title(the_string):
    return the_string.title()

print(title(input("Enter a string: ")))


#manual version

# def title_case_manual(the_string):
#     result = ""
#     capitalize_next = True

#     for i in the_string:
#         if i == " ":
#             result += i
#             capitalize_next = True
#         elif capitalize_next:
#             result += i.upper()
#             capitalize_next = False
#         else:
#             result += i.lower()

#     return result

# print(title_case_manual(input("Enter a string: ")))
