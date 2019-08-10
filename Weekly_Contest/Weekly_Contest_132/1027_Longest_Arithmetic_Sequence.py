#!/usr/bin/python3

# @Project = step_LeetCode
# @File    : 1027_Longest_Arithmetic_Sequence
# @Author  : TCY
# @Time    : 2019/8/10 11:21
# @Email   : tangcaiyuan@hust.edu.cn
# @Software: PyCharm

class Solution:
    def longestArithSeqLength(self, A: List[int]) -> int:
        dp = {}
        for i in range(len(A)):
            for j in range(i+1, len(A)):
                a, b = A[i], A[j]
                dp[a-b, j] = dp.get((a-b, i),1) + 1
                # print("差为%d,结束位置为%d, 结束值为%d, 长度为%d" %(a-b, j, b, dp[a-b,j]))
        return max(dp.values())