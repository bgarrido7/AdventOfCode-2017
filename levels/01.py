freq=0
input_string=input("Enter a list element separated by space ")
list=input_string.split()
for x in list:
    res=freq + int(x)
    print("- Current frequency "+ str(freq) +", change of " + x +"; resulting frequency  "+ str(res))    
    freq=res
    