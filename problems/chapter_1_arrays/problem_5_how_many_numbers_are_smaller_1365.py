"""
https://leetcode.com/problems/how-many-numbers-are-smaller-than-the-current-number/description/
1365. How Many Numbers Are Smaller Than the Current Number
Given the array nums, for each nums[i] find out how many numbers in the array are smaller than it.
That is, for each nums[i] you have to count the number of valid j's such that j != i and nums[j] < nums[i].
Return the answer in an array.

Example 1:
Input: nums = [8,1,2,2,3]
Output: [4,0,1,1,3]
"""


# takes less space, but slow
class Solution1:
    def smallerNumbersThanCurrent(self, nums: list[int]) -> list[int]:
        answers = []
        for num in nums:
            answers.append(sorted(nums).index(num))
        return answers


# superfast, faster solution is better
class Solution:
    def smallerNumbersThanCurrent(self, nums: list[int]) -> list[int]:
        sorted_nums = sorted(nums)
        nums_map = {}
        for ind, num in enumerate(sorted_nums):
            if num not in nums_map:
                nums_map[num] = ind
        return [nums_map[num] for num in nums]


solution = Solution()
print(solution.smallerNumbersThanCurrent(nums=[8, 1, 2, 2, 3]))
