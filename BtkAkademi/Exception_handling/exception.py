

def check_password(psw):
    import re
    if len(psw) < 9:
        raise Exception("parola en az 8 karakter olmalıdır")
    elif not re.search("[a-z]",psw):
        raise Exception("Parola kucuk harf icermelidir")
    elif not re.search("[A-Z]",psw):
        raise Exception("Parola buyuk harf icermelidir")
    elif not re.search("[0-9]",psw):
        raise Exception("Parola rakam harf icermelidir")
    elif not re.search("[_@$]",psw):
        raise Exception("Parola alpha numeric karakter icermelidir")
    elif re.search("\s",psw):
        raise Exception("Parola boşluk içermemelidir")
    
password = "135791315aA_"

try:
    check_password(password)
except Exception as es:
    print(es)
else:
    print("gecerli parola")
finally:
    print("finally")