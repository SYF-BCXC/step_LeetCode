#!/usr/bin/python3

# @Project = step_LeetCode
# @File    : Segment_Tree
# @Author  : TCY
# @Time    : 2019/7/15 17:25
# @Email   : tangcaiyuan@hust.edu.cn
# @Software: PyCharm

"""
自构线段树，完成update和query操作
https://www.bilibili.com/video/av47331849?from=search&seid=7648575135614905166
"""

class MySegmentTree:
    def __init__(self, arr):
        self.original_arr = arr
        self.original_len = len(arr)
        self.mx_len = 100
        self.build_arr = [0 for _ in range(self.mx_len)]
        self.buildTree(0, 0, len(arr) - 1)

    def buildTree(self, node, start, end):
        """构造线段树
        build_arr中每个值都代表了一个段落的和
        """
        if start == end:
            self.build_arr[node] = self.original_arr[start]
            return

        left_node = 2 * node + 1
        right_node = 2 * node + 2

        mid = start + (end - start) // 2
        self.buildTree(left_node, start, mid)
        self.buildTree(right_node, mid + 1, end)

        self.build_arr[node] = self.build_arr[left_node] + self.build_arr[right_node]

    def query(self, node, start, end, left, right):
        """To get sum of the scope [left, right] in original arr"""
        if start > right or end < left:
            return 0
        elif start == end:
            return self.original_arr[start]
        elif start >= left and end <= right:
            return self.build_arr[node]

        mid = start + (end - start) // 2
        left_node = 2 * node + 1
        right_node = 2 * node + 2

        left_sum = self.query(left_node, start, mid, left, right)
        right_sum = self.query(right_node, mid + 1, end, left, right)

        return left_sum + right_sum

    def update(self, node, start, end, idx, val):
        """Update original_arr[idx] = val and update build_arr"""
        if start == end == idx:
            self.original_arr[idx] = val
            self.build_arr[node] = val
            return
        mid = start + (end - start) // 2
        left_node = 2 * node + 1
        right_node = 2 * node + 2

        if start <= idx <= mid:
            self.update(left_node, start, mid, idx, val)
        elif mid + 1 <= idx <= end:
            self.update(right_node, mid + 1, end, idx, val)
        else:
            raise Exception("idx not in range [start, end]")

        self.build_arr[node] = self.build_arr[left_node] + self.build_arr[right_node]

    def printTree(self):
        print("The original arr:", end=' ')
        print(self.original_arr)
        print("The segment tree arr:", end=' ')
        print(self.build_arr)


if __name__ == '__main__':
    original_arr = [1, 3, 5, 7, 9, 11]
    mt = MySegmentTree(original_arr)
    mt.printTree()
    mt.update(0, 0, len(original_arr) - 1, 4, 6)
    mt.printTree()
    print(mt.query(0, 0, 5, 2, 5))
