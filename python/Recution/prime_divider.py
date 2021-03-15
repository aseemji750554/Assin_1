import math 
def pp(num):
    if num > 1:
        # check for factors
        for i in range(2,math.sqrt(n)):
            if (num % i) == 0:
                # print(num,"is not a prime number")
                # print(i,"times",num//i,"is",num)
                return 0
                
        else:
            # print(num,"is a prime number")
            return 1
            
        # if input number is less than
        # or equal to 1, it is not prime
    else:
        # print(num,"is not a prime number")
        return 0

def div(n):
    
    for i in range(1,n+1):
        if(n%i==0 and pp(i)==1):
            print(i)
n=50
div(n)
