#Print all natural numbers upto 5 except 3 using loops

for i in range(5):
    if i+1 == 3:
        continue
    print(i+1)