"""
https://leetcode.com/problems/missing-number/description/
268. Missing Number

Given an array nums containing n distinct numbers in the range [0, n], return the only number in the range
that is missing from the array.

Example 1:
Input: nums = [3,0,1]
Output: 2
"""


class Solution:
    def missingNumber(self, nums: list[int]) -> int:
        return sum(list(range(len(nums) + 1))) - sum(nums)


solution = Solution()
print(solution.missingNumber(nums=[3, 0, 1]))
