"""
a=10
b=oct(a)
print(b)


a=50
b=bin(a)
b=a>>3
print(b)


a=10
b=20
print("a's value is ",a,"and b's value is ",b)
print("a's value is {} and b's value is {}".format(a,b))




print("hello"*10)

year =2015

if (year % 4) == 0:
   if (year % 100) == 0:
       if (year % 400) == 0:
           print("{0} is a leap year".format(year))
       else:
           print("{0} is not a leap year".format(year))
   else:
       print("{0} is a leap year".format(year))
else:
   print("{0} is not a leap year".format(year))


marks=int(input("enter the marks"))

if marks>0 and marks<32:
    print("fail")
elif marks>33 and marks<44:
    print("grade 'E'")
elif marks>45 and marks<54:
    print("grade 'D'")
elif marks>55 and marks<64:
    print("grade 'c")
elif marks>65 and marks<74:
    print("grade 'B'")
elif marks>75 and marks<100:
    print("grade 'A'")
else:
   print("you enter wrong choice")

for i in range(0,100,2):
     print("even no. is",i)
        """""

num=int(input("enter the no."))
if num > 1:
    for i in range(2, num):
        if (num % i) == 0:
            print(num, "is not a prime number")
            break
    else:
        print(num, "is a prime number")
else:
    print(num, "is not a prime number")



