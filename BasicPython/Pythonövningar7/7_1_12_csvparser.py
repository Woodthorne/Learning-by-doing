import csv
list_of_data = []
with open('data.csv',newline='') as f:
    csvreader = csv.reader(f)
    for line in csvreader:
        list_of_data.append(line)
print(list_of_data)