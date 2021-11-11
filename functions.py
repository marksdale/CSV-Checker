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

def account_no_check(accno):
    val = True
      
    if len(accno) != 8:
         val = False
          
    if not all(char.isdigit() for char in accno):
         val = False

    if val:
        return val

def postcode_validate(pc):

    import requests
    import json

    url = "https://api.postcodes.io/postcodes/" + pc + "/validate"

    data = requests.get(url)

    result = data.json().get('result')

    return result