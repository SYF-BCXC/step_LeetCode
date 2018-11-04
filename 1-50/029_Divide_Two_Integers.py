#!/usr/bin/python3

# @Project = step_LeetCode
# @File    : 029_Divide_Two_Integers
# @Author  : TCY
# @Time    : 2018/11/4 14:22
# @Email   : tangcaiyuan@hust.edu.cn
# @Software: PyCharm


"""
题目描述:
https://leetcode-cn.com/problems/divide-two-integers/description/
思路:
（超时)1、用减法。先都abs()变正数，然后减法，直到被除数为负停止，记录减法次数，最后根据两数正负添加符号。
2、二分法。将除数用加法一次次累加起来，找到第一个大于被除数的值。如：100/3 = 33。
    我们构造:[3 6 12 24 48 96 192]，第一个大于100的为192，所以我们锁定其前一个96=3*(2^5)。然后
    100 - 96 = 4，用同样的方法，找到数组中的3=3*(2^0)。然后4-3 = 1，小于数组中最小值3，停止。
    而结果就是 (2^5 + 2^0) = 33

    此题不让用乘法除法和取余但是最快答案就是用的除法，最快52ms
"""


class Solution:
    # 思路1，超时
    def divide(self, dividend, divisor):
        """
        :type dividend: int
        :type divisor: int
        :rtype: int
        """
        flag = 0  # 标识最后结果正负，0和2表示为正，1表示为负
        rst = 0
        if dividend < 0:
            flag, dividend = flag + 1, -dividend
        if divisor < 0:
            flag, divisor = flag + 1, -divisor
        if divisor == 0:
            return -1
        if divisor == 1:
            return dividend
        while dividend >= 0:
            dividend = dividend - divisor
            rst += 1
        if flag == 1:
            return -(rst - 1)
        else:
            return rst - 1

    # 思路2，用时64ms
    def divide2(self, dividend, divisor):
        flag = 0  # 标识最后结果正负，0和2表示为正，1表示为负
        if dividend < 0:
            flag, dividend = flag + 1, -dividend
        if divisor < 0:
            flag, divisor = flag + 1, -divisor
        if divisor == 0:
            return -1
        tmp = [divisor]
        rst, point = 0, 0
        # 开始构造数组
        while tmp[-1] <= dividend:
            tmp.append(tmp[-1] + tmp[-1])
            point += 1
        # 构造答案
        while dividend >= tmp[0]:
            if tmp[point] > dividend:
                point -= 1
            else:
                # tmp[point] <= dividend
                rst += 2 ** point
                dividend -= tmp[point]
        if flag == 1:
            rst = -rst
        else:
            rst = rst
        if rst > 2 ** 31 - 1:
            return 2 ** 31 - 1
        if rst < -(2 ** 31):
            return -(2 ** 31)
        return rst


if __name__ == '__main__':
    print(Solution().divide2(-2147483648, -2))
