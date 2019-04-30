#!/usr/bin/python3

# @Project = step_LeetCode
# @File    : 5040_Coloring_A_Border
# @Author  : TCY
# @Time    : 2019/4/28 14:40
# @Email   : tangcaiyuan@hust.edu.cn
# @Software: PyCharm


class Solution:
    def colorBorder(self, grid, r0, c0, color):
        """连通分量的边界，用DFS"""
        n, m = len(grid), len(grid[0])
        dx = [0, 0, -1, 1]
        dy = [1, -1, 0, 0]
        bianjie = [[False for _ in range(m)] for _ in range(n)]
        havepass = [[False for _ in range(m)] for _ in range(n)]
        """写DFS，先确定搜索范围，再根据情况打标记(vis数组，访问了一定要标记上，否则会一直递归至溢出)，最后写递归部分"""

        def DFS(r, c, color):
            flag = False
            if r == 0 or r == n - 1 or c == 0 or c == m - 1:
                bianjie[r][c] = True
            else:
                for i in range(4):
                    tmpx = r + dx[i]
                    tmpy = c + dy[i]
                    if grid[r][c] != grid[tmpx][tmpy]:
                        flag = True
            if flag:
                bianjie[r][c] = True
            havepass[r][c] = True
            for i in range(4):
                tmpx = r + dx[i]
                tmpy = c + dy[i]
                if (tmpx >= 0 and tmpx < n and tmpy >= 0 and tmpy < m) and havepass[tmpx][tmpy] == False and grid[tmpx][
                    tmpy] == color:
                    DFS(tmpx, tmpy, color)

        DFS(r0, c0, grid[r0][c0])
        for i in range(n):
            for j in range(m):
                if bianjie[i][j]:
                    grid[i][j] = color
        return grid
