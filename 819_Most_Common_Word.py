#!/usr/bin/python3

# @Project = step_LeetCode
# @File    : 819_Most_Common_Word
# @Author  : TCY
# @Time    : 2019/4/29 11:44
# @Email   : tangcaiyuan@hust.edu.cn
# @Software: PyCharm

"""
其实还可以import re，用正则表达式提取所有的单词
1. 用replace替换标点为空格(若直接替换为空,对于 'a,b,c'这种字符会无法直接split)
2. b= re.split(r" +",paragraph)
"""


class Solution:
    def mostCommonWord(self, paragraph: str, banned):
        p = paragraph.lower()
        """当fm为false时，表示未进入单词。
        如果当前为字母，如果fm为False，说明刚进入单词，将fm改为True，并将该字符加入到tmp中；如果fm为True，说明一直在单词里，直接将字母添加到tmp中。
        如果当前非字母，如果fm为Ture，说明离开单词，如果tmp非空，则将tmp加入单词列表，并将fm改为false,tmp置空；如果fm为False，则跳过
        """
        words = []
        fm = False
        tmp = ''
        for i in p:
            if 'a' <= i <= 'z':
                """字母"""
                if fm:
                    tmp += i
                else:
                    fm = True
                    tmp += i
            else:
                """非字母"""
                if fm:
                    if tmp:
                        words.append(tmp)
                        fm = False
                        tmp = ''
        """最后一个字符可能就是字母，但是因为没有非字母激活，该单词不会加入，所以补充一下"""
        if tmp:
            words.append(tmp)
        ans = {}
        for i in words:
            if i not in banned:
                if i in ans:
                    ans[i] += 1
                else:
                    ans[i] = 1
        x = 0
        res = ''
        for k, v in ans.items():
            if v > x:
                x = v
                res = k
        return res
