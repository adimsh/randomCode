#To input a list of unknown size

n = int(input("How many items do you want to add? "))
my_list = []

for i in range(n):
    raw_val = input(f"Enter element {i+1}: ")
    try:
        # Try making it an int first
        item = int(raw_val)
    except ValueError:
        try:
            # If that fails, try making it a float
            item = float(raw_val)
        except ValueError:
            # If both fail, it stays a string
            item = raw_val
    my_list.append(item)

print (my_list)
