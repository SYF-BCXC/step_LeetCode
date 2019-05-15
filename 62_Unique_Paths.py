#!/usr/bin/python3

# @Project = step_LeetCode
# @File    : 62_Unique_Paths
# @Author  : TCY
# @Time    : 2019/5/15 15:23
# @Email   : tangcaiyuan@hust.edu.cn
# @Software: PyCharm


class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        """动态规划"""
        dp = [1 for _ in range(n)]
        for i in range(1,m):
            for j in range(1,n):
                dp[j] = dp[j] + dp[j-1]
        return dp[n-1]
        '''
        """Cm+n-2选m-1"""
        a,b = m+n-2, min(m,n)-1
        ans = 1
        for i in range(b):
            ans = ans * (a-i) // (i+1)
        return ans
        '''