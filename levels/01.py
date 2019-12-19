s = input()
sum=0
res = [int(x) for x in str(s)]  #place the input number into an array

for i in range(len(res)):
    print("res[i]=",res[i])
    print("sum=", sum)
    if i+1 < len(res):
        if res[i]==res[i+1] :        
            sum+=res[i]
            i+=i
    print("-------------------")
print(sum)