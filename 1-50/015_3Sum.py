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
（构思，暂未实现）2、排序后，用双指针法。指针分别指向a和b，设有abs(a)>abs(b)。
    若abs(a)>2*abs(b)，则a的指针+1
    若abs(a) == 2*abs(b)，则 若b的指针-1等于b，有一组返回值
    若abs(a) < 2*abs(b)，则b的指针靠内搜索
    直到两个指针重合，搜索完成
3、先排序，再从左到右扫描，然后以这个数为根据，在后面的数据中用双指针找到另外两个
4、对nums计数处理，同时将正数与负数分别开来，然后一正一负的情况下，找最后一个数是否在nums中
"""
"""
关于Counter类的补充：
    print(collections.Counter("aaacbb"))  # Counter({'a':6,'b':2,'c':1})
    print(collections.Counter("aaacbb").most_common(2))  # 打印出现次数最多的两个字符的键值对 [('a', 3), ('b', 2)]

关于lambda匿名函数的补充：
    lambda x, y: x + y, y  (输入x,y，返回x+y和y)
    标准格式：lambda parms:returns
    在官方文档中，提到(不建议使用lambda，一是因为作用有限，二是复杂的不便于阅读)：
    my usual course is to avoid using lambda.
    One reason for my preference is that lambda is quite limited in the functions it can define.
    The result has to be computable as a single expression, which means you can’t have multiway 
    if... elif... else comparisons or try... except statements. If you try to do too much in a lambda
    statement, you’ll end up with an overly complicated expression that’s hard to read. 
    
关于filter(function, iterable)的补充：
    Note that filter(function, iterable) is equivalent to the generator expression 
        (item for item in iterable if function(item)) if function is not None 
        and 
        (item for item in iterable if item) if function is None.

关于dict.get(key, default=None)函数的补充：
    从字典中寻找key所对应的value。如果找到了，则返回该value，否则返回传入的第二个参数(未传入参数则默认为None)

关于遍历Counter和dict的补充：
    由于Counter类继承于dict类，共同拥有items()方法。若直接进行 for i in Counter/dict 的遍历，则返回的是key值
若采用 for i,j in Counter.items()/dict.items() 则会获得键与值。
另外,Counter.items()/dict.items()都是一个dict_items的类型。
        *********python环境中执行过程***************
            c = collections.Counter("aaacbb")
            c.items()
        Out[18]: dict_items([('a', 3), ('c', 1), ('b', 2)])
        
            type(c.items())
        Out[19]: dict_items
        
            for i in c:
                print(i)
        Out[20]:a       # 返回键
                c
                b
        
            for i in c.items():
                print(i)
        Out[21]:('a', 3)    # tuple类型
                ('c', 1)
                
            for j in tmp:
                print(j)
        Out[22]:-1          # 返回键
                1
                2
                
            for j in tmp.items():
                print(j)
        Out[23]:(-1, 1)     # 返回tuple类型
                (1, 2)
                (2, 2)
        *********python环境中执行过程***************
"""

import collections


class Solution:
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        nums, result, i = sorted(nums), [], 0
        while i < len(nums) - 2:
            if i == 0 or nums[i] != nums[i - 1]:
                j, k = i + 1, len(nums) - 1
                while j < k:
                    if nums[i] + nums[j] + nums[k] < 0:
                        j += 1
                    elif nums[i] + nums[j] + nums[k] > 0:
                        k -= 1
                    else:
                        result.append([nums[i], nums[j], nums[k]])
                        j, k = j + 1, k - 1
                        while j < k and nums[j] == nums[j - 1]:
                            j += 1
                        while j < k and nums[k] == nums[k + 1]:
                            k -= 1
            i += 1
        return result

    def threeSum2(self, nums):  # 思路4
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        d = collections.Counter(nums)
        nums_2 = [x[0] for x in d.items() if x[1] > 1]
        nums_new = sorted([x[0] for x in d.items()])
        rtn = [[0, 0, 0]] if d[0] >= 3 else []
        for i, j in enumerate(nums_new):
            if j <= 0:
                numss2 = nums_new[i + 1:]
                for x, y in enumerate(numss2):
                    if 0 - j - y in [j, y] and 0 - j - y in nums_2:
                        if sorted([j, y, 0 - j - y]) not in rtn:
                            rtn.append(sorted([j, y, 0 - j - y]))
                    if 0 - j - y not in [j, y] and 0 - j - y in nums_new:
                        if sorted([j, y, 0 - j - y]) not in rtn:
                            rtn.append(sorted([j, y, 0 - j - y]))
        return rtn

        # 思路3
    def threeSum3(self, nums):
        """
        :param nums:List[int]
        :return: List[List[int]]
        """
        nums.sort()
        n, res = len(nums), []
        for i in range(n):
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            l, r = i + 1, n - 1
            while l < r:
                temp = nums[i] + nums[l] + nums[r]
                if temp == 0:
                    res.append([nums[i], nums[l], nums[r]])
                    l, r = l + 1, r - 1
                    # 为了避免[-3,1,1,2,2]的情况下[-3,1,2]会出现两次
                    while l < r and nums[l] == nums[l - 1]:
                        l = l + 1
                    while l < r and nums[r] == nums[r + 1]:
                        r = r - 1
                elif temp > 0:
                    r = r - 1
                else:
                    l = l + 1
        return res

    # 最快解法。思路4
    def threeSum4(self, nums):
        tmp = dict()
        for i in range(len(nums)):
            tmp[nums[i]] = tmp.get(nums[i], 0) + 1  # 完成计数功能，本质上感觉等价于Counter(nums)。
            # 但是此处temp是字典，而Counter返回的是Counter对象(虽然也是继承于dict类)
        left = sorted(filter(lambda x: x < 0, tmp))  # temp中所有小于0的值
        right = sorted(filter(lambda x: x >= 0, tmp))  # temp中所有大于等于0的值
        if 0 in tmp and tmp[0] > 2:  # 如果nums中存在3个以上的0，则将[0,0,0]添加到结果中去
            res = [[0, 0, 0]]
        else:
            res = []
        for i in left:
            for j in right:
                mid = -i - j
                if mid in tmp:
                    if mid in (i, j) and tmp[
                        mid] > 1:  # i+j+i=0 or i+j+j=0.若mid正好就是i和j中的一个，要看看nums数组中，mid出现的次数是否有两次及以上，否则不成立
                        res.append([i, mid, j])
                    elif mid < i or mid > j:  # i,j,mid互不相同
                        res.append([i, mid, j])
        return res


if __name__ == '__main__':
    print(Solution().threeSum())
