#!/usr/bin/python3

# @Project = step_LeetCode
# @File    : 5051_Valid_Boomerang
# @Author  : TCY
# @Time    : 2019/5/6 10:36
# @Email   : tangcaiyuan@hust.edu.cn
# @Software: PyCharm

class Solution:
    def isBoomerang(self, points: List[List[int]]) -> bool:
        if (points[2][1]-points[1][1])*(points[1][0]-points[0][0]) != (points[1][1]-points[0][1]) * (points[2][0]-points[1][0]):
            return True
        else:
            return False