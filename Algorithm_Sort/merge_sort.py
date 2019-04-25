#!/usr/bin/python3

# @Project = step_LeetCode
# @File    : merge_sort
# @Author  : TCY
# @Time    : 2019/4/13 16:53
# @Email   : tangcaiyuan@hust.edu.cn
# @Software: PyCharm
"""
补充：
a = [1,2]
b = [3]
b.append(a) # [3,[1,2]]
b.extend(a) # [3,1,2]
b += a      # [3,1,2]
"""


def merge(left, right):
    """
    用于合并两个有序数组
    :param left: 有序数组1
    :param right: 有序数组2
    :return: 合并后的有序数组
    """
    res = []
    while left and right:
        if left[0] < right[0]:
            res.append(left.pop(0))
        else:
            res.append(right.pop(0))
    if left:
        res.extend(left)
    if right:
        res.extend(right)
    return res


def merge_sort(l):
    """
    将数组L排序
    :param L: 待排序数组
    :return: 返回有序数组
    """
    if len(l) <= 1:
        return l
    mid = len(l) // 2
    left = l[:mid]
    right = l[mid:]
    left = merge_sort(left)
    right = merge_sort(right)
    return merge(left, right)


if __name__ == '__main__':
    test = [1, 4, 2, 3.6, -1, 0, 25, -34, 8, 9, 1, 0]
    print("original:", test)
    print("Sorted:", merge_sort(test))
