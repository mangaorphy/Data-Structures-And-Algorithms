'''
Given an integer X, return if x is a palindrome, and false otherwise
'''

class Solution(object):
    def isPalindrome(self, x):
        '''
        :type x: int
        :rtype: bool
        '''
    # Negative numbers are not palindromes
        if x < 0:
         return False
    # Convert the integer to a string
        str_x = str(x)
    # Check if the string is the same forwards and backwards
        return str_x == str_x[::-1]

# Example usage
print(Solution(121))   # Output: True
print(Solution(-121))  # Output: False
print(Solution(10))    # Output: False

