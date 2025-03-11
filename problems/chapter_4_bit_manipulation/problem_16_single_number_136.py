"""
https://leetcode.com/problems/single-number/description/
136. Single Number

Given a non-empty array of integers nums, every element appears twice except for one. Find that single one.
You must implement a solution with a linear runtime complexity and use only constant extra space.

Example 1:
Input: nums = [2,2,1]
Output: 1
"""

class Solution:
    def singleNumber(self, nums: list[int]) -> int:
        xor = 0
        for i in nums:
            xor ^= i  # pairs cancel each other out (because x ^ x = 0), order does not matter
        return xor


solution = Solution()
print(solution.singleNumber([4, 1, 2, 1, 2]))
