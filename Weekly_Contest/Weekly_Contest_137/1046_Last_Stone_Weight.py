#!/usr/bin/python3

# @Project = step_LeetCode
# @File    : 1046_Last_Stone_Weight
# @Author  : TCY
# @Time    : 2019/5/27 16:45
# @Email   : tangcaiyuan@hust.edu.cn
# @Software: PyCharm


class Solution:
    def binarySearch(self, nums, num):
        n = len(nums)
        l, r = 0, n - 1
        while l <= r:
            mid = l + (r - l) // 2
            if nums[mid] < num:
                l = mid + 1
            else:
                r = mid - 1
        return r + 1

    def lastStoneWeight(self, stones: List[int]) -> int:
        align = sorted(stones)

        tmp = len(align)
        while tmp > 1:
            x, y = align[-2], align[-1]
            align.pop()
            align.pop()
            if x != y:
                loc = self.binarySearch(align, y - x)
                align.insert(loc, y - x)
            tmp = len(align)
        if tmp == 1:
            return align[0]
        else:
            return 0
