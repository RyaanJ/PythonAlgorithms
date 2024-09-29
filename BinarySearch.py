'''
Given an array of integers nums which is sorted in ascending order, and an integer target, write a function to search target in nums. 
If target exists, then return its index. Otherwise, return -1.
You must write an algorithm with O(log n) runtime complexity.
'''

#This simply requires Binary Search

def search(nums: list[int], target: int) -> int:
        l = 0
        r = len(nums) - 1
        if len(nums) == 1 and nums[0] == target:
            return 0
        elif len(nums) == 1 and nums[0] != target:
            return -1
        elif nums[0] == target:
            return 0
        elif target not in nums:
            return -1

            
        
        while l < r:
            m = round((l + r) / 2 + 0.1)
            if target > nums[m]:
                if m == l:
                    return -1
                l = m

            elif target < nums[m]:
                if m == r:
                    return -1
                r = m

            elif target == nums[m]:
                return m
            
nums = [-1, 0, 3, 5, 9, 12]
target = 9

print(search(nums, target))

'''
Example 1:

Input: nums = [-1,0,3,5,9,12], target = 9
Output: 4
Explanation: 9 exists in nums and its index is 4
Example 2:

Input: nums = [-1,0,3,5,9,12], target = 2
Output: -1
Explanation: 2 does not exist in nums so return -1
'''