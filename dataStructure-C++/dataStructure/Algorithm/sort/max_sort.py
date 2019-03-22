# -*- coding: utf-8 -*-
"""
Created on Fri Mar 22 16:23:13 2019

@author: lenovo
"""
import copy


def a_greater_than_b(a, b):
    str_a = str(a)
    str_b = str(b)
    l = len(str_a) + len(str_b)
    if len(str_a) < l:
        d, m = divmod(l, len(str_a))
        str_a = str_a * d + str_a[:m]
    if len(str_b) < l:
        d, m = divmod(l, len(str_b))
        str_b = str_b * d + str_b[:m]
    for i in range(l):
        if str_a[i] > str_b[i]:
            return True
        if str_a[i] < str_b[i]:
            return False
    return True


def mergeSort(nums, left, right):
    # 0. 边界判断
    if left >= right:
        return
    # 1. 计算中间位置,并将两块分别排序
    mid = left + (right - left) // 2
    mergeSort(nums, left, mid)
    mergeSort(nums, mid + 1, right)
    # 2. 合并
    l = left
    if (mid + 1) >= right:
        r = right
    else:
        r = mid + 1
    mylist = copy.deepcopy(nums)
    while l <= mid and r <= right:
        if a_greater_than_b(mylist[l], mylist[r]):
            nums[left] = mylist[r]
            r += 1
        else:
            nums[left] = mylist[l]
            l += 1
        left += 1
    if l > mid:
        nums[left:(right + 1)] = mylist[r:(right + 1)]
    if r > right:
        nums[left:(right + 1)] = mylist[l:(mid + 1)]


def max_sort(nums):
    mergeSort(nums, 0, len(nums) - 1)
    nums.reverse()
    s = ""
    for i in range(len(nums)):
        s += str(nums[i])
    return s


alist = [12, 121]
print(max_sort(alist))
