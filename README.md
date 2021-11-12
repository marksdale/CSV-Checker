# Example CSV Data Checking Script

Python script to check a csv file for issues.  Writes good output to separate file and errors to another.  First small project to teach myself various aspects of Python.

## Technologies used:
- Python 3.9.8
- Requests library 2.26.0
- https://postcodes.io API - free service with no auth necessary.

## CSV Input file columns

- **name**        -   persons name
- **number**      -   up to 3 digit number
- **age**         -   persons age
- **password**    -   users password
- **account**     -   account number
- **postcode**    -   users postcode (UK)

## Script obectives

The data from the input file is taken line by line and in some cases the contents checked for validity.  Where issues are found the the whole record is written to the error.csv file in the output location along with a note of the issue.  IF all fields in a record are okay the data is written to the output file.

### Actions undertaken are:

1. If **number** is less than 3 chrs long prefix zeros.
2. **password** is checked for complexity.  It must:
    - be =<8 chrs long>
    - contain at least one upper case chr.
    - contain at least one lower case chr.
    - cotnain at least one symbol chr.
3. **account** number must be numeric and 8 chrs long.
4. **postcode** must be valid in the UK.

## Syntax

datacheck.py -i {input path}{filename} -o {input path}{filename} -t {true|false} -a {append|overwrite} -h help

- -i    -   enter path to the input csv file.
- -o    -   enter path to output file.
- -t    -   specify if the CSV file has headers or not.  if headers exist they will be added to the output files for either new or appended data.
- -a    -   specify whether the output should replace or overwrite existing files.

### Example

`datacheck.py -i C:\Documents\testdata.csv -o c:\Documents\output.csv -t true -a overwrite`

