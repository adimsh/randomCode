# WAP to input email IDs of n students and store them in a tuple. Create two more tuples, one to store the username and the other to store the domain name...

full_email = tuple()
user_name = tuple()
domain_name = tuple()
n = int(input("Enter total number of email IDs: "))
for i in range(n):
    email = input(f"Enter email id {i + 1}: ")
    full_email += (email, )

for i in full_email:
    un, dn = tuple(i.split('@')) # the returned list can be unpacked directly as well, without typecasting it to a tuple
    user_name += (un, )
    domain_name += (dn, )

print(full_email, user_name, domain_name, end = "\n")

