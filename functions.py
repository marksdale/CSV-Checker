############################################
#  Custom functions for data checking
############################################

# check password is complex
def password_check(passwd):
    SpecialSym =['$', '@', '#', '%', "£", "*", "!"]
    val = True
      
    if len(passwd) < 8:
         val = False
          
    if len(passwd) > 20:
         val = False
          
    if not any(char.isdigit() for char in passwd):
         val = False
          
    if not any(char.isupper() for char in passwd):
         val = False
          
    if not any(char.islower() for char in passwd):
         val = False
          
    if not any(char in SpecialSym for char in passwd):
         val = False

    if val:
        return val

# check account number is in correct format
def account_no_check(accno):
    val = True
      
    if len(accno) != 8:
         val = False
          
    if not all(char.isdigit() for char in accno):
         val = False

    if val:
        return val

# check postcode is valid.  Query https://postcodes.io API
def postcode_validate(pc):

    import requests      # requests is not a standard Python library.  Use 'python -m pip install requests' to install.
   
    url = "https://api.postcodes.io/postcodes/" + pc + "/validate"

    data = requests.get(url)

    result = data.json().get('result')

    return result

# write data to file by appending.  If file does not exist it is created.
def write_to_file(data, target):
     import csv
     with open(target, "at", newline='') as csvfile:
          writer = csv.writer(csvfile, delimiter=',')
          writer.writerow(data)
     
# strip filename from path argument to be used elsewhere.
def get_path(output_path):
     import os.path
     path = os.path.dirname(output_path)
     return path