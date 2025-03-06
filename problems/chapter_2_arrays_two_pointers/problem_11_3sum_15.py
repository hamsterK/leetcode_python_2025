"""
https://leetcode.com/problems/3sum/description/
15. 3Sum

Given an integer array nums, return all the triplets [nums[i], nums[j], nums[k]]
such that i != j, i != k, and j != k, and nums[i] + nums[j] + nums[k] == 0.
Notice that the solution set must not contain duplicate triplets.

Example 1:
Input: nums = [-1,0,1,2,-1,-4]
Output: [[-1,-1,2],[-1,0,1]]
"""


class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        triplets = []
        nums.sort()

        for ind, val in enumerate(nums):
            if (ind > 0) & (val == nums[ind-1]):
                continue

            left = ind + 1
            right = (len(nums) - 1)

            while left < right:
                currentSum = val + nums[left] + nums[right]
                if currentSum > 0:
                    right -= 1
                elif currentSum < 0:
                    left += 1
                else:
                    triplets.append([val, nums[left], nums[right]])
                    left += 1
                    while (left < right) & (nums[left] == nums[left-1]):
                        left += 1

        return triplets



solution = Solution()
print(solution.threeSum([-1,0,1,2,-1,-4]))





