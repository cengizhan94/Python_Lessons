import re
#Regex
"""hand = open("Dr.Chuck\intro.txt")
for line in hand:
    line = line.rstrip()
    if re.search('^from',line):
        print(line)"""

"""x = "My two favorite numbers are 23 and7"
y = re.findall('[0-9]+',x)
print(y)

y = re.findall('[aeio]+',x)
print(y)"""

#Greedy Matching

"""x = 'From: using the: character'
y = re.findall('^F.+:',x)
print(y)"""

#Non-Greedy Matching

"""x = 'From: sonsair11@gmail.com Sat Jan 5 07:28:16 2023'
y = re.findall('^F.+?:',x)
print(y)

y = re.findall('\S+@\S+',x)
print(y)"""

data = 'From c.engiz11@gmail.com Mon Jul 07:40:01 2023'
"""atpos = data.find('@')
print(atpos)

sppos = data.find(' ',atpos)
print(sppos)

host = data[atpos + 1 : sppos]
print(host)"""

#The double split pattern

words = data.split()
email = words[1]
pieces = email.split('@')
print(pieces[1])
