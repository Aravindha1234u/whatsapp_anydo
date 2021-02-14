import re

Regex = {
    "email":'^[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w{2,3}$',
    "phone":"^\+[1-9]{1}[0-9]{3,14}$"
}

def regex(email,phone):
    if not re.search(Regex['email'],email):
        print("Pass a valid Email address")
        exit(0)
        
    if not re.search(Regex['phone'],phone):
        print("Pass valid phonenumber with countrycode")
        exit(0)

    return True