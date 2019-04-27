#!/usr/bin/python3

# @Project = step_LeetCode
# @File    : 1013_Partition_Array_Into_Three_Parts_With_Equal_Sum
# @Author  : TCY
# @Time    : 2019/4/27 13:15
# @Email   : tangcaiyuan@hust.edu.cn
# @Software: PyCharm

class Solution:
    def canThreePartsEqualSum(self, A):
        flag1, flag2 = 0, 0
        l = len(A)
        all_sum = 0
        for i in range(l):
            all_sum += A[i]
        if all_sum % 3 != 0:
            return False
        sum1, sum2 = 0, 0
        for i in range(l):
            if sum1 == all_sum // 3:
                flag1 = i
                break
            else:
                sum1 += A[i]
        for i in range(flag1, l):
            if sum2 == all_sum // 3:
                flag2 = i
                return True
            else:
                sum2 += A[i]
        return False
