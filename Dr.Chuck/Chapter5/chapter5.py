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

x = 'From: sonsair11@gmail.com Sat Jan 5 07:28:16 2023'
y = re.findall('^F.+?:',x)
print(y)

y = re.findall('\S+@\S+',x)
print(y)
