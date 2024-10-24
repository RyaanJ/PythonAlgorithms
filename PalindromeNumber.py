"""
Given an integer x, return true if x is a 
palindrome
, and false otherwise.
"""

import math


def isPalindrome(x: int) -> bool:
    original_x = x
    if x == 0:
        return True
    if x < 0:
        return False
    reversed = 0
    pop = 0
    while x != 0:
        pop = x % 10
        x = math.floor(x / 10)
        reversed = (reversed * 10) + pop

    if reversed == original_x:
        return True
    else:
        return False


# Uses different logic than the ValidPalindrome.py as we are using math operations to reverse the number

print(isPalindrome(121))
print(isPalindrome(-121))
print(isPalindrome(12123))


"""
Example 1:

Input: x = 121
Output: true
Explanation: 121 reads as 121 from left to right and from right to left.
Example 2:

Input: x = -121
Output: false
Explanation: From left to right, it reads -121. From right to left, it becomes 121-. Therefore it is not a palindrome.
Example 3:

Input: x = 10
Output: false
Explanation: Reads 01 from right to left. Therefore it is not a palindrome.
 
"""
