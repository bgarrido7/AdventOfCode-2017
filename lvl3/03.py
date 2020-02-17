import sys

n = input()
i = 1

if n==i:
    print(0)
    sys.exit()

#def get_num():


while(1):
    i+=2
    row = i*i
    
    #corners
    if (row == n) or (n==row-i-1) or (n==row-(i-1)*2) or (n==row-(i-1)*3):   
        print(i-1)  
        sys.exit()

    elif row > n: 
        end = row-i+1
        n_lines=(i-1)/2
        #botom line
        for x in range(row, end, -1):     
            if x==n:
                middle = row - n_lines #number align with 1
                step = abs(n - middle)
                print(step + n_lines)
                sys.exit()
        
    
        #left line
        for x in range(end, (end-i+1), -1):     
            if x==n:
                middle = end - n_lines #number align with 1
                step = abs(n - middle)
                print(step + n_lines)
                sys.exit()
                
        #top line
            for x in range(end-i+1, (row-i*2-2), -1):     
                if x==n:
                    middle = end-i+1 - n_lines #number align with 1
                    step = abs(n - middle)
                    print(step + n_lines)
                    sys.exit()
         #right line
            for x in range((row-i*2-2), (row-i*3), -1):     
                if x==n:
                    middle = (row-i*2-2) - n_lines #number align with 1
                    step = abs(n - middle)
                    print(step + n_lines)
                    sys.exit()   
