#!/usr/bin/python3

# @Project = step_LeetCode
# @File    : 10_Regular_Expression_Matching
# @Author  : TCY
# @Time    : 2018/9/25 10:54
# @Email   : tangcaiyuan@hust.edu.cn
# @Software: PyCharm

"""
题目描述:
https://leetcode-cn.com/problems/regular-expression-matching/description/
思路:
1、先扫描字符模式p，记录 字符 和 . ，以及后面出现的是 *  . 还是直接出现多次。
    然后用一个List依次存储(如：[['a',3],['b','*'],['.'，'*'],['.',3]])。同样的，扫描字符串s，
    也用List存储(如：[['a',1],['b',2]],子元素为[出现字符，出现次数])。最后按照匹配规则进行匹配。
"""


class Solution:
    def isMatch(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: bool
        """
        if not s and not p:
            return True
        if not s:
            return False
        if not p:
            return False
        # 先处理字符串s
        list_s = []
        count_s = 1
        list_s.append([s[0], 1])
        for x, z in enumerate(s[1:]):
            # 这里由于切片s[1:]的第0个位置对应原来第1个位置，所以后面的x都要加1
            if z == s[x]:
                count_s += 1
                list_s[-1][-1] = count_s
            else:
                count_s = 1
                list_s.append([z, count_s])
        # 接下来处理模式串p。当前扫描字符为*，将前一个字符的出现次数设置为*；
        # 如果为 . ，则按照字符不同处理，添加一个新的子对；
        # 如果为 相同字符，则和s中处理一样，出现次数+1
        # 如果为 不同字符，则和s中处理一样，添加一个新的子对
        list_p = []
        count_p = 1
        list_p.append([p[0], 1, ' '])
        for x, z in enumerate(p[1:]):
            if z == '*':
                if list_p[-1][-2] == 1:
                    list_p[-1][-2] = 0
                    list_p[-1][-1] = '>='
                else:
                    list_p[-1][-2] -= 1
                    list_p.append([p[x], 0, '>='])
                continue
            if z == p[x]:
                count_p += 1
                list_p[-1][-2] = count_p
            else:
                count_p = 1
                list_p.append([z, count_p, ' '])
        # 为了方便处理[['a', 1], ['a', '*'],['a',1]]这种情况的复杂匹配问题
        # 在后面再append一个符号信息，表示 >= 这种信息
        del_loc = []  # 用于删除元素，python中删除list中元素有很大的坑，会在前面补充
        for x, z in enumerate(list_p[:-1]):
            # 和后面一个是相同的字符子串
            if z[0] == list_p[x + 1][0]:
                # 出现固定次数
                if z[-1] == ' ':
                    list_p[x + 1][1] += z[1]
                    del_loc.append(x)
                else:
                    list_p[x + 1][1] += list_p[x][1]
                    list_p[x + 1][-1] = '>='
                    del_loc.append(x)
        for i in range(len(list_p) - 1, -1, -1):
            if i in del_loc:
                list_p.pop(i)
        # 下面就是匹配处理，将list_s 中每个子对拿出来，进行匹配消除，匹配成功则进入下一个子对
        # 直到所有子对都匹配完成，则返回True；否则返回False
        # 匹配规则，如果是相同元素，则将出现次数相减
        flag = 0  # 用于记录list_s 中现在匹配到的字串的位置
        for i in list_p:
            # 不匹配，就看是否可以出现0次
            if flag == len(list_s):
                break
            if i[0] != list_s[flag][0] and i[0] != '.':
                if list_p[flag][1] == 0 and list_p[flag][-1] == '>=':
                    continue
                else:
                    return False
            else:
                if i[-1] == '>=':
                    if i[1] <= list_s[flag][1]:
                        flag += 1
                        continue
                    else:
                        return False
                else:
                    if i[1] == list_s[flag][1]:
                        flag += 1
                        continue
                    else:
                        return False
        if flag < len(list_s):
            return False
        else:
            return True

if __name__ == '__main__':
    print(Solution().isMatch("ab", ".*"))
