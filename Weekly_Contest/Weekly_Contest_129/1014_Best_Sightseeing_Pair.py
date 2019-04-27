#!/usr/bin/python3

# @Project = step_LeetCode
# @File    : 1014_Best_Sightseeing_Pair
# @Author  : TCY
# @Time    : 2019/4/27 15:05
# @Email   : tangcaiyuan@hust.edu.cn
# @Software: PyCharm


class Solution:
    def maxScoreSightseeingPair(self, A):
        """A[i]+A[j]+i-j = (A[i]+i) + (A[j]-j)
        枚举j，A[j]-j,并加上A[i]+i，其中i<j
        """
        n = len(A)
        ans = A[0] + A[1] - 1
        mx = A[0] + 0
        for i in range(1, n):
            ans = max(A[i] - i + mx, ans)
            mx = max(mx, A[i] + i)
        return ans
