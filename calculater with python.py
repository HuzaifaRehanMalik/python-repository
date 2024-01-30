x= int(input("enter value of first number: "))
y= int(input("enter value of second number: "))
print("1 for add(+)")
print("2 for subtarct(-)")
print("3 for devide(/)")
print("4 for multiply(*)")
choice = int(input("enter anyone number: "))
if choice==1:
    print("Result:",x+y)
elif choice==2:
    print("Result:",x-y)
elif choice==3:
    if y==0:
        print ("0 cannot be divided")
    else:
        print("Result:",x/y)  
elif choise==4:
    print("Result:",x*y)          
else:
    print("error: Plz try again")    