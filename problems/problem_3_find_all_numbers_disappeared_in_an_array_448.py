"""
https://leetcode.com/problems/find-all-numbers-disappeared-in-an-array/description/
448. Find All Numbers Disappeared in an Array

Given an array nums of n integers where nums[i] is in the range [1, n], return an array of all the integers
in the range [1, n] that do not appear in nums.

Example 1:
Input: nums = [4,3,2,7,8,2,3,1]
Output: [5,6]
"""


# solution with space complexity O(n)
class Solution1:
    def findDisappearedNumbers(self, nums: list[int]) -> list[int]:
        return list(set(range(1, len(nums) + 1)) - set(nums))


# solution with space complexity O(1)
class Solution:
    def findDisappearedNumbers(self, nums: list[int]) -> list[int]:
        nums_set = set(nums)
        missing_nums = []
        for num in range(1, len(nums) + 1):
            if num not in nums_set:
                missing_nums.append(num)
        return missing_nums


solution = Solution()
print(solution.findDisappearedNumbers(nums=[4, 3, 2, 7, 8, 2, 3, 1]))
