############################################
#  Example CSV data checking script
############################################

# Parse input command line arguments.
import argparse
# import csv handler library
import csv
# import custom written functions
from functions import *

# create argparse object
parser = argparse.ArgumentParser(description='Data checking and remediation')

#add arguments to the object
parser.add_argument('-i',action='store', type=str, help='<filepath><filename>', required=True)
parser.add_argument('-o',action='store', type=str, help='<filepath><filename>', required=True)
parser.add_argument('-t',action='store', type=str, choices=['true', 'false'], help='Does the file have column headers or not?', required=True)

# save arguments to variable
args = parser.parse_args()

# Set variables for command line arguments
input_file = args.i
output_file = args.o
error_file = get_path(output_file) + "\error.csv"
header = args.t

# open CSV file as specified in the input file argument.
with open(input_file, 'rt') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    # skip the top line of the file if the header arg was set to true.
    for line in csv_reader:
        error = "false"
        if header == "true":
            header = "false"
            data = line[0],line[1], line[2], line[3], line[4], line[5]
            write_to_file(data, output_file)
            write_to_file(data, error_file)
        else:
            # ensure all numbers are 3 chrs long.  prefix with zeros where not.
            col1 = format(line[1], "0>3")
            # run password check function to check complexity
            if password_check(line[3]) == None:
                col3 = "insecure"
            else:
                col3 = line[3]
            # run account number check function to ensure acc No.s are the correct format.
            if account_no_check(line[4]) == None:
                col4 = "invalid"
            else:
                col4 = line[4]
            # run the postcode checker function to check validity of the postcode.
            #if postcode_validate(line[5])== False:
            #    col5 = "invalid"
            #else:
                col5 = line[5]
            # print results for checking














            
            print(line[0], col1, line[2], col3, col4, col5)
#close csv file as all done.
csv_file.close()

