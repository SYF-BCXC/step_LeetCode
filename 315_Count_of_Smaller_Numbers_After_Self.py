#!/usr/bin/python3

# @Project = step_LeetCode
# @File    : 315_Count_of_Smaller_Numbers_After_Self
# @Author  : TCY
# @Time    : 2019/5/23 19:38
# @Email   : tangcaiyuan@hust.edu.cn
# @Software: PyCharm


class Solution:
    def f(self, num, nums):
        """找num在nums中应该插入的位置(第一个大于他的元素下标)"""
        l, r = 0, len(nums) - 1
        while l <= r:
            mid = l + (r - l) // 2
            if nums[mid] < num:
                l = mid + 1
            if nums[mid] >= num:
                r = mid - 1
        return r + 1

    def countSmaller(self, nums):
        """利用栈，从右往左扫描，cur值在栈的第i位，则其右边有多少小于的值"""
        if not nums:
            return []
        stack = []
        ans = [0 for _ in range(len(nums))]
        for i in range(len(nums) - 1, -1, -1):
            j = self.f(nums[i], stack)
            """超时.将这一部分改成二分查找？
            while j < len(stack):
                if stack[j] >= nums[i]:
                    break
                j += 1
            """
            stack.insert(j, nums[i])
            ans[i] = j
        return ans
