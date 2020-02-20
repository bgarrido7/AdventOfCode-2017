import sys

n = input()
i = 2
x = 1

spiral = [1, 1]

while  x < n :
    j=i
    for s in range(3):
        j=i
        spiral.append(spiral[i-j]+spiral[i-1])
        i += 1
        spiral.append(spiral[i-1]+spiral[i-2]+spiral[i-j])
        #x = spiral[-1]
        j=i
        i += 1

    j=i+1    
    i += 1
    x = spiral[-1]
    #print(x)
    print(spiral)


print(x)

