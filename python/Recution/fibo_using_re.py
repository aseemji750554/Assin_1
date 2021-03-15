# def febo(n):
#     if n==1:
#         print(a)
#     if n==2:
#         print(b)
#     else:
#         return febo(n-1)+febo(n-2)
# n=int(input("enter the value of n"))
# a=0
# b=1
# febo(n)


# Python program to display the Fibonacci sequence

def fibo(n):
   if n <= 1:
       return n
   else:
       return(fibo(n-1) + fibo(n-2))


n=int(input("Enter the limit"))

if n <= 0:
   print("Plese enter a positive integer")
else:
   print("Fibonacci sequence:")
   for i in range(n):
       print(fibo(i))