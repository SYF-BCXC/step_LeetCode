#!/usr/bin/python3

# @Project = leetCode
# @File    : 2_add_two_numbers
# @Author  : TCY
# @Time    : 2018/9/15 16:02
# @Email   : tangcaiyuan@hust.edu.cn
# @Software: PyCharm

"""
题目描述:
https://leetcode-cn.com/problems/add-two-numbers/description/
思路:
思路较为简单，相加即可。

以下两个观念非常重要，完全不同于常规的C语言和JAVA等，本人当时也很奇怪：
关于“python基于值的管理”的补充：
    大致意思，C语言中变量是内存中的值，如a=3，那么会为a开辟一个空间，内容就是3；而python中则是，先开辟一个空间，内容为3，然后让该变量指向这个值。
    因此，当变量改变时，C语言中变量改变的是内存空间中的值，不是地址；而python中，变量变的是地址，不变的是原来那个内存中的值。

    参考文献：https://blog.csdn.net/WSBruce/article/details/79234389

关于赋值，浅拷贝与深拷贝的补充(参考文献中有例子，可以帮助理解)：
    赋值：是对对象的引用。当创建一个对象，然后将其赋值给一个变量的时候，python并没有拷贝这个对象的值，而是拷贝了对该对象的引用。所以，原始对象一旦改变，赋值对象同样会改变
    浅复制：不会拷贝子对象(例如alist[1,2,[3,4]]，其中alist[2]，即[3,4]就是一个子对象)。所以拷贝的部分不会跟着改变，但是子对象由于只是拷贝引用，所以会跟着变。
    深复制：拷贝子对象，用更多内存，完全不会跟着变

    参考文献：https://www.cnblogs.com/xueli/p/4952063.html
"""


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
        current, carry = dummy, 0   # 此处current = dummy 就是赋值操作，他们指的都是同一块内存

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
