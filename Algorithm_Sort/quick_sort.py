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



'''
def partition_2(arr, l, r):
    """
    前后指针法。
    1. 特殊情况判断。
    2. pre,cur分别对应小于等于的尾、当前扫描到的大于部分的尾
    3. while cur<len(arr),当前值大于flag,直接cur+=1；否则，pre+=1,swap(cur,pre),cur+=1
    """
    if not arr or l >= r:
        return l
    pre, cur = l - 1, l
    flag, floc = arr[l], l
    while cur <= r:
        if arr[cur] > flag:
            cur += 1
        else:
            pre += 1
            arr[pre], arr[cur] = arr[cur], arr[pre]
            cur += 1
    arr[floc], arr[pre] = arr[pre], arr[floc]
    return pre


def partition(arr, l, r):
    """
    双指针法。1. 特殊条件判断
    2. 记录左端点值。
    3. 若l < r，大循环，找到一组不符合的交换(右边先找，左部分带等于)
    4. 记录r的位置，交换左端点的值
    :param arr:
    :param l:
    :param r:
    :return:
    """
    if l >= r:
        return l
    flag, floc = arr[l], l
    while l < r:
        while l < r and arr[r] > flag:
            r -= 1
        while l < r and arr[l] <= flag:
            l += 1
        arr[l], arr[r] = arr[r], arr[l]
    arr[floc], arr[r] = arr[r], arr[floc]
    return r


def quick_sort_recursion(arr, l, r):
    """
    1. 有效边界判断
    2. 通过partition函数找到标志位的最终位置
    3. 根据位置，递归左右两部分
    :param arr:
    :param l:
    :param r:
    :return:
    """
    if len(arr) <= 0 or l >= r:
        return
    mid = partition(arr, l, r)
    if mid > l:
        quick_sort_recursion(arr, l, mid - 1)
    if mid < r:
        quick_sort_recursion(arr, mid + 1, r)


def quick_sort_nonrecursion(arr, l, r):
    """
    1. 特殊情况判断
    2. 定义递归用的栈，将当前的l和r压入
    3. 栈不为空，则循环。每次循环弹出当前的l和r，执行partition操作，并根据情况压入
    :param arr:
    :param l:
    :param r:
    :return:
    """
    if not arr or l >= r:
        return
    stack = []
    stack.append(l)
    stack.append(r)
    while stack:
        tr = stack.pop()
        tl = stack.pop()
        mid = partition_2(arr, tl, tr)
        if mid > tl:
            stack.append(tl)
            stack.append(mid - 1)
        if mid < tr:
            stack.append(mid + 1)
            stack.append(tr)
'''
