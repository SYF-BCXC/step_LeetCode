#!/usr/bin/python3

# @Project = step_LeetCode
# @File    : 215_Kth_Largest_Element_in_an_Array
# @Author  : TCY
# @Time    : 2019/5/2 0:14
# @Email   : tangcaiyuan@hust.edu.cn
# @Software: PyCharm
"""python 之 heap
https://blog.csdn.net/a529975125/article/details/83315727
"""


"""最快解答
        heap = nums[:k]
        heapq.heapify(heap)
        for num in nums[k:]:
            if num > heap[0]:
                heapq.heappushpop(heap, num)
        return heap[0]
"""


class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        def partition(nums, l, r):
            if not nums or l > r:
                return -1
            k = nums[l]
            while l < r:
                while l < r and nums[r] > k:
                    r -= 1
                nums[l] = nums[r]
                while l < r and nums[l] <= k:
                    l += 1
                nums[r] = nums[l]
            nums[l] = k
            return l

        l, r = 0, len(nums) - 1
        k = len(nums) - k
        while True:
            tmp = partition(nums, l, r)
            if tmp == k:
                return nums[tmp]
            elif tmp < k:
                l = tmp + 1
            elif tmp > k:
                r = tmp - 1
