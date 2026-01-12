def calcDiscount(bill: float):

    if 500 <= bill < 1000: #range(won't work for float values)
        shrink_factor = 0.95
    elif 1000 <= bill < 2000:
        shrink_factor = 0.92
    elif bill >= 2000:
        shrink_factor = 0.9
    else:
        shrink_factor = 1.0
        print(f"Shop for {500-bill} more to get a discount!")
    
    while True:
        is_member = input("Are you a member? (Y/N)\n")
        if is_member in "yYnN":
            break
        else:
            print("Invalid input\n")

    if is_member in 'yY':
            shrink_factor *= 0.95

    return bill*shrink_factor

print(calcDiscount(float(input("Enter shopping amount: "))))

#exam friendly approach: 

# def calcDiscount(bill):
#     if bill >= 2000:
#         factor = 0.90
#     elif bill >= 1000:
#         factor = 0.92
#     elif bill >= 500:
#         factor = 0.95
#     else:
#         factor = 1.0

#     member = input("Are you a member? (Y/N): ")
#     if member in "yY":
#         factor *= 0.95

#     discount = bill - bill * factor
#     net = bill * factor

#     print("Discount:", discount)
#     print("Net Payable Amount:", net)


# calcDiscount(float(input("Enter shopping amount: ")))
