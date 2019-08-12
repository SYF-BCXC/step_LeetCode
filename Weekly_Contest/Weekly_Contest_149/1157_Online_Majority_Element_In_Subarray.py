#!/usr/bin/python3

# @Project = step_LeetCode
# @File    : 1157_Online_Majority_Element_In_Subarray
# @Author  : TCY
# @Time    : 2019/8/11 22:13
# @Email   : tangcaiyuan@hust.edu.cn
# @Software: PyCharm

"""
该做法虽然能通过，但是更关键的在于超过元素一半的解法(虽然python莫名超时,C++却ok)
a = self.a[left]
t = 1
for i in range(left+1, right+1):
    if self.a[i] == a:
        t += 1
    else:
        t -= 1
        if t <= 0:
            a = self.a[i]
            t = 1
t = 0
for i in range(left, right+1):
    if self.a[i] == a:
        t += 1
if t >= threshold:
    return a
else:
    return -1

奇淫技巧(不保证能100%正确，但是大概率正确):
https://www.youtube.com/watch?v=soR1-xscM94         25分钟附近

也可以进来的时候统计每个字符所在的位置.
a = collections.defaultdict(list)
for loc,val in enumerate(arr):
    a[val].append(loc)
然后，直接用k = random.randomint(left,right)  #可以取到right
然后用bisect.bisect_left 和 bisect_right找left和right在self.a[k]的位置
如果差值大于threshold就说明找到了，重复多次，未果则返回-1
"""


class MajorityChecker:

    def __init__(self, arr: List[int]):
        self.a = arr

    def query(self, left: int, right: int, threshold: int) -> int:
        tmp = self.a[left:right + 1]
        c = collections.Counter(tmp)
        for k, v in c.items():
            if v >= threshold:
                return k
        return -1
