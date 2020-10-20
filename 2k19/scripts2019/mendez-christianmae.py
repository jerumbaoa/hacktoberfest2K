# function to check string is
# palindrome or not
def isPalindrome(word):

    # Using predefined function to
    # reverse to string print(s)
    rev = ''.join(reversed(word))

    # Checking if both string are
    # equal or not
    if (word == rev):
        return True
    return False

# main function
word= "malayalam"
ans = isPalindrome(word)

if (ans):
    print("Yes")
else:
    print("No")