#!/usr/bin/python3

# @Project = step_LeetCode
# @File    : 959_Regions_Cut_By_Slashes
# @Author  : TCY
# @Time    : 2019/8/11 9:59
# @Email   : tangcaiyuan@hust.edu.cn
# @Software: PyCharm

"""
类似于数岛屿的题，这里用并查集

"""

class Solution:
    def regionsBySlashes(self, grid: List[str]) -> int:
        N = len(grid)
        ll = N * N * 4
        f = list(range(ll))
        self.count = ll

        def find(x):
            if f[x] != x:
                f[x] = find(f[x])
            return f[x]

        def union(x, y):
            x, y = find(x), find(y)
            if x != y:
                f[x] = y
                self.count -= 1

        def g(x, y, k):
            return (N * x + y) * 4 + k

        for i in range(N):
            for j in range(N):
                if i > 0:
                    union(g(i, j, 0), g(i - 1, j, 2))
                if j > 0:
                    union(g(i, j, 3), g(i, j - 1, 1))
                if grid[i][j] == '\\':
                    union(g(i, j, 0), g(i, j, 1))
                    union(g(i, j, 2), g(i, j, 3))
                elif grid[i][j] == '/':
                    union(g(i, j, 0), g(i, j, 3))
                    union(g(i, j, 1), g(i, j, 2))
                elif grid[i][j] == ' ':
                    union(g(i, j, 0), g(i, j, 1))
                    union(g(i, j, 2), g(i, j, 3))
                    union(g(i, j, 0), g(i, j, 3))
        return self.count
