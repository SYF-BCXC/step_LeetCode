#!/usr/bin/python3

# @Project = step_LeetCode
# @File    : 026_Remove_Duplicates_from_Sorted_Array
# @Author  : TCY
# @Time    : 2018/10/30 10:52
# @Email   : tangcaiyuan@hust.edu.cn
# @Software: PyCharm

"""
题目描述:
https://leetcode-cn.com/problems/remove-duplicates-from-sorted-array/description/
思路:
1、简单，直接看代码

关于"if not x"," if x is not None" 和 "if not x is None"的区别：
    if not x:{
    以下都会被判为False
    not None == not False == not '' == not 0 == not [] == not {} == not ()
    }
    if x is not None:{
    如条件所示，如果不为None则进入
    }
    if not x is None:{
    同上，但是该写法不推荐，容易被理解为if (not x) is None
    }

关于x is None 和 x == None 的补充：
    is 比较的是数据的 id
    == 比较的是数据的 值
"""


class Solution:
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int 数组新长度
        """
        l, loc = 1, 0
        if not nums:
            return 0
        for i, k in enumerate(nums):
            if k != nums[loc]:
                # 出现了不同的元素
                l += 1
                loc += 1
                nums[loc] = k
        return l


if __name__ == '__main__':
    print(Solution().removeDuplicates())
