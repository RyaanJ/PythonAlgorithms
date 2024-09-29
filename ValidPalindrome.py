'''
A phrase is a palindrome if, after converting all uppercase letters into lowercase letters and removing all non-alphanumeric characters, 
it reads the same forward and backward. 
Alphanumeric characters include letters and numbers.
'''



def isPalindrome(s: str) -> bool:
        s = ''.join(char for char in s if char.isalnum())
        s = s.lower()
        l = s
        l = l[::-1]
        return (l == s)

x = isPalindrome("A man, a plan, a canal: Panama")
print(x)


'''
Example 1:

Input: s = "A man, a plan, a canal: Panama"
Output: true
Explanation: "amanaplanacanalpanama" is a palindrome.
Example 2:

Input: s = "race a car"
Output: false
Explanation: "raceacar" is not a palindrome.
Example 3:

Input: s = " "
Output: true
Explanation: s is an empty string "" after removing non-alphanumeric characters.
Since an empty string reads the same forward and backward, it is a palindrome.
'''