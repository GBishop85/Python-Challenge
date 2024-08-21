import csv

 
 #joining path
 budget_data = os.path.join("Resources", "budget_data.csv")


 # Retrieve Budget Data from CSV file
  with open('budget_data.csv','r') as file:
  reader = csv.reader(file)
  next(reader)  # Skip the header row

 # find net amount of profit and loss
 P = []
 months = []

 #read through each row of data after header
 for rows in csvreader:
     P.append(int(rows[1]))
     months.append(rows[0])

