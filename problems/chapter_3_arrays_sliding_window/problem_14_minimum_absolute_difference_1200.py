"""
https://leetcode.com/problems/minimum-absolute-difference/description/
1200. Minimum Absolute Difference

Given an array of distinct integers arr, find all pairs of elements with the minimum absolute difference of any two elements.
Return a list of pairs in ascending order(with respect to pairs), each pair [a, b] follows
a, b are from arr
a < b
b - a equals to the minimum absolute difference of any two elements in arr

Example 1:
Input: arr = [4,2,1,3]
Output: [[1,2],[2,3],[3,4]]
Explanation: The minimum absolute difference is 1. List all pairs with difference equal to 1 in ascending order.
"""


#slow solution
class Solution1:
    def minimumAbsDifference(self, arr: list[int]) -> list[list[int]]:
        arr.sort()
        answers = dict()
        for i in range(len(arr) - 1):
            answers.setdefault(arr[i+1] - arr[i], []).append([arr[i], arr[i+1]])
        return min(answers.items(), key=lambda x: x[0])[1]


# faster solution
class Solution:
    def minimumAbsDifference(self, arr: list[int]) -> list[list[int]]:
        arr.sort()
        answers = list()
        min_dif = float('inf')  # an infinite integer
        for i in range(len(arr) - 1):
            current_dif = arr[i+1] - arr[i]
            if current_dif < min_dif:
                min_dif = current_dif
                answers = [[arr[i], arr[i+1]]]
            elif current_dif == min_dif:
                answers.append([arr[i], arr[i+1]])

        return answers


solution = Solution()
print(solution.minimumAbsDifference([40,11,26,27,-20]))
