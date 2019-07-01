"""
bfs
1. dx,dy,vis[][]
2. 访问做的操作
3. 4个方向的探索，要加判断条件
"""

class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        self.area = 0
        vis = [[False for _ in range(len(grid[0]))] for _ in range(len(grid))]
        ans = 0
        dx = [1, 0, -1, 0]
        dy = [0, 1, 0, -1]
        
        def dfs(vis,grid,x,y):
            if grid[x][y] != 1:
                return 0
            self.area += 1
            vis[x][y] = True
            
            for i in range(4):
                tmpx = x + dx[i]
                tmpy = y + dy[i]
                if 0 <= tmpx < len(grid) and 0 <= tmpy < len(grid[0]) and vis[tmpx][tmpy] == False:
                    dfs(vis,grid,tmpx,tmpy)
        
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                self.area = 0
                if vis[i][j] == False:
                    dfs(vis,grid,i,j)
                if self.area > ans:
                    ans = self.area
        return ans