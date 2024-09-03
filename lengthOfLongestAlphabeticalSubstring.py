# Made my own leetcode problem, it's a play on LC #3, which is to find the longest substring in a string
# but for this problem, you are suppose to find the longest substring in a string that is also in ALPHABETICAL order

def lengthOfLongestAlphabeticalSubstring(s: str) -> int:
        alphabet = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z", "0"]
        current_sum = 1
        new = 1
        i = 0 
        k = 1
        while i < k and k < len(s):
            if s[k] == (alphabet[alphabet.index(s[i]) + 1]):
                current_sum += 1
                i += 1
                k += 1
            elif s[k] != (alphabet[alphabet.index(s[i]) + 1]):
                i += 1
                k += 1
                new = max(new, current_sum)
                current_sum = 1
        return new

print(lengthOfLongestAlphabeticalSubstring("abdertyzxnt"))

'''
Example 1:

Input: s = "zxyzxyz"

Output: 3

Explanation: The string "xyz" is the longest without duplicate characters

Exmaple 2:

Input: s = "abdertyzxnt"

Output: 2
'''