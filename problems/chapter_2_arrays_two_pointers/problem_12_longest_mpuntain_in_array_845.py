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
        if len(arr) < 3:
            return 0
        answer = 0
        left = arr.pop()
        counter = 0
        flag_descend = False
        while arr:
            right = left
            left = arr.pop()
            if right < left:
               counter += 1
            elif right > left and counter >= 1:
                flag_descend = True
                counter += 1
                if len(arr) == 0:
                    counter += 1
            else:
                answer = max(answer, counter) if (counter >= 3 and flag_descend) else 0
                counter = 0

        answer = max(answer, counter) if (counter >= 3 and flag_descend) else 0

        return answer


solution = Solution()
print(solution.longestMountain([0,2,0,2,1,2,3,4,4,1]))
