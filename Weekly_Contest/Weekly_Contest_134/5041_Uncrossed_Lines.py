#!/usr/bin/python3

# @Project = step_LeetCode
# @File    : 5041_Uncrossed_Lines
# @Author  : TCY
# @Time    : 2019/4/28 14:42
# @Email   : tangcaiyuan@hust.edu.cn
# @Software: PyCharm

"""直接动态规划"""
class Solution:
    def maxUncrossedLines(self, A, B):
        vis = []
        for i in range(len(A) + 1):
            tmp = []
            for j in range(len(B) + 1):
                tmp.append(0)
            vis.append(tmp)
        for i in range(1, len(A) + 1):
            for j in range(1, len(B) + 1):
                if A[i - 1] == B[j - 1]:
                    vis[i][j] = vis[i - 1][j - 1] + 1
                else:
                    vis[i][j] = max(vis[i - 1][j], vis[i][j - 1])
        return vis[-1][-1]
