#!/usr/bin/python3

# @Project = step_LeetCode
# @File    : 027_Remove_Element
# @Author  : TCY
# @Time    : 2018/10/30 14:46
# @Email   : tangcaiyuan@hust.edu.cn
# @Software: PyCharm

"""
题目描述:
https://leetcode-cn.com/problems/remove-element/description/
思路:

"""


class Solution:
    # 用时53ms
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        l, loc = 0, 0
        for i, k in enumerate(nums):
            if k != val:
                l += 1
                nums[loc] = k
                loc += 1
        return l

    # 最快解答，用时36ms
    def fast_removeElement(self, nums, val):
        while val in nums:
            nums.remove(val)
        return len(nums)

if __name__ == '__main__':
    print(Solution().removeElement())
