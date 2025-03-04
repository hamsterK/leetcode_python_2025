"""
https://leetcode.com/problems/spiral-matrix/description/
54. Spiral Matrix

Given an m x n matrix, return all elements of the matrix in spiral order.

Example 1:
Input: matrix = [[1,2,3],[4,5,6],[7,8,9]]
Output: [1,2,3,6,9,8,7,4,5]
"""


class Solution:
    def spiralOrder(self, matrix: list[list[int]]) -> list[int]:
        if len(matrix[0]) == 1:
            return [i[0] for i in matrix]

        answer = []
        while len(matrix) != 0:

            # step 1
            answer.extend(matrix[0])
            del matrix[0]
            if len(matrix) == 0:
                break

            # step 2
            for i in range(len(matrix)):
                answer.append(matrix[i].pop(-1))
            for i in reversed(range(len(matrix))):
                if len(matrix[i]) == 0:
                    del matrix[i]
            if len(matrix) == 0:
                break

            # step 3
            answer.extend(reversed(matrix[-1]))
            del matrix[-1]
            if len(matrix) == 0:
                break

            # step 4
            for i in reversed(range(len(matrix))):
                answer.append(matrix[i].pop(0))
                if len(matrix[i]) == 0:
                    del matrix[i]

        return answer


solution = Solution()
print(solution.spiralOrder([[2,3,4],[5,6,7],[8,9,10],[11,12,13],[14,15,16]]))
