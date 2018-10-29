#!/usr/bin/python3

# @Project = step_LeetCode
# @File    : 024_Swap_Nodes_in_Pairs
# @Author  : TCY
# @Time    : 2018/10/27 22:24
# @Email   : tangcaiyuan@hust.edu.cn
# @Software: PyCharm

"""
题目描述:
https://leetcode-cn.com/problems/swap-nodes-in-pairs/description/
思路:
1、 递归。先考虑仅有两个结点的情况,每次交换两个
"""


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def swapPairs(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head:
            return head
        if not head.next:
            return head
        h = ListNode(-1)
        h.next = head
        tmp = h
        # 后面至少有一个节点
        while tmp.next is not None:
            # 后面至少有两个节点
            if tmp.next.next is not None:
                tmp.next = self.swapTwo(tmp.next)
                tmp = tmp.next.next
            else:
                break
        return h.next


    def swapTwo(self, head):
        """
        交换链表前两个元素返回
        :param head:表头
        :return: 链表
        """
        tmp = head.next
        head.next = head.next.next
        tmp.next = head
        return tmp


if __name__ == '__main__':
    print(Solution().swapPairs())
