#!/usr/bin/python3

# @Project = step_LeetCode
# @File    : 78_Subsets
# @Author  : TCY
# @Time    : 2019/5/21 10:58
# @Email   : tangcaiyuan@hust.edu.cn
# @Software: PyCharm


class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        '''位运算方法
        1. N = len(nums),构造一个N位的二进制数.并从全零递增到全一，过程中，第i位是否为1就表示当前item是否有nums[i]

        '''
        n = len(nums)
        ans = []
        for i in range(2 ** n):
            tmp = []
            """i为构造的二进制数"""
            for j in range(n):
                if (2 ** j & i) > 0:
                    tmp.append(nums[j])
            ans.append(tmp[:])
        return ans
        '''
        """回溯法
        回溯法和递归是相互有关联的，递归单线，回溯能构成树
        这里又发现一个神奇的坑，result.append(item)和result.append(item[:])并不一样，前者应该是存了地址，item变了就都变了，result最后全为空；后者应该是复制了内容
        """
        def generate(i,nums,item,result):
            """回溯主体"""
            if i >= len(nums): return
            item.append(nums[i])
            result.append(item[:])
            generate(i+1,nums,item,result)
            item.pop()
            generate(i+1,nums,item,result)
        result,item = [],[]
        result.append(item[:])
        generate(0,nums,item,result)
        return result
        '''