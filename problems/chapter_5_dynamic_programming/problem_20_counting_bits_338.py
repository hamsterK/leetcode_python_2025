"""
https://leetcode.com/problems/counting-bits/description/
338. Counting Bits

Given an integer n, return an array ans of length n + 1 such that for each i (0 <= i <= n),
ans[i] is the number of 1's in the binary representation of i.

Example 1:
Input: n = 2
Output: [0,1,1]
Explanation:
0 --> 0
1 --> 1
2 --> 10
"""


# solution 1
class Solution1:
    def countBits(self, n: int) -> list[int]:
        answer = []
        for i in range(n+1):
            answer.append(bin(i).count('1'))
        return answer


# solution 2 - fast
class Solution:
    def countBits(self, n: int) -> list[int]:
        dp = [0] * (n + 1)
        offset = 1

        for i in range(1, n + 1):
            if offset * 2 == i:
                offset = i

            dp[i] = 1 + dp[i-offset]

        return dp


solution = Solution()
print(solution.countBits(5))