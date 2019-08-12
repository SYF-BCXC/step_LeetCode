#!/usr/bin/python3

# @Project = step_LeetCode
# @File    : 976_Largest_Perimeter_Triangle
# @Author  : TCY
# @Time    : 2019/8/12 11:13
# @Email   : tangcaiyuan@hust.edu.cn
# @Software: PyCharm


class Solution:
    # 关键在于有序会方便
    # a <= b <= c
    # a + b > c
    def largestPerimeter(self, A: List[int]) -> int:
        A.sort()
        for i in range(len(A)-1, 1, -1):
            if A[i] < A[i-1] + A[i-2]:
                return A[i] + A[i-1] + A[i-2]
        return 0