import csv

# File name
csv_file = 'expenses.csv'

# Headers and data
headers = ['date', 'category', 'amount']
data = [
    ['2025-05-01', 'Food', 50.00],
    ['2025-05-02', 'Transport', 20.00],
    ['2025-05-03', 'Food', 30.00]
]

# Open the file in append mode ('a') and write the data
with open(csv_file, mode='a', newline='') as file:
    writer = csv.writer(file)
    
    # Write headers only if file is empty
    if file.tell() == 0:
        writer.writerow(headers)
    
    # Write data rows
    writer.writerows(data)

print("Data added successfully!")