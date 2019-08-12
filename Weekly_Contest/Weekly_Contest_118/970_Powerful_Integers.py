#!/usr/bin/python3

# @Project = step_LeetCode
# @File    : 970_Powerful_Integers
# @Author  : TCY
# @Time    : 2019/8/12 11:55
# @Email   : tangcaiyuan@hust.edu.cn
# @Software: PyCharm


class Solution:
    def powerfulIntegers(self, x: int, y: int, bound: int) -> List[int]:
        if x == 1 and y == 1:
            if bound < 2:
                return []
            return [2]

        xpow, ypow = 1, 1
        ans = set()
        if x == 1:
            while xpow + ypow <= bound:
                ans.add(xpow + ypow)
                ypow = ypow * y
            return ans

        if y == 1:
            while xpow + ypow <= bound:
                ans.add(xpow + ypow)
                xpow = xpow * x
            return ans

        while xpow + ypow <= bound:
            while xpow + ypow <= bound:
                ans.add(xpow + ypow)
                ypow = ypow * y
            ypow = 1
            xpow = xpow * x
        return list(ans)