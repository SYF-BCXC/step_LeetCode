#!/usr/bin/python3

# @Project = step_LeetCode
# @File    : 028_Implement_strStr()
# @Author  : TCY
# @Time    : 2018/10/30 15:00
# @Email   : tangcaiyuan@hust.edu.cn
# @Software: PyCharm

"""
题目描述:
https://leetcode-cn.com/problems/implement-strstr/description/
思路:
1、 单纯用python的优势。。。
2、 KMP算法

关于KMP算法的补充：
    核心思路：利用已经匹配上的信息和模式串自身的信息，减少匹配次数。
    https://www.cnblogs.com/yjiyjige/p/3263858.html
    难点Next数组构造:http://www.cnblogs.com/tangzhengyue/p/4315393.html
"""


class Solution:
    # 思路1。。。in 和 find 函数，用时48ms
    def strStr(self, haystack, needle):
        return haystack.index(needle) if needle in haystack else -1

    # 思路1。。。 切片 ，用时52ms
    def strStr2(self, haystack, needle):
        a, b = len(haystack), len(needle)
        for i in range(a - b + 1):
            if haystack[i:i + b] == needle:
                return i
        return -1

    # 思路2，KMP算法,用时80ms
    def strStr3(self, haystack, needle):
        def getNextArray(str):
            """
            获得子串的next数组
            :param str: 字串
            :return: next数组
            """
            j, k, tmp = 0, -1, len(str)
            nextArray = [-1 for i in range(tmp)]  # 或者 [-1] * tmp
            while j < tmp - 1:
                if k == -1 or str[k] == str[j]:
                    j, k = j + 1, k + 1
                    nextArray[j] = k
                else:
                    k = nextArray[k]
            return nextArray

        if not needle:
            return 0
        myNext = getNextArray(needle)
        n, m, i, j = len(haystack), len(needle), 0, 0
        while i < n and j < m:
            if haystack[i] == needle[j]:
                i, j = i + 1, j + 1
            else:
                if myNext[j] == -1:
                    i, j = i + 1, 0
                else:
                    j = myNext[j]
        if i != n:
            return i - j
        else:
            if j == m:
                return i - j
            else:
                return -1


if __name__ == '__main__':
    print(Solution().strStr3("mississippi", "issipi"))
