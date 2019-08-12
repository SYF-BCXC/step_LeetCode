#!/usr/bin/python3

# @Project = step_LeetCode
# @File    : 986_Interval_List_Intersections
# @Author  : TCY
# @Time    : 2019/8/13 0:17
# @Email   : tangcaiyuan@hust.edu.cn
# @Software: PyCharm


class Solution:
    # [a,b] 和 [c, d]要相交的条件. a <= d and c <= b
    def intervalIntersection(self, A: List[List[int]], B: List[List[int]]) -> List[List[int]]:
        i = j = 0
        ans = []
        while i < len(A) and j < len(B):
            a, b = A[i][0], A[i][1]
            c, d = B[j][0], B[j][1]
            if a <= d and c <= b:
                ans.append([max(a, c), min(b, d)])
            if b < d:
                i += 1
            else:
                j += 1
        return ans

