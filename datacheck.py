############################################
#  Example CSV data checking script
############################################

# Parse input command line arguments.
import argparse
# import csv handler library
import csv
# import library 
import os 
# import custom written functions
from functions import *

# create argparse object
parser = argparse.ArgumentParser(description='Data checking and remediation')

#add arguments to the object
parser.add_argument('-i',action='store', type=str, help='<filepath><filename>', required=True)
parser.add_argument('-o',action='store', type=str, help='<filepath><filename>', required=True)
parser.add_argument('-t',action='store', type=str, choices=['true', 'false'], help='Does the file have column headers or not?', required=True)
parser.add_argument('-a',action='store', type=str, choices=['append', 'overwrite'], help='Action if file already exists.', required=True)

# save arguments to variable
args = parser.parse_args()

# Set variables for command line arguments
input_file = args.i
output_file = args.o
error_file = get_path(output_file) + "\error.csv"
header = args.t
exist_action = args.a

# delete existing output files if 'overwrite' specified in arguments.
if exist_action == "overwrite":
    if os.path.exists(output_file):
        os.remove(output_file)
    if os.path.exists(error_file):
        os.remove(error_file)

# open CSV file as specified in the input file argument.
with open(input_file, 'rt') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    for line in csv_reader:
        error = "false"
        # skip processingf the top line of the file if the header arg was set to true.  Just write headers to the output files.
        if header == "true":
            header = "false"
            # write headers to output files
            data = line[0],line[1], line[2], line[3], line[4], line[5]
            write_to_file(data, output_file)
            write_to_file(data, error_file)
        else:
            col0 = line[0]
            # ensure all numbers are 3 chrs long.  prefix with zeros where not.
            col1 = format(line[1], "0>3")
            col2 = line[2]
            # run password check function to check complexity
            if password_check(line[3]) == None:
                col3 = line[3] + " - insecure"
                error = "true"
            else:
                col3 = line[3]
            # run account number check function to ensure acc No.s are the correct format.
            if account_no_check(line[4]) == None:
                col4 = line[4] + " - invalid"
                error = "true"
            else:
                col4 = line[4]
            # run the postcode checker function to check validity of the postcode.
            if postcode_validate(line[5])== False:
                col5 = line[5] + " - invalid"
                error = "true"
            else:
                col5 = line[5]
            # write output to file
            data = col0, col1, col2, col3, col4, col5
            if error == 'true':
                write_to_file(data, error_file)
            else:
                write_to_file(data, output_file)

#close csv file as all done.
csv_file.close()

