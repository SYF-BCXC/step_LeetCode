#!/usr/bin/python3

# @Project = leetCode
# @File    : 4_Median_of_Two_Sorted_Arrays
# @Author  : TCY
# @Time    : 2018/9/15 19:47
# @Email   : tangcaiyuan@hust.edu.cn
# @Software: PyCharm

"""
题目描述:
https://leetcode-cn.com/problems/median-of-two-sorted-arrays/description/
思路:
1、 分别得到两个List的的长度m和n，求和，找中间位置。如果是奇数，int(7/2)+1 = 4。
    如果是偶数,8/2=4，再加上5。接下来就是找第a小的问题，分别两个指针指向两个数组的第一个位置，
    谁更下就下标加1，且a-=1，直到a==0;
2、 有序数组合并，直接取中间位置即可(由于两个数组都是有序的，时间复杂度并不会超。且最快解答中，居然直接使用sort()函数排序，也没有超时。排序最低也是nlogn，暂时还不清楚是为什么)
"""

# 思路一的失败。主要难在数组边界的判断，以及选择第a+1号数时的难度
"""
class Solution:
    def findMedianSortedArrays(self, nums1, nums2):

        # 思路1：分别得到两个List的的长度m和n，求和，找中间位置。如果是奇数，int(7/2)+1 = 4。
        # 如果是偶数,8/2=4，再加上5。接下来就是找第a小的问题，分别两个指针指向两个数组的第一个位置，
        # 谁更下就下标加1，且a-=1，直到a==0;
        m = len(nums1)
        n = len(nums2)
        a, temp = divmod(m+n, 2)
        a_piont = 0
        b_piont = 0
        a_flag = 0  # a_piont未到最后为0，到最后了为1
        b_flag = 0  # b_piont未到最后为0，到最后了为1
        # 先找到第a个
        while a > 1:
            # 开始减小
            if nums1[a_piont]<nums2[b_piont]:
                # 第一个list更小，如果+1未越界，让a_piont+1；否则让b+1,且a设置为到末尾
                if a_piont+1 < m:
                    a_piont += 1
                else:
                    b_piont += 1
                    a_flag = 1
            else:
                if b_piont+1 < n:
                    b_piont += 1
                else:
                    a_piont += 1
                    b_flag = 1
            a -= 1
        if a_piont+1==m:
            a_flag = 1
        if b_piont+1==n:
            b_flag =1
        # 此时两个指针所指的值更小的那个正好就是第a小个
        if temp == 0:
            # 偶数个,找两个,a,a+1
            if nums1[a_piont]<nums2[b_piont]:
                if nums1[a_piont+1]>nums2[b_piont]:
                    #此时为a,b
                    return (nums1[a_piont]+nums2[b_piont])/2
                else:
                    #此时为a,a+1
                    return (nums1[a_piont] + nums1[a_piont+1]) / 2
            else:
                if nums2[b_piont+1]>nums1[a_piont]:
                    #此时为b,a
                    return (nums1[a_piont] + nums2[b_piont]) / 2
                else:
                    #此时为b,b+1
                    return (nums2[b_piont] + nums2[b_piont + 1]) / 2
        else:
            # 奇数个，找一个，a+1
            if nums1[a_piont]<nums2[b_piont]:
                if a_flag:
                    # A到了最后，
                    return nums2[b_piont]
                else:
                    if nums1[a_piont+1]>nums2[b_piont]:
                        #此时为b
                        return nums2[b_piont]
                    else:
                        #此时为a+1
                        return nums1[a_piont+1]
            else:
                if nums2[b_piont+1]>nums1[a_piont]:
                    #此时为a
                    return nums1[a_piont]
                else:
                    #此时为b+1
                    return nums2[b_piont + 1]
"""


class Solution:
    def mergeArray(self,nums1,nums2):
        # 有序数组合并，返回有序数组
        my_nums = []
        m = len(nums1)
        n = len(nums2)
        a_point = 0
        b_point = 0
        a_flag = 1
        b_flag = 1
        if not nums1:
            return nums2
        if not nums2:
            return nums1
        while a_flag and b_flag:
            if nums1[a_point] < nums2[b_point]:
                my_nums.append(nums1[a_point])
                a_point += 1
                if a_point == m:
                    a_flag = 0
            else:
                my_nums.append(nums2[b_point])
                b_point += 1
                if b_point == n:
                    b_flag = 0
        if a_flag == 0:
            my_nums.extend(nums2[b_point:])
        if b_flag == 0:
            my_nums.extend(nums1[a_point:])
        return my_nums

    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        #思路2：有序数组合并，直接取中间位置即可
        m = len(nums1)
        n = len(nums2)
        my_nums = self.mergeArray(nums1, nums2)
        a, temp = divmod(m + n, 2)
        if temp == 0:
            # 偶数个
            return (my_nums[a] + my_nums[a - 1]) / 2
        else:
            # 奇数个
            return my_nums[a]


if __name__ == '__main__':
    nums1 = [1, 3, 5, 6]
    nums2 = [3, 4]
    print(Solution().findMedianSortedArrays(nums1, nums2))

