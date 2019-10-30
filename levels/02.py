
list=input()
listIn=str(list.split())

print("- " + listIn )
listIn.sort()

count=1
for x in listIn :
    y=x+1
    for y in listIn:
        if(y==x):
            count+=1
    if count==2 :
        print(" contain two" + x)
    if count==3:
        printf(" contains three" + x)

if(count==1):       
    print("- " + listIn + "contains no letters that appear exaclty two or three times")    