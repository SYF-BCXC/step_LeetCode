#!/usr/bin/python3

# @Project = step_LeetCode
# @File    : 018_4Sum
# @Author  : TCY
# @Time    : 2018/10/12 12:44
# @Email   : tangcaiyuan@hust.edu.cn
# @Software: PyCharm

"""
题目描述:
https://leetcode-cn.com/problems/4sum/description/
思路:
1、同 015_3Sum 的思路，固定两个另外两个指针搜索
2、同 015_3Sum 的思路，Counter所有的值，再进行搜索(但是这里target为任意值，所以此方法并没有提高太多效率)
3、基于2Sum并利用递归解决NSum带target问题
"""
"""
关于python中for循环的补充：
for i in range(0,10):
    i += 1
    print(i)
结果：1    2   3   4   ...    10
结论：i在循环过程中改变不会影响到循环次数

关于python中消除List中重复元素的方法：

def func1(one_list):
    '''
    使用集合，最常用
    '''
    return list(set(one_list))
 
 
def func2(one_list):
    '''
    使用字典的方式
    '''
    return {}.fromkeys(one_list).keys()
 
 
def func3(one_list):
    '''
    使用列表推导的方式
    '''
    temp_list=[]
    for one in one_list:
        if one not in temp_list:
            temp_list.append(one)
    return temp_list
 
 
def func4(one_list):
    '''
    使用排序的方法
    '''
    result_list=[]
    temp_list=sorted(one_list)
    i=0
    while i<len(temp_list):
        if temp_list[i] not in result_list:
            result_list.append(temp_list[i])
        else:
            i+=1
    return result_list
"""
import collections


class Solution:
    # 思路1，但是执行效率很慢
    def fourSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        nums.sort()
        n = len(nums)
        result = []
        for i in range(n - 3):
            for j in range(i + 1, n - 2):
                lnode, rnode = j + 1, n - 1
                while lnode < rnode:
                    tmp = nums[i] + nums[j] + nums[lnode] + nums[rnode]
                    if tmp == target:
                        result.append([nums[i], nums[j], nums[lnode], nums[rnode]])
                        lnode += 1
                        rnode -= 1
                    elif tmp < target:
                        lnode += 1
                    else:
                        rnode -= 1
        # 去除重复元素
        y = []
        for i in result:
            if not i in y:
                y.append(i)
        return y

    # 最快解答，解决NSum带target的问题。思路3
    def fourSum2(self, nums, target):

        def findNsum(nums, target, N, result, results):
            # early termination
            if len(nums) < N or N < 2 or target < nums[0] * N or target > nums[-1] * N:
                return

            # two pointer solve sorted 2-sum problem
            if N == 2:
                l, r = 0, len(nums) - 1
                while l < r:
                    s = nums[l] + nums[r]
                    if s == target:
                        results.append(result + [nums[l], nums[r]])
                        l += 1
                        while l < r and nums[l] == nums[l - 1]:
                            l += 1
                    elif s < target:
                        l += 1
                    else:
                        r -= 1

            # recursively reduce N
            else:
                for i in range(len(nums) - N + 1):
                    if i == 0 or (i > 0 and nums[i - 1] != nums[i]):
                        findNsum(nums[i + 1:], target - nums[i], N - 1, result + [nums[i]], results)

        results = []
        findNsum(sorted(nums), target, 4, [], results)
        return results


if __name__ == '__main__':
    print(Solution().fourSum([-3, -2, -1, 0, 0, 1, 2, 3], 0))
