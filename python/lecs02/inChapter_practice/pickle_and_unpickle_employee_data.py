# WAP to take employee data of n employees as input, store each record as a list then pickle each list(at the end also tell the total size of the binary file), later unpickle them and print them to the console screen

import pickle

dump_dest = open("emp_records.dat", "ab") # we cannot do wb since that will truncate the binary file to 0 everytime we enter a new record
print("Enter records of employees:\n")
recno = 1
while True:
    ename = input(f"Employee {recno} record:\nEnter employee name: ")
    eid = int(input("Enter employee id: "))
    ebasic = float(input("Enter basic salary: "))
    eallow = float(input("Enter allowance: "))
    totalsal = ebasic + eallow
    emprec = [ename, eid, ebasic, eallow, totalsal]
    pickle.dump(emprec, dump_dest)
    answer = input("Do you wish to add more records (y/n): ")
    if answer.lower() == 'n':
        break
    recno += 1
dump_dest.flush() # not really needed

# to tell the total size of the binary file
print("Records pickled successfuly. Total size of the binary file(in bytes) is- ", dump_dest.tell())

dump_dest.close()

with open("emp_records.dat", "rb") as load_dest:
    emp_rec_list = []
    empno = 1
    while True:
        try:
            record = pickle.load(load_dest)
            print("Record of employee",  empno, ": ", record)
            emp_rec_list.append(record)
            empno += 1
        except EOFError:
            break
