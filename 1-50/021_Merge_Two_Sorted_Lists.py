#!/usr/bin/python3

# @Project = step_LeetCode
# @File    : 021_Merge_Two_Sorted_Lists
# @Author  : TCY
# @Time    : 2018/10/24 21:29
# @Email   : tangcaiyuan@hust.edu.cn
# @Software: PyCharm

"""
题目描述:
https://leetcode-cn.com/problems/merge-two-sorted-lists/description/
思路:
比较当前l1 与 l2 大小 最后拼接剩余部分
"""


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        myL = ListNode(0)
        flag = myL
        while l1 and l2:
            if l1.val < l2.val:
                tmp = ListNode(l1.val)
                flag.next = tmp
                l1 = l1.next
                flag = flag.next
            else:
                tmp = ListNode(l2.val)
                flag.next = tmp
                l2 = l2.next
                flag = flag.next
        if l1:
            flag.next = l1
        if l2:
            flag.next = l2
        return myL.next

    # 思路一样，写法简洁更快
    def mergeTwoLists2(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        思路：
            注意返回的也是一个有序列表
            比较当前l1 与 l2 大小 最后拼接剩余部分
        """
        head = temp = ListNode(0)
        while l1 and l2:
            if l1.val <= l2.val:
                temp.next = l1
                l1 = l1.next
            else:
                temp.next = l2
                l2 = l2.next
            temp = temp.next
        temp.next = l1 or l2
        return head.next



if __name__ == '__main__':
    print(Solution().mergeTwoLists())
