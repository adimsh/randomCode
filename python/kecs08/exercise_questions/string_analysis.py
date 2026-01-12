the_string = input("Enter text: ")

total_char = len(the_string)

alpha_count = 0
digit_count = 0
ws_count = 0
sc_count = 0

for i in the_string:
    if i.isalpha():
        alpha_count += 1
    elif i.isdigit():
        digit_count += 1
    elif i.isspace():
        ws_count += 1
    else:
        sc_count += 1

word_count = len(the_string.split())

print(
    f"Analysis:\n"
    f"Total characters- {total_char}\n"
    f"Total alphabets- {alpha_count}\n"
    f"Total digits- {digit_count}\n"
    f"Total special symbols- {sc_count}\n"
    f"Total words- {word_count}"
)

