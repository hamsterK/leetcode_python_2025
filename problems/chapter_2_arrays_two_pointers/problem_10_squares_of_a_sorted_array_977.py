"""
https://leetcode.com/problems/squares-of-a-sorted-array/description/
977. Squares of a Sorted Array

Given an integer array nums sorted in non-decreasing order,
return an array of the squares of each number sorted in non-decreasing order.

Example 1:
Input: nums = [-4,-1,0,3,10]
Output: [0,1,9,16,100]
Explanation: After squaring, the array becomes [16,1,0,9,100].
After sorting, it becomes [0,1,9,16,100].
"""


#  solution 1
class Solution1:
    def sortedSquares(self, nums: list[int]) -> list[int]:
        return sorted([i**2 for i in nums])


#  solution with 2-pointer
class Solution:
    def sortedSquares(self, nums: list[int]) -> list[int]:
        answer = []
        l, r = 0, len(nums) - 1
        while l <= r:
            left, right = abs(nums[l]), abs(nums[r])
            if left > right:
                answer.append(left ** 2)
                l += 1
            else:
                answer.append(right ** 2)
                r -= 1
        return answer[::-1]


solution = Solution()
print(solution.sortedSquares([-4,-1,0,3,10]))
