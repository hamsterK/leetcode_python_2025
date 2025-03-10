"""
https://leetcode.com/problems/contains-duplicate-ii/description/
219. Contains Duplicate II

Given an integer array nums and an integer k, return true if there are
two distinct indices i and j in the array such that nums[i] == nums[j] and abs(i - j) <= k.

Example 1:
Input: nums = [1,2,3,1], k = 3
Output: true
"""


class Solution:
    def containsNearbyDuplicate(self, nums: list[int], k: int) -> bool:
        seen = set()
        for i, num in enumerate(nums):
            if num in seen:
                return True
            seen.add(num)
            if len(seen) > k:
                seen.remove(nums[i - k])

        return False


solution = Solution()
print(solution.containsNearbyDuplicate(nums = [1,2,3,1,2,3], k = 2))
