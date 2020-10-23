# Check if a number is odd or even
def check_number(number):
  if (number % 2) == 0:
     print("{} is Even".format(number))
  else:
     print("{} is Odd".format(number))
     
num = int(input("Enter a number: "))
check_number(num)
