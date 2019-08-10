#!/usr/bin/python3

# @Project = step_LeetCode
# @File    : 1146_Snapshot_Array
# @Author  : TCY
# @Time    : 2019/8/9 22:56
# @Email   : tangcaiyuan@hust.edu.cn
# @Software: PyCharm

import bisect


class SnapshotArray:

    def __init__(self, length: int):
        self.A = [[[-1, 0]] for _ in range(length)]
        self.snap_id = 0
        self.length = length

    def set(self, index: int, val: int) -> None:
        i = bisect.bisect(self.A[index], [self.snap_id])    # The returned insertion point i partitions the array a into two halves so that all(val <= x for val in a[lo:i]) for the left side and all(val > x for val in a[i:hi]) for the right side. 因此对于列表同样适用，[1,3] < [1,5], [1,1]>[1].
        if i >= len(self.A[index]):
            self.A[index].append([self.snap_id, val])
        else:
            self.A[index][i][1] = val

    def snap(self) -> int:
        self.snap_id += 1
        return self.snap_id - 1

    def get(self, index: int, snap_id: int) -> int:
        i = bisect.bisect(self.A[index], [snap_id, float('inf')]) - 1
        return self.A[index][i][1]

# Your SnapshotArray object will be instantiated and called as such:
# obj = SnapshotArray(length)
# obj.set(index,val)
# param_2 = obj.snap()
# param_3 = obj.get(index,snap_id)
