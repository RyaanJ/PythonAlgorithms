## 28. Find the Index of the First Occurrence in a String
class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        l = False
        if needle not in haystack:
            return -1
        for i in range(len(haystack)):
            if haystack[i:i + len(needle)] == needle:
                return i


"""
Given two strings needle and haystack, return the index of the first occurrence of needle in haystack, or -1 if needle is not part of haystack.

Input: haystack = "sadbutsad", needle = "sad"
Output: 0
Explanation: "sad" occurs at index 0 and 6.
The first occurrence is at index 0, so we return 0.

Input: haystack = "leetcode", needle = "leeto"
Output: -1
Explanation: "leeto" did not occur in "leetcode", so we return -1.
"""