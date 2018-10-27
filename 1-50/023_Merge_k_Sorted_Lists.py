#!/usr/bin/python3

# @Project = step_LeetCode
# @File    : 023_Merge_k_Sorted_Lists
# @Author  : TCY
# @Time    : 2018/10/26 10:35
# @Email   : tangcaiyuan@hust.edu.cn
# @Software: PyCharm

"""
题目描述:
https://leetcode-cn.com/problems/merge-k-sorted-lists/description/
思路:
1、参照两个有序链表的合并，可以将链表数组中的每个链表两两合并。效率很慢
2、用堆实现。

enumerate() 函数用于将一个可遍历的数据对象(如列表、元组或字符串)组合为一个索引序列，同时列出数据和数据下标，一般用在 for 循环当中。
    seq = ['one', 'two', 'three']
    for i, element in enumerate(seq):
        print i, element

    0 one
    1 two
    2 three

关于heapq堆的补充：
    heapify(x)  #以线性时间将一个列表转为堆
    heappush(heap,item)#往堆中插入一条新的值
    item = heappop(heap)#弹出最小的值
    item = heap[0]#查看堆中最小的值，不弹出
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

    # 思路一样，但是需要k-1次合并，慢的那种
    def mergeKLists2(self, lists):
        if not lists:
            return lists
        while len(lists) > 1:
            l1 = lists.pop()
            l2 = lists.pop()
            r = self.mergeTwoLists(l1, l2)
            lists.append(r)
        return lists[0]

    def mergeKLists(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """
        if not lists:
            return lists
        lists2 = []
        while len(lists) + len(lists2) > 1:
            # 为了减少链表合并的次数，每次将一边的链表两两合并完成放如另外一边
            # 如果单纯的每次用最后两个链表合并，再将结果放入最后，一共需要合并k-1次。
            # 这样两边倒，类似于2分法，只需要log(k)次。真实提交对比结果，时间复杂度从6512ms，降低到了164ms。
            if len(lists2) == 0:
                while len(lists) > 1:
                    l1 = lists.pop()
                    l2 = lists.pop()
                    r = self.mergeTwoLists(l1, l2)
                    lists2.append(r)
                if len(lists) == 1:
                    lists2.append(lists.pop())
            else:
                while len(lists2) > 1:
                    l1 = lists2.pop()
                    l2 = lists2.pop()
                    r = self.mergeTwoLists(l1, l2)
                    lists.append(r)
                if len(lists2) == 1:
                    lists.append(lists2.pop())
        if len(lists) == 1:
            return lists[0]
        if len(lists2) == 1:
            return lists2[0]


""" 最快解答

from heapq import heappush, heappop, heapify

class Solution:
    def mergeKLists(self, lists):
        h = [(node.val, index, node) for index, node in enumerate(lists) if node]
        heapify(h)
        sorted_head = ListNode(-1)
        cur = sorted_head
        while h:
            (cur_min, index, node) = heappop(h)
            next_node = node.next
            if next_node:
                heappush(h, (next_node.val,index, next_node))
            node.next = None
            cur.next = node
            cur = cur.next
        return sorted_head.next
"""

if __name__ == '__main__':
    print(Solution().mergeKLists())
