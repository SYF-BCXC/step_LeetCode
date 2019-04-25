#!/usr/bin/python3

# @Project = step_LeetCode
# @File    : quick_sort
# @Author  : TCY
# @Time    : 2019/4/13 17:05
# @Email   : tangcaiyuan@hust.edu.cn
# @Software: PyCharm


def swap(lst, a, b):
    tmp = lst[a]
    lst[a] = lst[b]
    lst[b] = tmp


def partition_pre_after(lst, start, end):
    """前后指针法"""
    if start >= end:
        return start
    pivot = lst[start]
    pivot_pos = start
    pre = start     # 指向小的后
    after = start   # 指向当前
    while after <= end:
        if after <= end and lst[after] >= pivot:
            after += 1
        if after <= end and lst[after] < pivot:
            pre += 1
            swap(lst, after, pre)
            after += 1
    swap(lst, pivot_pos, pre)
    return pre


def partition_dig(lst, start, end):
    """挖坑法。"""
    if start >= end:
        return start
    pivot = lst[start]
    while start < end:
        while start < end and lst[end] >= pivot:
            end -= 1
        lst[start] = lst[end]
        while start < end and lst[start] <= pivot:
            start += 1
        lst[end] = lst[start]
    lst[start] = pivot
    return start


def partition_double_point(lst, start, end):
    """
    双指针法。以lst[start]为基准，完成一次分割，并返回其最终位置
    :param lst: 待划分数组
    :param start: 本次划分范围的开始
    :param end: 本次划分范围的结束
    :return: 基准的位置
    """
    if start >= end:
        return start
    pivot = lst[start]
    pivot_pos = start
    while start < end:
        while lst[end] >= pivot and end > start:
            end -= 1
        while lst[start] <= pivot and start < end:
            start += 1
        swap(lst, start, end)
    swap(lst, pivot_pos, start)
    return end


def quick_sort_recursion(lst, left, right):
    """
    将lst进行快速排序
    :param lst: 待排序数组
    :param left: 数组范围左侧
    :param right: 数组范围右侧
    :return: None
    """
    if right <= left:
        return
    idx = partition_double_point(lst, left, right)
    quick_sort_recursion(lst, left, idx - 1)
    quick_sort_recursion(lst, idx + 1, right)


def quick_sort_nonrecursion(lst, left, right):
    if left >= right:
        return
    zhan = [left, right]
    while zhan:
        tmp_right = zhan.pop()
        tmp_left = zhan.pop()
        idx = partition_pre_after(lst, tmp_left, tmp_right)
        if idx > tmp_left:
            zhan.append(tmp_left)
            zhan.append(idx - 1)
        if idx < tmp_right:
            zhan.append(idx + 1)
            zhan.append(tmp_right)


if __name__ == '__main__':
    test = [1, 4, 2, 3.6, -1, 0, 25, -34, 8, 9, 1, 0]
    print("original:", test)
    quick_sort_nonrecursion(test, 0, len(test) - 1)
    print("Sorted:", test)
