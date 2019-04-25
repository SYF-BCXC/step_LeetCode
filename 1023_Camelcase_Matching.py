#!/usr/bin/python3

# @Project = step_LeetCode
# @File    : 1023_Camelcase_Matching
# @Author  : TCY
# @Time    : 2019/4/24 15:22
# @Email   : tangcaiyuan@hust.edu.cn
# @Software: PyCharm

def camelMatch(queries, pattern):
    """
    :type queries: List[str]
    :type pattern: str
    :rtype: List[bool]
    """
    """只能查入小写字母。用双指针，一个指向模式串，一个指向匹配串，如果匹配串中为大写且不与当前位置匹配，则返回False"""

    def isDa(s):
        if ord(s) <= ord('Z') and ord(s) >= ord('A'):
            return True
        else:
            return False

    def isMatch(quer, pat):
        point_q, point_p = 0, 0
        len_q, len_p = len(quer), len(pat)
        while point_q < len_q and point_p < len_p:
            if quer[point_q] == pat[point_p]:
                point_q += 1
                point_p += 1
            else:
                if isDa(quer[point_q]):
                    return False
                else:
                    point_q += 1
        if point_p != len_p:
            return False
        else:
            if point_q < len_q:
                """注意一下剩下的是否有多余的大写"""
                for i in range(point_q, len_q):
                    if isDa(quer[i]):
                        return False
                return True
            else:
                return True

    result = []
    for i in queries:
        result.append(isMatch(i, pattern))
    return result


queries = ["IXfGawluvnCa", "IsXfGaxwulCa", "IXfGawlqtCva", "IXjfGawlmeCa", "IXfGnaynwlCa", "IXfGcamwelCa"]
pattern = "IXfGawlCa"
result = camelMatch(queries, pattern)
print(result)