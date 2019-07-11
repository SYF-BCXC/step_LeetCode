#!/usr/bin/python3

# @Project = leetCode
# @File    : 3_Longest_Substring_Without_Repeating_Characters
# @Author  : TCY
# @Time    : 2018/9/15 19:02
# @Email   : tangcaiyuan@hust.edu.cn
# @Software: PyCharm
"""
题目描述:
https://leetcode-cn.com/problems/longest-substring-without-repeating-characters/description/
思路:
从左到右扫描即可。如果最新扫描的字符，在已扫字符串中，则将他在字符串中出现的位置之前的都去除，将其加入，最后记录最长长度返回即可。
"""


class Solution:
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        length = len(s)
        if length == 0:
            return 0
        elif length == 1:
            return 1
        else:
            b = 0   # 当前myList的长度
            myList = [s[0]]
            temp = 1    # 用来记录扫描串中最长串的长度
            while b < (length - 1):
                if s[b + 1] not in myList:
                    # 如果不在里面，将该元素加入list，并重新计算最大temp
                    b += 1
                    myList.append(s[b])
                    if len(myList) > temp:
                        temp = len(myList)
                else:
                    # 如果在里面，将该元素在list中位置以前的(包括该位置)都删除，将该元素加入list
                    loc = myList.index(s[b + 1])
                    myList = myList[loc + 1:] + [s[b + 1]]
                    b = b + 1
            return temp


if __name__ == '__main__':
    inString = input("请输入字符串:")
    print(Solution().lengthOfLongestSubstring(inString))

""" 最快参考代码
class Solution:
    def lengthOfLongestSubstring(self, s):
        sub = ''
        sub_len = 0
        max_len = 0
        max_sub = ''
        for letter in s:
            if letter in sub:
                if sub_len > max_len:
                    max_len = sub_len
                    max_sub = sub
                index = sub.index(letter)
                sub = sub[index + 1:] + letter
                sub_len = sub_len - index
            else:
                sub = sub + letter
                sub_len += 1
        if sub_len > max_len:
            max_len = sub_len
        return max_len
"""


''' 第二次遇到，居然第一感觉是用动态规划
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        """
        动态规划
        1、 原问题：长度为n的字符串的最长子串。子问题：长度为i的字符串的最长子串。
        2、 状态： dp[i] 表示以s[i]结尾的最长子串
        3、 初始化： dp[i] = s[i]
        4、 状态转移方程： dp[i] = dp[i-1]+s[i] if s[i] not in dp[i-1] else s[i]
        """
        if not s: return 0
        dp = [s[i] for i in range(len(s))]
        ans = 1
        for i in range(1,len(dp)):
            if s[i] not in dp[i-1]:
                dp[i] = dp[i-1] + s[i]
                ans = max(ans, len(dp[i]))
            else:
                for j in range(i-1, -1, -1):
                    if s[j] not in dp[i]:
                        dp[i] = s[j] + dp[i]
                    else:
                        break
        print(dp)
        return ans
    
'''
