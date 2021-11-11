# Parse input command line arguments.
import argparse

parser = argparse.ArgumentParser(description='Data checking and remediation')

parser.add_argument('-i',action='store', type=str, help='<filepath><filename>', required=True)
parser.add_argument('-o',action='store', type=str, help='<filepath><filename>', required=True)
parser.add_argument('-t',action='store', type=str, choices=['true', 'false'], help='Does the file have column headers or not?', required=True)

args = parser.parse_args()

# Set variables for command line arguments
input_file = args.i
output_file = args.o
header = args.t

import csv
from functions import *

with open(input_file, 'rt') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    for line in csv_reader:
        if header == "true":
            header = "false"
        else:
            col1 = format(line[1], "0>3")
            if password_check(line[3]) == None:
                col3 = "insecure"
            else:
                col3 = line[3]
            
            if account_no_check(line[4]) == None:
                col4 = "invalid"
            else:
                col4 = line[4]
            
            print(line[0], col1, line[2], col3, col4)

csv_file.close()

quit()

