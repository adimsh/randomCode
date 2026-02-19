# Write a program to enter the following records in a binary file:
# Item No		integer
# Item_Name     string
# Qty			integer
# Price		    float
# Number of records to be entered should be accepted from the user. 

# Read the file to display the records in the
# following format:
# Item No:
# Item Name : 		
# Quantity:
# Price per item:
# Amount:		( to be calculated as Price * Qty)
import pickle

num = int(input("Enter number of items: "))
items = list()
for i in range(num):
    Item_no = int(input(f"Enter item number for item {i + 1}: "))
    Item_name = input("Enter item name: ")
    Qty = int(input("Enter item quantity: "))
    Price = float(input("Enter item cost: "))
    item_info = [
        Item_no,
        Item_name,
        Qty,
        Price
    ]
    items.append(item_info)
    print()

# Pickling the info
with open("item_inventory.dat", "wb") as fh:
    pickle.dump(items, fh)  # dumping the entire data like this is discouraged due to it's size (if there are a lot of items)
                            # instead we should dump each record seperately (we would be able to access them seperately as well)

# Unpickling the info and displaying output
with open("item_inventory.dat", "rb") as fh:
    print("ITEM INFO-")
    t_amount = 0
    listx = pickle.load(fh)
    for info in listx:
        print(
            "Item No-", info[0], "\n"
            "Item Name-", info[1], "\n"
            "Qty- ", info[2], "\n"
            "Price(per unit)- ", info[3], "\n"
            "Amount", info[2] * info[3], "\n"
        )
        t_amount += info[2] * info[3]
    print("Grand total- ", t_amount)



# Ai version

# import pickle

# def binary_operations():
#     # 1. Writing to the file
#     try:
#         with open("records.dat", "wb") as f:
#             n = int(input("How many records do you want to enter? "))
#             for i in range(n):
#                 print(f"\nEntering details for Item {i+1}:")
#                 item_no = int(input("Item No: "))
#                 name = input("Item Name: ")
#                 qty = int(input("Quantity: "))
#                 price = float(input("Price: "))
                
#                 # We store the record as a list
#                 record = [item_no, name, qty, price]
#                 pickle.dump(record, f)
        
#         # 2. Reading and Displaying
#         print("\n" + "="*30)
#         print("STORE RECORDS REPORT")
#         print("="*30)
        
#         with open("records.dat", "rb") as f:
#             while True:
#                 try:
#                     data = pickle.load(f)
#                     # Calculation: Amount = Price * Quantity
#                     amount = data[3] * data[2]
                    
#                     print(f"Item No:      {data[0]}")
#                     print(f"Item Name:    {data[1]}")
#                     print(f"Quantity:     {data[2]}")
#                     print(f"Price per item: {data[3]}")
#                     print(f"Amount:       {amount}")
#                     print("-" * 20)
#                 except EOFError:
#                     # End of File reached
#                     break
#     except Exception as e:
#         print(f"An error occurred: {e}")

# binary_operations()