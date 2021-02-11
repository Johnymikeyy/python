#reading the csv files with csv Module

import csv
with open("fruits.csv", 'r', newline ='', encoding = 'utf-8') as file:
    csv_rows = csv.reader(file)
    
    for row in csv_rows:
        print(row)