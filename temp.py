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


if header == "true":
    line_count = 0
else:
    line_count = 1


with open(input_file, 'rt') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    for line in csv_reader:
        if line_count == 0:
            line_count += 1
            continue
        else:
            print(line)
            line_count += 1

csv_file.close()