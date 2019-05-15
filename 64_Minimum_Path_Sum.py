#!/usr/bin/python3

# @Project = step_LeetCode
# @File    : 64_Minimum_Path_Sum
# @Author  : TCY
# @Time    : 2019/5/15 15:25
# @Email   : tangcaiyuan@hust.edu.cn
# @Software: PyCharm

class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        """动态规划法。
        1. 原问题：从左上走到n,n;子问题：从左上走到i,j
        2. 状态：dp[i][j]表示从0,0到i,j最小路径和
        3. 初始化：dp[0][0] = grid[0][0],dp[i][0]为0列前i个的和，dp[0][j]为0行前j个元素和
        4. 动态转移方程： dp[i][j]= min(dp[i-1][j],dp[i][j-1])+grid[i][j]
        """
        '''
        if not grid:
            return 0
        n,m = len(grid),len(grid[0])
        dp = [[0 for _ in range(m)]for _ in range(n)]
        dp[0][0]=grid[0][0]
        for i in range(1,n):
            dp[i][0] = dp[i-1][0]+grid[i][0]
        for j in range(1,m):
            dp[0][j] = dp[0][j-1] + grid[0][j]
        for i in range(1,n):
            for j in range(1,m):
                dp[i][j]= min(dp[i-1][j],dp[i][j-1])+grid[i][j]
        return dp[n-1][m-1]
        '''
        """空间优化,dp[j] = min(dp[j],dp[j-1])+grid[i][j](时间上的差距，新旧)"""
        if not grid:
            return 0
        n, m = len(grid), len(grid[0])
        dp = [0 for _ in range(m)]
        dp[0] = grid[0][0]
        for j in range(1, m):
            dp[j] = dp[j - 1] + grid[0][j]
        for i in range(1, n):
            for j in range(0, m):
                if j > 0:
                    dp[j] = min(dp[j], dp[j - 1]) + grid[i][j]
                else:
                    dp[j] = dp[j] + grid[i][j]
        return dp[m - 1]

