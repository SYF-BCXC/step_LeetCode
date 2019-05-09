#!/usr/bin/python3

# @Project = step_LeetCode
# @File    : 206_Reverse_Linked_List
# @Author  : TCY
# @Time    : 2019/5/8 9:52
# @Email   : tangcaiyuan@hust.edu.cn
# @Software: PyCharm


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        """方法一：迭代
        1. 特殊情况判定.空，一个节点，两个节点
        2. pre,cur,aft分别代表前面已逆序部分的头，当前未扫描的链表头，cur的next。
        3. 初始化，pre = None;cur = head; aft = cur.next;
        cur.next = pre;pre = cur; cur = aft; aft = aft.next
        4. 结束条件。cur等于None则不再操作。
        5. 返回pre
        if not head:
            return head
        pre,cur,aft = None, head, head.next
        while aft:
            cur.next = pre
            pre,cur,aft = cur,aft,aft.next
        cur.next = pre
        return cur
        """
        """方法二：递归
        a -> b -> c
        1. 递归出口
        2. 将当前节点后面的节点反转，并返回其头。
        3. 当前节点的next仍然指向当初的节点b(现在反转部分的尾),所以，a.next.next即为b.next,则b.next = a,a.next = None.(c->b->a)
        """
        def recursion(n):
            if n == None or n.next == None:
                return n
            rev = recursion(n.next)
            n.next.next = n
            n.next = None
            return rev

        return recursion(head)
