#!/usr/bin/python3

# @Project = step_LeetCode
# @File    : 015_3Sum
# @Author  : TCY
# @Time    : 2018/9/28 23:06
# @Email   : tangcaiyuan@hust.edu.cn
# @Software: PyCharm

"""
题目描述:
https://leetcode-cn.com/problems/3sum/description/
思路:
1、暴力法。O(n^3)，时间复杂度太高
2、排序后，用双指针法。指针分别指向a和b，设有abs(a)>abs(b)。
    若abs(a)>2*abs(b)，则a的指针+1
    若abs(a) == 2*abs(b)，则 若b的指针-1等于b，有一组返回值
    若abs(a) < 2*abs(b)，则b的指针靠内搜索
    直到两个指针重合，搜索完成
"""


class Solution:
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """


if __name__ == '__main__':
    print(Solution().threeSum())