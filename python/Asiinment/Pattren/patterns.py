'''

Welcome to GDB Online.
GDB online is an online compiler and debugger tool for C, C++, Python, Java, PHP, Ruby, Perl,
C#, VB, Swift, Pascal, Fortran, Haskell, Objective-C, Assembly, HTML, CSS, JS, SQLite, Prolog.
Code, Compile, Run and Debug online from anywhere in world.

'''
print("Hello "*5,end='')
# pattern 1
n = int(input('Entern the n'))

for i in range(1,n):
    # print(i)
    print(" "*(n-i),end="")
    print("*"*i)
# pattern 2    
n = int(input('Entern the n'))

for i in range(1,n):
    # print(i)
    print(" "*(n-i))
    print("*"*i,end="")
    
    
    
