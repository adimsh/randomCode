import csv
	
with open("people.csv", "r") as file_object:
	reader_object = csv.reader(file_object)
	for row in reader_object:
		print(row) # each row is a list
	print("CSV file read successfully")