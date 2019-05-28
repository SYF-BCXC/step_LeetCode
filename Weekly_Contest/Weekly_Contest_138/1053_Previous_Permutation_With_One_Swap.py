#!/usr/bin/python3

# @Project = step_LeetCode
# @File    : 1053_Previous_Permutation_With_One_Swap
# @Author  : TCY
# @Time    : 2019/5/27 16:41
# @Email   : tangcaiyuan@hust.edu.cn
# @Software: PyCharm


class Solution:
    def prevPermOpt1(self, A: List[int]) -> List[int]:
        """i和j尽可能往后面取，同时A[i] > A[j]"""
        n = len(A)
        loc = n - 1
        for i in range(n - 1, -1, -1):
            if i > 0 and A[i - 1] > A[i]:
                loc = i - 1
                break
        loc2 = n - 1
        for i in range(loc + 1, n):
            """找最后一个小于他的值"""
            if A[i] >= A[loc]:
                loc2 = i - 1
                break
        A[loc], A[loc2] = A[loc2], A[loc]
        return A
