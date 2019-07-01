# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

"""
改进方案：
1. 直接用栈
2. 同样是这个方法，但是可以考虑用0补齐两个链表
"""


class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        def reverseList(ln):
            if not ln:
                return ln
            pre = ListNode(0)
            cur = ln
            while cur:
                tmp = cur.next 
                cur.next = pre.next
                pre.next = cur
                cur = tmp
            return pre.next
        
        l1 = reverseList(l1)
        l2 = reverseList(l2)
        carry = 0
        ans = ListNode(0)
        cur = ans
        while l1 and l2:
            tmp = l1.val + l2.val + carry
            carry = tmp // 10
            tmp = tmp % 10
            cur.next = ListNode(tmp)
            cur = cur.next
            l1 = l1.next
            l2 = l2.next
        while l1:
            tmp = l1.val + carry
            carry = tmp // 10
            tmp = tmp % 10
            cur.next = ListNode(tmp)
            cur = cur.next
            l1 = l1.next
        while l2:
            tmp = l2.val + carry
            carry = tmp // 10
            tmp = tmp % 10
            cur.next = ListNode(tmp)
            cur = cur.next
            l2 = l2.next
        if carry == 1:
            cur.next = ListNode(1)
        return reverseList(ans.next)