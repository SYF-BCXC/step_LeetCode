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
2、 递归。

关于循环删除List表中元素的补充：
    删除的方法：
    1、remove: 删除单个元素，删除首个符合条件的元素，按值删除。L.remove("2")，则是删除L中第一个值为"2"的元素
    2、pop:删除并 返回 指定位置 元素(根据索引)。L.pop(2)，删除索引为2的元素
    3、del:根据索引删除。del L[0:3]，删除前三个元素

    for x, z in L:(L是一个List)
    z依次遍历List中的元素，x也依次增加(哪怕你删除了一个元素，总长度减少了，x也依旧每次循环+1)
    因此，删除后L的长度会变小，但是X会一直增加，可能会越界，也可能发生别的错误。

    解决方法：
    1、倒序删除。
    ########### 代码 ###########
    num_list = [1, 2, 3, 4, 5]
    for i in range(len(num_list)-1, -1, -1):
        if num_list[i] == 2:
            num_list.pop(i)
        else:
            print(num_list[i])

    2、考虑用while循环

    参考文献：https://www.cnblogs.com/bananaplan/p/remove-listitem-while-iterating.html
"""


class Solution:
    # 方法太过直接，操作起来太复杂，同时对于最后两个List进行比较也不方便，当面对"ab"和".*"时，匹配过于麻烦
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
        # list_s = [['a', 4], ['d', 2], ['b', 2], ['d', 1], ['c', 2]]
        # list_p = [['a', 0, '>='], ['d', 0, '>='], ['b', 0, '>='], ['d', 1, ' '], ['c', 0, '>=']]
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

    # 方法二：用递归，此方法速度较慢，速度前90%
    def isMatch2(self, s, p):
        # p 为空的时候，s 如果为空则返回True，不为空则返回False
        if not p:
            return not s
        # p中只有一个字符，或者当前这个字符没有伸展能力
        if len(p) == 1 or p[1] != '*':
            if len(s) > 0 and (p[0] == s[0] or p[0] == '.'):
                return self.isMatch2(s[1:], p[1:])
            else:
                return False
        else:
            # len(p)!= 1 and p[1] == '*'
            # 当前这个字符具有伸展性
            # s 并未匹配完成，并且当前这个字符能匹配上
            while len(s) > 0 and (p[0] == s[0] or p[0] == '.'):
                # 处理 "c*" 这种，但是 c 并未在 s 中出现
                if self.isMatch2(s, p[2:]):
                    return True
                s = s[1:]
            return self.isMatch2(s, p[2:])

    # 方法三：动态规划，此方法速度较快，用时76ms，速度前5%
    def isMatch3(self, s, p):
        if not s and not p:
            return True
        if not p:
            return False
        m, n = len(s), len(p)
        d = [[False for i in range(n + 1)] for j in range(m + 1)]
        # d[i][j]表示s[:i]与p[:j]是否匹配
        d[0][0] = True
        for k in range(2, n + 1, 2):
            if p[k - 1] == '*':
                d[0][k] = True
            else:
                break
        if m == 0:
            return d[m][n]
        if s[0] == p[0] or p[0] == '.':
            d[1][1] = True
        if n == 1:
            return d[m][n]
        for i in range(1, m + 1):
            for j in range(2, n + 1):
                x, y, z = s[i - 1], p[j - 1], p[j - 2]
                if x == y or y == '.':
                    d[i][j] = d[i - 1][j - 1]
                else:
                    if y != '*':
                        d[i][j] = False
                    else:
                        if x == z or z == '.':
                            if d[i][j - 2]:
                                d[i][j] = True
                            else:
                                d[i][j] = d[i - 1][j]
                        else:
                            d[i][j] = d[i][j - 2]
        return d[m][n]

    # 同为方法三，但是他的答案更精简，值得研究
    def isMatch3_2(self, s, p):
        dp = [[False for i in range(len(p) + 1)] for j in range(len(s) + 1)]
        dp[0][0] = True
        for i in range(1, len(p) + 1):
            if p[i - 1] == '*':
                if i >= 2:
                    dp[0][i] = dp[0][i - 2]
        for i in range(1, len(s) + 1):
            for j in range(1, len(p) + 1):
                if p[j - 1] == '.':
                    dp[i][j] = dp[i - 1][j - 1]
                elif p[j - 1] == '*':
                    dp[i][j] = dp[i][j - 1] or dp[i][j - 2] or (
                            dp[i - 1][j] and (s[i - 1] == p[j - 2] or p[j - 2] == '.'))
                else:
                    dp[i][j] = dp[i - 1][j - 1] and s[i - 1] == p[j - 1]
        return dp[len(s)][len(p)]

    # 最快解法
    def isMatch4(self, s, p):
        memo = {}

        def dp(i, j):
            if (i, j) not in memo:
                if j == len(p):
                    ans = i == len(s)
                else:
                    first_match = i < len(s) and p[j] in {s[i], '.'}
                    if j + 1 < len(p) and p[j + 1] == '*':
                        ans = dp(i, j + 2) or first_match and dp(i + 1, j)
                    else:
                        ans = first_match and dp(i + 1, j + 1)

                memo[i, j] = ans
            return memo[i, j]

        return dp(0, 0)


if __name__ == '__main__':
    print(Solution().isMatch3("", ".*"))
