#!/usr/bin/python3

# @Project = step_LeetCode
# @File    : 1143_Longest_Common_Subsequence
# @Author  : TCY
# @Time    : 2019/8/10 0:03
# @Email   : tangcaiyuan@hust.edu.cn
# @Software: PyCharm

"""
求两个字符串相同的最长子序列
dp[i][j] 表示 text1[:i] 和 text2[:j] 的最长子序列长度

if a[-1] == b[-1]:
    dp[i][j] = dp[i-1][j-1] + 1
else:
    dp[i][j] = max(dp[i-1][j], dp[i][j-1])
"""

class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        n, m = len(text1), len(text2)
        dp = [[0 for _ in range(m+1)] for _ in range(n+1)]
        for i in range(1, n+1):
            for j in range(1, m+1):
                a = text1[:i]
                b = text2[:j]
                if a[-1] == b[-1]:
                    dp[i][j] = dp[i-1][j-1] + 1
                else:
                    dp[i][j] = max(dp[i-1][j], dp[i][j-1])
        return dp[n][m]