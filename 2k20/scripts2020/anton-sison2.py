# Check if a number is positive or negative
def check_number(number):
  if number > 0:
     print("{} is a positive number".format(number))
  elif number == 0:
     print("Zero")
  else:
     print("{} is a negative number".format(number))
     
num = int(input("Enter a number: "))
check_number(num)
