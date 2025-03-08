"""
https://leetcode.com/problems/longest-mountain-in-array/description/
845. Longest Mountain in Array

You may recall that an array arr is a mountain array if and only if:
arr.length >= 3
There exists some index i (0-indexed) with 0 < i < arr.length - 1 such that:
arr[0] < arr[1] < ... < arr[i - 1] < arr[i]
arr[i] > arr[i + 1] > ... > arr[arr.length - 1]

Given an integer array arr, return the length of the longest subarray, which is a mountain.
Return 0 if there is no mountain subarray.

Example 1:
Input: arr = [2,1,4,7,3,2,5]
Output: 5
Explanation: The largest mountain is [1,4,7,3,2] which has length 5.
"""


class Solution:
    def longestMountain(self, arr: list[int]) -> int:
        answer = 0

        for i in range(1, len(arr) - 1):
            if arr[i-1] < arr[i] > arr[i+1]:
                l = r = i
                while l > 0 and arr[l] > arr[l-1]:
                    l -= 1

                while r < len(arr) - 1 and arr[r] > arr[r+1]:
                    r += 1
                answer = max(answer, r - l + 1)

        return answer


solution = Solution()
print(solution.longestMountain([0,1,2,3,4,5,4,3,2,1,0]))
