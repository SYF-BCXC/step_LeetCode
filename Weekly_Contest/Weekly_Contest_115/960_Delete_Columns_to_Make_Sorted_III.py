#!/usr/bin/python3

# @Project = step_LeetCode
# @File    : 960_Delete_Columns_to_Make_Sorted_III
# @Author  : TCY
# @Time    : 2019/8/11 10:00
# @Email   : tangcaiyuan@hust.edu.cn
# @Software: PyCharm


"""
思路：
每列既然是一起删除和比较的，就将整列作为一个元素。这样问题变成了，最长上升子序列问题，即用dp解决。
"""

class Solution:
    def minDeletionSize(self, A: List[str]) -> int:
        n, m = len(A), len(A[0])
        cmp = [[False for _ in range(m)] for _ in range(m)]   # 第i列 <= 第j列
        for i in range(m):
            for j in range(m):
                tmp = True
                for k in range(n):
                    if A[k][i] > A[k][j]:
                        tmp = False
                        break
                cmp[i][j] = tmp
        dp = [1 for _ in range(m+1)]
        dp[0] = 1
        for i in range(1,m):
            for j in range(0, i):
                if cmp[j][i]:
                    dp[i] = max(dp[i],dp[j] + 1)
        return m - max(dp)