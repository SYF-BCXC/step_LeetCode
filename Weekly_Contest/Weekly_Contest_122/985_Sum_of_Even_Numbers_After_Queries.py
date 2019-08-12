#!/usr/bin/python3

# @Project = step_LeetCode
# @File    : 985_Sum_of_Even_Numbers_After_Queries
# @Author  : TCY
# @Time    : 2019/8/13 0:13
# @Email   : tangcaiyuan@hust.edu.cn
# @Software: PyCharm

class Solution:
    def sumEvenAfterQueries(self, A: List[int], queries: List[List[int]]) -> List[int]:
        s = sum(a for a in A if a % 2 == 0)
        ans = []
        for i,j in queries:
            if A[j] % 2 == 0: s -= A[j]
            A[j] = A[j] + i
            if A[j] % 2 == 0: s += A[j]
            ans.append(s)
        return ans