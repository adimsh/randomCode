import csv
header = ['Name', 'Age', 'City']
data = [['Aman', 17, 'Jaipur'],
	['Bhavesh', 18, 'Udaipur'],
	['Chirag', 16, 'Jodhpur']
	]
	
with open("people.csv", "w", newline = "") as file_object:
	writer_object = csv.writer(file_object)
	writer_object.writerow(header)
	writer_object.writerows(data)
print("CSV file written successfully")