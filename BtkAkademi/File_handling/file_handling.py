# file = open("C:/users/sonsa/Documents/newFile.txt","w")
# file.close()

# file=open("newfile2.txt","x",encoding="UTF-8")
try:
    file=open("newfile.txt","r",encoding="UTF-8")
except Exception as e:
    print("Read error")
finally:
   file.close() 
# file.write("Cengiz Han") #w 
# file.write(" Hello world!") #a
print(file)



