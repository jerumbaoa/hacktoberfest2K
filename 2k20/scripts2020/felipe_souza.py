"""
A palindrome is a word, number, phrase, or other sequence of characters 
which reads the same backward as forward, such as madam, racecar. There are 
also numeric palindromes, including date/time stamps using short digits 
11/11/11 11:11 and long digits 02/02/2020. Sentence-length palindromes ignore 
capitalization, punctuation, and word boundaries.
"""

def is_palindrome(word):
    """
    This function receives a string named as word and return if the word is a palindrome or not
    """
    return word == word[::-1]
