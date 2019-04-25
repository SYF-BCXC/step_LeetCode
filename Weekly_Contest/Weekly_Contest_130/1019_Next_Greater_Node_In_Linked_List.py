#!/usr/bin/python3

# @Project = step_LeetCode
# @File    : 1019_Next_Greater_Node_In_Linked_List
# @Author  : TCY
# @Time    : 2019/4/25 15:38
# @Email   : tangcaiyuan@hust.edu.cn
# @Software: PyCharm

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None


class Solution(object):
    def nextLargerNodes(self, head):
        """
        :type head: ListNode
        :rtype: List[int]
        """
        """维护逆序栈"""
        shu = []
        # 链表不方便维护先变list
        while head:
            shu.append(head.val)
            head = head.next
        # 逆序栈对应元素的位置
        sta = []
        res = [0 for _ in range(len(shu))]
        # 新值入栈，若小于栈顶，则结果指针跳过；若大于栈顶，则将该值对应的结果置为当前值。
        for i in range(len(shu)):
            while (len(sta)>0) and (shu[i] > shu[sta[-1]]):
                res[sta[-1]] = shu[i]
                sta.pop()
            sta.append(i)
        return res