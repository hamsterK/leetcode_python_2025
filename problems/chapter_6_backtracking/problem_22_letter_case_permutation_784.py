"""
https://leetcode.com/problems/letter-case-permutation/description/
784. Letter Case Permutation

Given a string s, you can transform every letter individually to be lowercase or uppercase to create another string.
Return a list of all possible strings we could create. Return the output in any order.

Example 1:
Input: s = "a1b2"
Output: ["a1b2","a1B2","A1b2","A1B2"]
"""


class Solution:
    def letterCasePermutation(self, s: str) -> list[str]:
        res = []

        def backtrack(sub="", i=0):
            # print("Sub", sub, "i:", i)
            if len(sub) == len(s):
                res.append(sub)
                return

            if s[i].isalpha():
                backtrack(sub + s[i].swapcase(), i + 1)
            backtrack(sub + s[i], i + 1)

        backtrack()
        return res


solution = Solution()
print(solution.letterCasePermutation("a1b2"))
