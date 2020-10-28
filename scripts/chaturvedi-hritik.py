# Great number function

def big_num(a,b):
    if(a > b):
        print(str(a)+" is greater than "+ str(b))
    elif(b>a):
        print(str(b)+" is greater than "+str(a))
    else:
        print(str(a)+" is equal to"+str(b))

c = int(input("Enter the first number: "))
d = int(input("Enter the second number: "))

big_num(c,d)
