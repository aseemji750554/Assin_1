# using recurtion
f=1
def fect (n):
    if n==1:
        return n
    return n*fect(n=n-1)
n=int(input('enter the n'))
print(fect(n))
