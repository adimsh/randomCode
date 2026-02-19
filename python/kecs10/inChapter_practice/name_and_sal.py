#WAP to enter names of employees and their salaries as input and store them in a dictionary

my_dict = dict() # or we can simply do- {} instead of dict()
n = int(input("Enter number of employees: "))

for i in range(n):
    my_dict.update({
        input("Enter name of the employee: "): float(input("Enter salary of the employee: "))
    })
    # or just simply do:
    # name = input("Name: ")
    # salary = input("Salary: ")
    # my_dict[name] = salary

print(my_dict)