fname = input("Enter File Path: ")
if len(fname) < 1: 
    fname = "Dr.Chuck\Chapter4\clown.txt"
hand = open(fname)
dict = dict()
for line in hand:
    line = line.rstrip()
    words = line.split()
    for w in words:
        dict[w] = dict.get(w,0)+1
#we want to find the most common word

largest = -1
theword = None
for k,v in dict.items():
    print(k,v)
    if v > largest:
        largest = v
        theword = k
print(theword,largest)
        