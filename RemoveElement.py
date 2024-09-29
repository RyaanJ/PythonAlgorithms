'''
Given an integer array nums and an integer val, remove all occurrences of val in nums in-place. 
The order of the elements may be changed. Then return the number of elements in nums which are not equal to val.
Consider the number of elements in nums which are not equal to val be k, to get accepted, you need to do the following things:
Change the array nums such that the first k elements of nums contain the elements which are not equal to val. 
The remaining elements of nums are not important as well as the size of nums.
Return k.
'''

def removeElement(nums: list[int], val: int) -> int:
        k = 0
        for i in range(len(nums)):
            if nums[i] != val:
                nums[k] = nums[i]
                k +=1
        return nums
        

nums = [3, 2, 2, 3]
val = 3

print(removeElement(nums, val))
#As long as first two elements are correct, problem is solved

nums2 = [0, 1, 2, 2, 3, 0, 4, 2]
val2 = 2

print(removeElement(nums2, val2))
#As long as first 5 elements are correct, problem solved

'''
Intuition!
The intuition behind this solution is to iterate through the array and keep track of two pointers: index and i. 
The index pointer represents the position where the next non-target element should be placed, while the i pointer iterates through the array elements. 
By overwriting the target elements with non-target elements, the solution effectively removes all occurrences of the target value from the array.
'''


'''
Example 1:

Input: nums = [3,2,2,3], val = 3
Output: 2, nums = [2,2,_,_]
Explanation: Your function should return k = 2, with the first two elements of nums being 2.
It does not matter what you leave beyond the returned k (hence they are underscores).
Example 2:

Input: nums = [0,1,2,2,3,0,4,2], val = 2
Output: 5, nums = [0,1,4,0,3,_,_,_]
Explanation: Your function should return k = 5, with the first five elements of nums containing 0, 0, 1, 3, and 4.
Note that the five elements can be returned in any order.
It does not matter what you leave beyond the returned k (hence they are underscores).
'''