import argparse

parser = argparse.ArgumentParser(description='Data checking and remediation')

parser.add_argument('-i',action='store', type=str, help='<filepath><filename>', required=True)
parser.add_argument('-o',action='store', type=str, help='<filepath><filename>', required=True)
parser.add_argument('-t',action='store', type=str, choices=['true', 'false'], help='Does the file have column headers or not?', required=True)

inputfile = parser.parse_args('-i')

print(inputfile)


#parser.print_help()

