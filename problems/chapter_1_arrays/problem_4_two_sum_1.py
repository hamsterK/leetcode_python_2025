"""
https://leetcode.com/problems/two-sum/description/
1. Two Sum

Given an array of integers nums and an integer target,
return indices of the two numbers such that they add up to target.
You may assume that each input would have exactly one solution, and you may not use the same element twice.
You can return the answer in any order.

Example 1:
Input: nums = [2,7,11,15], target = 9
Output: [0,1]
"""


class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        elements = dict()
        for ind, num in enumerate(nums):
            if (desired_num := target - num) in elements:
                return [elements[desired_num], ind]
            elements[num] = ind


solution = Solution()
print(solution.twoSum(nums=[-3, 4, 3, 90], target=0))
