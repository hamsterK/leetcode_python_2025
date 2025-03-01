"""
https://leetcode.com/problems/contains-duplicate/description/
217. Contains Duplicate

Given an integer array nums, return true if any value appears at least twice in the array,
and return false if every element is distinct.

Example 1:
Input: nums = [1,2,3,1]
Output: true
"""


class Solution:
    def containsDuplicate(self, nums: list[int]) -> bool:
        return len(nums) != len(set(nums))


solution = Solution()
print(solution.containsDuplicate(nums=[1, 2, 3, 1]))