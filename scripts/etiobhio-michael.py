#Collatz sequence
#the simplest impossible math problem
#
#define function collatz()
def collatz(number):
    if number % 2 == 0:
        print(number// 2)
        return number // 2
    elif number % 2 == 1:
        print(3*number+1)    
        return 3*number+1
#Print out question prompt
print('provide a number: ')
#save answer as variable user_input
try:
    user_input = int(input())
    #while loop that continues until user_input is 1
    while user_input != 1:
        user_input = collatz(int(user_input))
except ValueError:
    print('Please enter an Integer.')