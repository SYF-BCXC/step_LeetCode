#!/usr/bin/python3

# @Project = step_LeetCode
# @File    : 1011_Capacity_To_Ship_Packages_Within_Days
# @Author  : TCY
# @Time    : 2019/4/30 14:56
# @Email   : tangcaiyuan@hust.edu.cn
# @Software: PyCharm


class Solution:
    def shipWithinDays(self, weights: List[int], D: int) -> int:
        """二分搜索。
        下限：最大值
        上限：总和
        """

        def cando(weights, w, d):
            idx = 0
            tmp = 0
            """若未超重，就加入tmp；若超重，则将tmp置为当前值，并将d--;如果d<0且还没有遍历结束，返回失败。如果d>=0并且遍历结束，则返回true"""
            for i in weights:
                if d <= 0:
                    return False
                tmp += i
                if tmp > w:
                    tmp = i
                    d -= 1
            if d > 0:
                return True
            else:
                return False

        # print(cando(weights,15,D))
        l, r = max(weights), sum(weights)
        ans = r
        while l <= r:
            mid = (l + r) // 2
            """二分查找，如果可以，搜索左边。不行，搜索右边"""
            if cando(weights, mid, D):
                ans = mid
                l, r = l, mid - 1
            else:
                l, r = mid + 1, r
        return ans


