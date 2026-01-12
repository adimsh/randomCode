#To calculate amount payable at simple interest

prin = float(input("Enter Principal Amount:"))
rate = float(input("Enter Interest Rate(per annum):"))
time = float(input("Enter lending period(in years):"))

SI = prin*rate*time/100
amt = prin + SI

print("Total Payable Amount is:", amt)
