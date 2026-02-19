# WAP to create a CSV file named "student.csv" and strore student records(Roll Number, Name, Marks) in it. The program should accept input for 3 students and store their details in the file.
# Ensure that the roll number is stored as an integer and marks as a floating-point number.
import csv

stu_rec = 1
rec_list = []
print("ENTER STUDENT RECORDS")
while True:
    print("Student {}:\n".format(stu_rec))
    roll_no = int(input("Enter student Roll Number- "))
    name = input("Enter student Name- ")
    marks = float(input("Enter student Marks- "))
    record = [roll_no, name, marks]
    rec_list.append(record)
    ans = input("Do you wish to make more entries?(y/n): ")
    if ans.lower() == 'n':
        break
    stu_rec += 1

file_obj = open("student.csv", "w", newline = "")
writer_obj = csv.writer(file_obj)

# writing into the file
header = ["Roll Number", "Name", "Marks"]
writer_obj.writerow(header)
writer_obj.writerows(rec_list)
file_obj.close()

# Reading records
file_obj = open("student.csv", "r", newline = "")
reader_obj = csv.reader(file_obj)
for row in reader_obj:
    print(row)
file_obj.close()
print("Student Records printed successfully")

