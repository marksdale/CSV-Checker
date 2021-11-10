



import csv

source_file = "C:/Users/mark/OneDrive/Documents/testdata.csv"

with open(source_file) as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    for row in csv_reader:
        print(f'\t{row[0]},{row[1]},{row[2]},{row[3]},{row[4]}')

