"""
http://leetcode.com/problems/number-of-islands/description/
200. Number of Islands

Given an m x n 2D binary grid which represents a map of '1's (land) and '0's (water), return the number of islands.
An island is surrounded by water and is formed by connecting adjacent lands horizontally or vertically.
You may assume all four edges of the grid are all surrounded by water.

Example 1:
Input: grid = [
  ["1","1","1","1","0"],
  ["1","1","0","1","0"],
  ["1","1","0","0","0"],
  ["0","0","0","0","0"]
]
Output: 1
"""


class Solution:
    def numIslands(self, grid: list[list[str]]) -> int:
        if not grid:
            return 0

        counter = 0

        def check_neighbours(i, j):
            queue = set()
            directions = ((1, 0), (-1, 0), (0, 1), (0, -1))
            for el in directions:
                new_el = (i + el[0], j + el[1])
                if (new_el[0] in range(0, len(grid)) and new_el[1] in range(0, len(grid[0]))
                        and grid[new_el[0]][new_el[1]] == "1"):
                    grid[new_el[0]][new_el[1]] = "0"
                    queue.add(new_el)

            for el in queue:
                check_neighbours(el[0], el[1])
            queue.clear()

        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if (i, j) != "0" and grid[i][j] == "1":
                    counter += 1
                    check_neighbours(i, j)

        return counter


solution = Solution()
print(solution.numIslands(grid = [
  ["1","1","1","1","0"],
  ["1","1","0","1","0"],
  ["1","1","0","0","0"],
  ["0","0","0","0","0"]
]))
