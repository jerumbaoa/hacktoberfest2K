# Max & Min finder (Input in One line List)
# Python Program which take Input of list in single line & give there Max & Min Value

#If split input needed
# numbers = input_from_user.split()
# numbers=map(int, numbers)
# n=int(input())


lst = []

for i in map(int,input().split()):
    lst.append(i)

A=max(lst)
B=min(lst)

print("Max No in List is : ",A)
print("Min No in List is : ",B)
print("Max+Min: ",A+B)