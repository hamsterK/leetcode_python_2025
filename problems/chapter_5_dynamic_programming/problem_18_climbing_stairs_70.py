"""
https://leetcode.com/problems/climbing-stairs/description/
70. Climbing Stairs

You are climbing a staircase. It takes n steps to reach the top.
Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?

Example 1:
Input: n = 2
Output: 2
Explanation: There are two ways to climb to the top.
1. 1 step + 1 step
2. 2 steps
"""


class Solution:
    def climbStairs(self, n: int) -> int:
        answer = []
        for i in range(n):
            if i == 0:
                answer.append(1)
            elif i == 1:
                answer.append(2)
            else:
                answer.append(answer[i-2] + answer[i-1])

        return answer[-1]


solution = Solution()
print(solution.climbStairs(4))
