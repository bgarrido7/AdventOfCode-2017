f = open("test.txt", 'r')

array = []

for line in f:
    for x in line.split():
        array.append(int(x))

#while max(array) != min(array):
for a in range(2):
    m = max(array) / (len(array)-1)
    i = array.index(max(array))

    print "max->", max(array), "divide->", m
    array[i] = max(array) % (len(array) -1)    
    print(array)
    print(m)
    i+=1

    for j in range(len(array)-1):
        index = i
        if index >= len(array):
            index=0
        array[index] = m
        index+=1
        print(array)
    