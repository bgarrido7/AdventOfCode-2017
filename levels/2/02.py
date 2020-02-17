f = open ('test.txt', 'r')
array = []
sum = 0

for line in f:
    array.append([int(x) for x in line.split()])

for x in array:
    min = x[0]
    max = x[0]
    for i in x:
        if min > i:
            min = i
        if max < i:
            max = i
    sum+=max-min
    
print(sum)
f.close()
