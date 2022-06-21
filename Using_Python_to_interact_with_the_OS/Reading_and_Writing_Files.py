### READ FILE ###

file.open("spuider.txt") # open file
print(file.readline()) # read just one line
print(file.read()) # read all lines from the current place
file.close() # close file always

# Another way of reading (does not need to close)

with open("spider.txt") as file:
	print(file.readline())

# iteration

with open("spider.txt") as file:
	for line in file:
	print(line.strip().upper()) # with no extra empty lines(use of strip)

### WRITE IN FILE ###

with open("novel. txt", "w") as file:
	file.write("It was a dark and stormy night") # it returns the number of characters and also it removes the previous content of the file

### CSV ###

## Reading CSV

import csv
f = open("csv_file.txt")
csv_f = csv.reader(f)
for row in csv_file:
	name, phone, role = row
	print('Name: {}, Phone: {}, Role: {}'.format(name, phone, role))


## Writing CSV

hosts = [["workstation.local", "192.168.25.46"], ["webserver.cloud", "10.2.5.6"]]
with open('hosts.csv', 'w') as hosts_csv:
	writer = csv.writer(hosts_csv)
	writer.writerows(hosts)

## Reading and Writing CSV Files with Dictionaries

# DictReader

with open('software.csv') as software:
	reader = csv.DictReader(software)
	for row in reader: 
		print(("{} has {} users").format(row["name"], row["users"]))

# DictWriter

users = [ {"name": "Sol Mansi", "username": "solm", "department": "IT"},
		  {"name": "Anthos Kountouris", "username": "anthosk", "department": "User Experience Reaserch"},
		  {"name": "Nikolas Nikolaou", "username": "nikolasn", "department": "Development"} ]

keys = ["name", "username", "deparment"]

with open('by_department.csv', 'w') as by_department:
	writer = csv.DictWriter(by_department, fieldnames=keys)
	writer.writerheader()
	write.writerows(users)



