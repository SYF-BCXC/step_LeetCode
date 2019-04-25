#!/usr/bin/python3

# @Project = step_LeetCode
# @File    : 1024_Video_Stitching
# @Author  : TCY
# @Time    : 2019/4/24 16:09
# @Email   : tangcaiyuan@hust.edu.cn
# @Software: PyCharm


class Solution(object):
    def videoStitching(self, clips, T):
        """
        :type clips: List[List[int]]
        :type T: int
        :rtype: int
        """
        """贪心算法。当前覆盖了[0,now]，找一个k,使得clips[k][0]<=now,并且使clips[k][1]尽可能大"""
        """注意一点，tmp初始化为None,因此可能没有tmp[1]；其次，对循环内完成查找和循环外完成查找都需要判定"""
        result = []
        now = 0
        while now < T:
            tmp = None
            for i in clips:
                if i[0] <= now:
                    if tmp == None:
                        tmp = i
                    else:
                        if tmp[1] < i[1]:
                            tmp = i
            if now >= T:
                return len(result)
            else:
                if tmp == None:
                    return -1
                else:
                    if now < tmp[1]:
                        now = tmp[1]
                        result.append(tmp)
                    else:
                        return -1
        if now < T:
            return -1
        else:
            return len(result)
