#!/usr/bin/python3

# @Project = leetCode
# @File    : 2_add_two_numbers
# @Author  : TCY
# @Time    : 2018/9/15 16:02
# @Email   : tangcaiyuan@hust.edu.cn
# @Software: PyCharm


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def add_two_numbers(self, l1, l2):
        """
        :param l1: ListNode
        :param l2: ListNode
        :return: ListNode
        """
        dummy = ListNode(0)
        current, carry = dummy, 0

        while l1 or l2:
            va1 = carry
            if l1:
                va1 += l1.val
                l1 = l1.next
            if l2:
                va1 += l2.val
                l2 = l2.next
            # divmod(a, b) 返回的是 a/b, a%b
            carry, va1 = divmod(va1, 10)
            current.next = ListNode(va1)
            current = current.next
        if carry == 1:
            current.next = ListNode(1)

        return dummy.next


if __name__ == '__main__':
    a1 = ListNode(3)
    a2 = ListNode(4)
    a3 = ListNode(5)
    a1.next = a2
    a2.next = a3

    b1 = ListNode(3)
    b2 = ListNode(4)
    b3 = ListNode(5)
    b1.next = b2
    b2.next = b3

    c = Solution().add_two_numbers(a1, b1)

    while c:
        print(c.val)
        c = c.next
