 2k20/scripts2020/Shriraj_Chinchwade.py 
@@ -0,0 +1,24 @@
# A positive integer is called an Armstrong number of order n if
# abcd... = an + bn + cn + dn + ...=

num = int(input("input the number that you want to check for armstrong number = "))

# Changed num variable to string, 
# and calculated the length (number of digits)
order = len(str(num))

# initialize sum
sum = 0

# find the sum of the cube of each digit
temp = num
while temp > 0:
   digit = temp % 10
   sum += digit ** order
   temp //= 10

# display the result
if num == sum:
   print(num,"is an Armstrong number")
else:
   print(num,"is not an Armstrong number")
