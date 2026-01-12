#a program to calculate compound interest given, Principal(P), rate of interest(r), time in years(t), number of times the interest is compounded(n)

def main():
    Prin = float(input("Enter the Principal amount: "))
    rate = float(input("Enter rate of interest(%): "))
    time = float(input("Enter time(in years): "))
    num = int(input("Enter number of times the interest is compounded(in one year): "))

    interest = calcCompInt(Prin, rate, time, num)
    Amount = Prin + interest
    
    print(f"Total Compound Interest: {interest}\nTotal Amount payable: {Amount}")

def calcCompInt(P, r, t, n): 
    r /= 100
    CI = P*((1 + r/n)**(n*t)-1)
    return CI

if __name__ == "__main__":
    main()