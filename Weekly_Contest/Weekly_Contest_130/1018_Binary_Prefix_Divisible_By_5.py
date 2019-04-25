#!/usr/bin/python3

# @Project = step_LeetCode
# @File    : 1018_Binary_Prefix_Divisible_By_5
# @Author  : TCY
# @Time    : 2019/4/25 15:37
# @Email   : tangcaiyuan@hust.edu.cn
# @Software: PyCharm


class Solution(object):
    def prefixesDivBy5(self, A):
        """
        :type A: List[int]
        :rtype: List[bool]
        """
        result = []
        rate = 0
        for i in range(len(A)):
            rate = rate * 2 + A[i]
            result.append(rate % 5 == 0)
        return result
