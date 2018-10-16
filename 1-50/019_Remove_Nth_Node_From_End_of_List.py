#!/usr/bin/python3

# @Project = LeetCode
# @File    : 019_Remove_Nth_Node_From_End_of_List
# @Author  : TCY
# @Time    : 2018/10/16 20:31
# @Email   : tangcaiyuan@hust.edu.cn
# @Software: PyCharm

"""
题目描述:
https://leetcode-cn.com/problems/remove-nth-node-from-end-of-list/description/
思路:
1、 双指针法。两个指针始终保持隔N，当最后一个指针到链表的结尾，则表明前一个指针是倒数第N个。
    难点：删除第一个元素会很难处理。先后移n-1个元素，如果rnode.next==None，说明这时要删除第一个元素。最后补上rnode=rnode.next即可
"""


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    # 思路1
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        lnode, rnode = head, head
        for i in range(n - 1):
            rnode = rnode.next
        if rnode.next == None:
            head = head.next
            return head
        rnode = rnode.next
        while rnode.next != None:
            lnode = lnode.next
            rnode = rnode.next
        tmp = lnode.next.next
        lnode.next = tmp
        return head


if __name__ == '__main__':
    print(Solution().removeNthFromEnd())
