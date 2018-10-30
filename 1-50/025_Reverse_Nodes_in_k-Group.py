#!/usr/bin/python3

# @Project = step_LeetCode
# @File    : 025_Reverse_Nodes_in_k-Group
# @Author  : TCY
# @Time    : 2018/10/30 1:28
# @Email   : tangcaiyuan@hust.edu.cn
# @Software: PyCharm

"""
题目描述:
https://leetcode-cn.com/problems/reverse-nodes-in-k-group/description/
思路:
1、递归。一次反转K个元素，需要先判定从开始进入到结尾是否有K个元素。反转则是，除了头元素，
    后面每个元素指向前一个元素，头元素则是指向最后一个。
"""


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    # 用时88ms，最快56ms
    def reverseKGroup(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        if k == 1:
            return head
        if head is None:
            return head
        h = ListNode(0)
        h.next = head
        n, tmp, tst = 0, h, h
        while True:
            while n != k:
                if tst.next is not None:
                    n += 1
                    tst = tst.next
                else:
                    return h.next
            n = 0
            # 探测到前面有K个元素
            # 进行交换
            tmp.next, tmp = self.swapK(tmp.next, k)
            tst = tmp
            # 交换完成一次，继续

    def swapK(self, head, k):
        prior, stand, nxt = head, head.next, head.next.next
        # K=3,1->2->3->4,需要循环两次，最后3->4时，4为None，无next，避免循环越界
        for i in range(k - 2):
            stand.next = prior
            prior = stand
            stand = nxt
            nxt = nxt.next
        stand.next = prior
        head.next = nxt
        return stand, head

    # 最快解答，56ms,思路一样，但是写法精炼
    def fast_reverseKGroup(self, head, k):
        dummy = jump = ListNode(0)
        dummy.next = l = r = head

        while True:
            count = 0
            while r and count < k:  # use r to locate the range
                r = r.next
                count += 1
            if count == k:  # if size k satisfied, reverse the inner linked list
                pre, cur = r, l
                for _ in range(k):
                    cur.next, cur, pre = pre, cur.next, cur  # standard reversing
                jump.next, jump, l = pre, l, r  # connect two k-groups
            else:
                return dummy.next


if __name__ == '__main__':
    def list2ListNode(lst):
        head = ListNode(0)
        tmp = head
        for i, k in enumerate(lst):
            tmp.next = ListNode(k)
            tmp = tmp.next
        return head.next


    def printListNode(lst):
        tmp = lst
        while True:
            if tmp is not None:
                print(tmp.val)
                tmp = tmp.next
            else:
                return


    test = [1, 2, 3, 4, 5]
    k = 3
    printListNode(Solution().reverseKGroup(list2ListNode(test), k))
