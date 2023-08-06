# file=open("newfile.txt","r",encoding="UTF-8")

#for
# for item in file:
#     print(item,end= " ")
# print("for")


#read()

# content = file.read()
# print("content1")
# print(content)

# content2 = file.read()
# print("content2")
# print(content2)


# content3 = file.read(5)
# print("contetn3")
# print(content3)

#readline()
# print(file.readline(),end="") 
# print(file.readline(),end="") 
# print(file.readline(),end="") 
# print(file.readline(),end="") 
# print(file.readline(),end="") 
# print(file.readline(),end="") 
# print(file.readline(),end="") 
# print(file.readline(),end="") 
# print(file.readline(),end="") 

# list = file.readlines()
# print(list)
#file.close()

#auto close file

# with open("newfile.txt","a",encoding="UTF-8") as file:
    # file.seek(65)
    # file.write("\nHello World2")
    # file.write("\nPervin Oflaz")
    
with open("newfile.txt","r+",encoding="UTF-8") as file:
    print(file.read())
    content = file.read()
    content = "Zeynep Uyar\n" + content
    file.seek(0)
    file.write(content)    
    list = file.readlines()
    list.insert(1,"ZeynoLine\n")
    file.seek(0)
    # for i in list:
    #     file.write(i)
    file.writelines(list)
    
    # print(file.tell())
    # print(content) 
    # file.seek(0)
    # print(file.tell())
    # print(content)
with open("newfile.txt","r",encoding="UTF-8") as file:
    print(file.read())   
    

    


