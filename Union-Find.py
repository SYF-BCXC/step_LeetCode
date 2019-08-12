#!/usr/bin/python3

# @Project = step_LeetCode
# @File    : Union-Find
# @Author  : TCY
# @Time    : 2019/8/10 21:12
# @Email   : tangcaiyuan@hust.edu.cn
# @Software: PyCharm

"""
并查集的实现。
本质是树。

"""

f = list(range(100))

def find(x):
    if x != f[x]:
        f[x] = find(f[x])
    return f[x]

def union(x,y):
    x = find(x)     # 最终总会指向根节点
    y = find(y)
    if x != y:
        f[x] = y

print('原始集合',f)
while True:
    a, b = list(map(int, input().split()))
    union(a,b)
    print(f)
