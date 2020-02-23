import re

f = open("input.txt", 'r')
this = True
res = []
followers = []
follow = []
candidates = []
size=[]
for content in f:

    line = re.split(' |, |\n', content)
    child = []
    if len(line)>3 :
        child.append(line[0])
        for i in range (3, len(line)-1):
            child.append(line[i])

        followers.append(list(child))

for x in followers:
    size.append(len(x))
max_size=max(size)

for z in followers:
    if len(z) == max_size:
        follow.append(z)

print(follow)

for check in follow:
    candidates.append(check[0])

print "\ncandidates->", candidates, "\n"

for check in follow:
    this = True
    for test in candidates:
       # print(test)
       # print(check)
    
        if test not in check:
            #print("this is not the bottom")
            this = False
    if this==True :
        res = check

print(res[0])