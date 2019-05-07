#!/usr/bin/python3

# @Project = step_LeetCode
# @File    : 5047_Minimum_Score_Triangulation_of_Polygon
# @Author  : TCY
# @Time    : 2019/5/6 10:38
# @Email   : tangcaiyuan@hust.edu.cn
# @Software: PyCharm


class Solution:
    def minScoreTriangulation(self, A: List[int]) -> int:
        n = len(A)
        dp = [[0 for _ in range(n)] for _ in range(n)]
        """目标是dp[1][n-1]"""
        """i == j , 0"""
        for i in range(1, n):
            for j in range(1, n):
                if i + j >= n:
                    pass
                else:
                    tmp_min = 0xfffffff
                    """[j][j+i]"""
                    for k in range(j, j + i):
                        tmp = dp[j][k] + dp[k + 1][i + j] + A[j - 1] * A[k] * A[i + j]
                        if tmp < tmp_min:
                            tmp_min = tmp
                    dp[j][j + i] = tmp_min
        return dp[1][n - 1]
