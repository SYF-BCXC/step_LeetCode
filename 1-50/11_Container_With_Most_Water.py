#!/usr/bin/python3

# @Project = step_LeetCode
# @File    : 11_Container_With_Most_Water
# @Author  : TCY
# @Time    : 2018/9/27 1:24
# @Email   : tangcaiyuan@hust.edu.cn
# @Software: PyCharm

"""
题目描述:
https://leetcode-cn.com/problems/container-with-most-water/description/
思路:
1、暴力法。超时
2、贪心策略。从左到右扫描，每个值从两边开始找第一个大于该值的值。超时
3、双指针法。一个指针放左一个放右，每次让短的那个向长的靠拢。最快,o(n)
"""


class Solution:
    # 方法1，超时
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        my_max = 0
        for i in range(len(height)):
            for j in range(i, len(height)):
                temp = (j - i) * min(height[i], height[j])
                if temp > my_max:
                    my_max = temp
        return my_max

    def maxArea2(self, height):
        temp = 0
        for i in range(len(height)):
            for l in range(i):
                if height[l] >= height[i]:
                    if (i - l) * height[i] > temp:
                        temp = (i - l) * height[i]
                        break
        for i in range(len(height)):
            for r in range(len(height) - 1, i, -1):
                if height[r] >= height[i]:
                    if (r - i) * height[i] > temp:
                        temp = (r - i) * height[i]
                        break
        return temp

    # 此为最快解法
    def maxArea3(self, height):
        l, r, temp = 0, len(height) - 1, 0
        while r != l:
            m_len = min(height[l], height[r])
            if (r - l) * m_len > temp:
                temp = (r - l) * m_len
            while height[l] <= m_len and l < r:
                l += 1
            while height[r] <= m_len and l < r:
                r -= 1
            """ 这个方法太麻烦，上面用while可以加快速度
            if height[l] < height[r]:
                l += 1
            else:
                r -= 1
            """
        return temp


if __name__ == '__main__':
    print(Solution().maxArea3([1, 8, 6, 2, 5, 4, 8, 3, 7]))
