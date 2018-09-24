#!/usr/bin/python3

# @Project = leetCode
# @File    : 1_two_sum
# @Author  : TCY
# @Time    : 2018/9/15 0:25
# @Email   : tangcaiyuan@hust.edu.cn
# @Software: PyCharm


def two_sum(nums, target):
    """
    :type nums: List[int]
    :type target: int
    :rtype: List[int]
    """
    lookup = {}
    for i, num in enumerate(nums):
        if target - num in lookup:
            return [lookup[target - num], i]
        lookup[num] = i


print(two_sum([2, 7, 11, 15], 9))
