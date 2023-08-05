
liste = ["1","2","5a","10b","abc","10","50"]
#1 
for item in liste:
    try:
        result = int(item)
        print(result)
    except Exception as e:
        continue
    
#2

while True:
    sayi = input("sayi: ")
    if sayi == "q" or sayi == "Q":
        break
    
    try:
        result = float(sayi)
        print(f'girdiginiz sayi: {sayi}')
    except Exception as e:
        print("gecersiz girdi")
        continue

#3

def checkPassword(password):
    turkce_karakterler = "şçğöıİ"
    
    for item in password:
        if item in turkce_karakterler:
            raise TypeError("Parola turkce karakter iceremez")
        else:
            pass


password = input("parola: ")

try:
    checkPassword(password)
except Exception as e:
    print(e)
    
#4

def faktoriyel(x):
    x = int(x)
    
    if x < 0:
        raise ValueError("Negatif değer")
    
    result = 1
    
    for i in range(1, x+1):
        result *= i
    
    return result
    
for x in [5,10,20,-3,"10a"]:
    try:
        y = faktoriyel(x)
    except Exception as e:
        print(e)
        continue
print(y)