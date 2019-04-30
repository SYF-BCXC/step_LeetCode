#!/usr/bin/python3

# @Project = step_LeetCode
# @File    : 675_Cut_Off_Trees_for_Golf_Event
# @Author  : TCY
# @Time    : 2019/4/28 22:01
# @Email   : tangcaiyuan@hust.edu.cn
# @Software: PyCharm


import queue

"""虽然超时了，但是好像是因为Python语言本身速度慢的原因，思路没有错，用python通过的用的是一个Hadlock's algorithm算法。目前想先刷常规题与常规思路，这个算法就先搁置吧。代码如下：
class Solution(object):
    def cutOffTree(self, forest):
        # Add sentinels (a border of zeros) so we don't need index-checks later on.
        forest.append([0] * len(forest[0]))
        for row in forest:
            row.append(0)

        # Find the trees.
        trees = [(height, i, j)
                 for i, row in enumerate(forest)
                 for j, height in enumerate(row)
                 if height > 1]

        # Can we reach every tree? If not, return -1 right away.
        queue = [(0, 0)]
        reached = set()
        for i, j in queue:
            if (i, j) not in reached and forest[i][j]:
                reached.add((i, j))
                queue += (i+1, j), (i-1, j), (i, j+1), (i, j-1)
        if not all((i, j) in reached for (_, i, j) in trees):
            return -1

        # Distance from (i, j) to (I, J).
        def distance(i, j, I, J):
            now, soon = [(i, j)], []
            expanded = set()
            manhattan = abs(i - I) + abs(j - J)
            detours = 0
            while True:
                if not now:
                    now, soon = soon, []
                    detours += 1
                i, j = now.pop()
                if (i, j) == (I, J):
                    return manhattan + 2 * detours
                if (i, j) not in expanded:
                    expanded.add((i, j))
                    for i, j, closer in (i+1, j, i < I), (i-1, j, i > I), (i, j+1, j < J), (i, j-1, j > J):
                        if forest[i][j]:
                            (now if closer else soon).append((i, j))

        # Sum the distances from one tree to the next (sorted by height).
        trees.sort()
        return sum(distance(i, j, I, J) for (_, i, j), (_, I, J) in zip([(0, 0, 0)] + trees, trees))
        """
class Solution:
    def cutOffTree(self, forest):
        """分为两部分，先排序一个存放元组(height,i,j)的List，然后写一个BFS(获取从A点到B点需要走的步数)，最后遍历List获得总步数"""
        """BFS部分
        1. 确定搜索范围
        2. 用队列进行搜索
        BFS与DFS，需要提前准备的变量：dx，dy，n, m, vis，
        """
        dx = [0, 0, -1, 1]
        dy = [1, -1, 0, 0]
        n, m = len(forest), len(forest[0])

        def BFS(forest, x, y, tx, ty):
            if x == tx and y == ty:
                return 0
            vis = [[False for _ in range(m)] for _ in range(n)]
            q = queue.Queue()
            q.put((x, y))
            crt = 0
            while not q.empty():
                crt += 1
                for k in range(q.qsize()):
                    r, c = q.get()
                    for i in range(4):
                        tmpx, tmpy = r + dx[i], c + dy[i]
                        if 0 <= tmpx < n and 0 <= tmpy < m and vis[tmpx][tmpy] == False and forest[tmpx][tmpy] != 0:
                            if tmpx == tx and tmpy == ty:
                                return crt
                            vis[tmpx][tmpy] = True
                            q.put((tmpx, tmpy))
            return -1

        """排序元祖List部分"""
        trees = []
        for i in range(n):
            for j in range(m):
                if forest[i][j] > 1:
                    trees.append((forest[i][j], i, j))
        sorted_trees = sorted(trees, key=lambda x: x[0])
        nowx, nowy = 0, 0
        ans = 0
        for i in sorted_trees:
            tmp = BFS(forest, nowx, nowy, i[1], i[2])
            nowx, nowy = i[1], i[2]
            if tmp == -1:
                return -1
            else:
                ans += tmp
        return ans


s = Solution()
t = [
    [1, 2, 3],
    [0, 0, 4],
    [7, 6, 5]
]
print(s.cutOffTree(t))
