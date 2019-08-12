#!/usr/bin/python3

# @Project = step_LeetCode
# @File    : 1155_Number_of_Dice_Rolls_With_Target_Sum
# @Author  : TCY
# @Time    : 2019/8/11 22:08
# @Email   : tangcaiyuan@hust.edu.cn
# @Software: PyCharm


class Solution:
    def numRollsToTarget(self, d: int, f: int, target: int) -> int:
        md = 10 ** 9 + 7
        dp = [[0 for _ in range(target + 1)] for _ in range(d + 1)]
        # dp[d][target] -> d个色子目标为target有的种类
        # dp[i][j] = dp[i-1][j-1] + dp[d-1][j-2] + ... + dp[d-1][j-f]
        dp[0][0] = 1
        for m in range(1, f + 1):
            if m <= target:
                dp[1][m] = 1
        for i in range(2, d + 1):
            for j in range(i, target + 1):
                for k in range(1, f + 1):
                    if j - k >= 0:
                        dp[i][j] = (dp[i][j] + dp[i - 1][j - k]) % md

        return dp[d][target]


