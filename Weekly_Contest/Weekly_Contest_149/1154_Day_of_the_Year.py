#!/usr/bin/python3

# @Project = step_LeetCode
# @File    : 1154_Day_of_the_Year
# @Author  : TCY
# @Time    : 2019/8/11 22:07
# @Email   : tangcaiyuan@hust.edu.cn
# @Software: PyCharm

import datetime
class Solution:
    def ordinalOfDate(self, date: str) -> int:
        dd = datetime.datetime.strptime(date,"%Y-%m-%d")
        return dd.timetuple().tm_yday