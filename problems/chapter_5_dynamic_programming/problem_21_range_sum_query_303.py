"""
https://leetcode.com/problems/range-sum-query-immutable/description/
303. Range Sum Query - Immutable

Given an integer array nums, handle multiple queries of the following type:
Calculate the sum of the elements of nums between indices left and right inclusive where left <= right.
Implement the NumArray class:
NumArray(int[] nums) Initializes the object with the integer array nums.
int sumRange(int left, int right) Returns the sum of the elements of nums between indices left and right inclusive
(i.e. nums[left] + nums[left + 1] + ... + nums[right]).

Example 1:
Input
["NumArray", "sumRange", "sumRange", "sumRange"]
[[[-2, 0, 3, -5, 2, -1]], [0, 2], [2, 5], [0, 5]]
Output
[null, 1, -1, -3]
"""


# Solution_1 - slow
class NumArray1:
    def __init__(self, nums: list[int]):
        self.nums = nums

    def sumRange(self, left: int, right: int) -> int:
        return sum(self.nums[left:right+1])


# Solution_2 - faster
class NumArray:
    def __init__(self, nums: list[int]):
        self.acc_nums = [0]
        for num in nums:
            self.acc_nums.append(self.acc_nums[-1] + num)

    def sumRange(self, left: int, right: int) -> int:
        return self.acc_nums[right+1] - self.acc_nums[left]
