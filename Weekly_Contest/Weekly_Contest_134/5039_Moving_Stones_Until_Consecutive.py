#!/usr/bin/python3

# @Project = step_LeetCode
# @File    : 5039_Moving_Stones_Until_Consecutive
# @Author  : TCY
# @Time    : 2019/4/28 14:31
# @Email   : tangcaiyuan@hust.edu.cn
# @Software: PyCharm


class Solution:
    def numMovesStones(self, a: int, b: int, c: int):
        """先让abc有序"""
        a, b, c = sorted([a, b, c])
        miny, maxy = 2, 0
        """计算最多移动次数，两边往中间一步一步移动次数最多"""
        maxy = (b - a - 1) + (c - b - 1)
        """计算最少移动次数，其中两个位置相距为1和2最为独特。
        两个距离为2，总次数为1
        一个距离为2，总次数必定为1
        两个距离为1，总次数为0
        一个距离为1，总次数必定为1
        对于其他，都大于2的情况，总次数则直接为2
        """
        count1 = 0
        count2 = 0
        if b - a == 2:
            count2 += 1
        if b - a == 1:
            count1 += 1
        if c - b == 1:
            count1 += 1
        if c - b == 2:
            count2 += 1
        if count2 >= 1:
            miny = 1
        if count1 == 2:
            miny = 0
        if count1 == 1:
            miny = 1
        return [miny, maxy]
