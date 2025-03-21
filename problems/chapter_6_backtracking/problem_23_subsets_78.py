"""
https://leetcode.com/problems/subsets/
78. Subsets

Given an integer array nums of unique elements, return all possible subsets (the power set).
The solution set must not contain duplicate subsets. Return the solution in any order.

Example 1:
Input: nums = [1,2,3]
Output: [[],[1],[2],[1,2],[3],[1,3],[2,3],[1,2,3]]
"""


class Solution:
    def subsets(self, nums: list[int]) -> list[list[int]]:
        def backtrack(start, path):

            result.append(path[:])
            for i in range(start, len(nums)):
                path.append(nums[i])
                backtrack(i+1, path)
                path.pop()

        result = []
        backtrack(0, [])
        return result


solution = Solution()
print(solution.subsets([1, 2, 3]))
