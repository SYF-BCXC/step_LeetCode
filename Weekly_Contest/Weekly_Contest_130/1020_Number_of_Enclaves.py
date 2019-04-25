#!/usr/bin/python3

# @Project = step_LeetCode
# @File    : 1020_Number_of_Enclaves
# @Author  : TCY
# @Time    : 2019/4/25 15:38
# @Email   : tangcaiyuan@hust.edu.cn
# @Software: PyCharm

import queue

"""  一点小情况：测试时变量声明在类外没什么问题，但是提交有问题，放入类内就通过了，估计用全局变量被多次测试污染了

# 必用变量
vis = [[False] * 505 for _ in range(505)]
que = queue.Queue()
dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]
"""

def numEnclaves(A):
    # 必用变量
    vis = [[False] * 505 for _ in range(505)]
    que = queue.Queue()
    dx = [0, 0, 1, -1]
    dy = [1, -1, 0, 0]
    """先得到维度，并初始化"""
    n, m = len(A), len(A[0])
    for i in range(n):
        if A[i][0] == 1:
            vis[i][0] = True
            que.put((i, 0))
        if A[i][m - 1] == 1:
            vis[i][m - 1] = True
            que.put((i, m - 1))
    for i in range(m):
        if A[0][i] == 1:
            vis[0][i] = True
            que.put((0, i))
        if A[n - 1][i] == 1:
            vis[n - 1][i] = True
            que.put((n - 1, i))
    while not que.empty():
        x, y = que.get()
        for i in range(4):
            tmpx, tmpy = x + dx[i], y + dy[i]
            if tmpx < 0 or tmpx >= n or tmpy < 0 or tmpy >= m:
                continue
            if (not vis[tmpx][tmpy]) and A[tmpx][tmpy] == 1:
                vis[tmpx][tmpy] = True
                que.put((tmpx, tmpy))
    ans = 0
    for i in range(n):
        for j in range(m):
            if (not vis[i][j]) and A[i][j] == 1:
                ans += 1
    return ans


A = [[0, 0, 1, 1, 1, 0, 1, 1, 1, 0, 1], [1, 1, 1, 1, 0, 1, 0, 1, 1, 0, 0], [0, 1, 0, 1, 1, 0, 0, 0, 0, 1, 0],
     [1, 0, 1, 1, 1, 1, 1, 0, 0, 0, 1], [0, 0, 1, 0, 1, 1, 0, 0, 1, 0, 0], [1, 0, 0, 1, 1, 1, 0, 0, 0, 1, 1],
     [0, 1, 0, 1, 1, 0, 0, 0, 1, 0, 0], [0, 1, 1, 0, 1, 0, 1, 1, 1, 0, 0], [1, 1, 0, 1, 1, 1, 0, 0, 0, 0, 0],
     [1, 0, 1, 1, 0, 0, 0, 1, 0, 0, 1]]
print(numEnclaves(A))
