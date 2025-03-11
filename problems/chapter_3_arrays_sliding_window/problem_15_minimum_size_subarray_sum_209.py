"""
https://leetcode.com/problems/minimum-size-subarray-sum/description/
209. Minimum Size Subarray Sum

Given an array of positive integers nums and a positive integer target, return the minimal length of a subarray
whose sum is greater than or equal to target. If there is no such subarray, return 0 instead.

Example 1:
Input: target = 7, nums = [2,3,1,2,4,3]
Output: 2
Explanation: The subarray [4,3] has the minimal length under the problem constraint.
"""


class Solution:
    def minSubArrayLen(self, target: int, nums: list[int]) -> int:
        l, total, answer = 0, 0, float('inf')
        for r in range(len(nums)):
            total += nums[r]
            while total >= target:
                answer = min(answer, r - l + 1)
                total -= nums[l]
                l += 1
        return 0 if total == float('inf') else answer


solution = Solution()
print(solution.minSubArrayLen(target = 11, nums = [1,2,3,4,5]))
