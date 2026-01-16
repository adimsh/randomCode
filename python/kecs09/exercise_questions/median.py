# to find median of n numbers(list input from user)

data_set = []
n = int(input("Enter number of elements: "))
for i in range(n):
    item = int(input(f"Enter element {i + 1}: "))
    data_set.append(item)

sorted_data_set = sorted(data_set)

# to find median
if not data_set:
    print("EMPTY LIST. Median doesn't exist.")
elif n % 2 != 0:
    median = sorted_data_set[((n+1)//2) - 1]
else:
    median = (sorted_data_set[(n//2) - 1] + sorted_data_set[n//2])/2

print("Median is:", median)

