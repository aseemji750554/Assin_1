am=float(input("Enter the amount "))

print('1 check balence')
print('2 credit')
print('3 debit balence')
print('4 exit')
ch=0
while ch!=4:
    ch = int(input())
    if ch==1 :
        print("The amount is ",am)
    if ch==2:
        ca=float(input("Enter thr amount to credit"))
        am=am+ca
        print("The Final Balance is :-",am)
    if ch==3:
        d=float(input("Enter the amount to debit"))
        if d>am+50:
            print('insuffient')
        else:
            am=am-d-50
            print("final balece is ",am)


