#!/usr/bin/python3

# @Project = leetCode
# @File    : 1_two_sum
# @Author  : TCY
# @Time    : 2018/9/15 0:25
# @Email   : tangcaiyuan@hust.edu.cn
# @Software: PyCharm

"""
题目描述:
https://leetcode-cn.com/problems/two-sum/description/
思路:
1、扫描nums数组。lookup存放扫描过的数字，目标值target - 当前扫描的数字，如果该数字在lookup中就返回这一组数，如果不在则添加到lookup数组中去。
"""

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
