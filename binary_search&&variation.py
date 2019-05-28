#!/usr/bin/python3

# @Project = step_LeetCode
# @File    : binary_search&&variation
# @Author  : TCY
# @Time    : 2019/5/24 20:35
# @Email   : tangcaiyuan@hust.edu.cn
# @Software: PyCharm


def binarySearch(nums, target):
    """普通的二分查找
    找到返回位置，没找到返回-1
    """
    l, r = 0, len(nums) - 1
    while l <= r:
        mid = l + (r - l) // 2
        if nums[mid] == target:
            return mid
        elif nums[mid] < target:
            l = mid + 1
        else:
            r = mid - 1
    return -1


def binarySearchFB(nums, target):
    """找第一个大于等于target的值，如果所有值都小于target返回len(nums)"""
    l, r = 0, len(nums) - 1
    while l <= r:
        mid = l + (r - l) // 2
        if nums[mid] < target:
            l = mid + 1
        else:
            r = mid - 1
    return r + 1


def binarySearchLS(nums, target):
    l, r = 0, len(nums) - 1
    while l <= r:
        mid = l + (r - l) // 2
        if nums[mid] <= target:
            l = mid + 1
        else:
            r = mid - 1
    return l - 1


while True:
    target = int(input())
    nums = [1, 2, 4, 5, 5, 5, 7, 10]
    print(binarySearchLS(nums, target))
