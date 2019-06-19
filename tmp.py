while True:
    try:
        s = input()
        words = list(input().split())
        n = len(s)
        if n <= 0 or not words:
            print(False)
            continue
        dp = [False for _ in range(n + 1)]  # dp[i]表示0~i-1的子串满足
        dp[0] = True
        for i in range(1, n + 1):
            ts = s[:i]
            for j in range(i):
                if dp[j] and ts[j:] in words:
                    dp[i] = True
                    continue
        print(dp[-1])
    except:
        break

'''
def read_data():
    import numpy as np
    mnist = np.load("C:/Users/Dawn/Desktop/mnist.npz")
    X = mnist["X"]
    return X


def cando(img):
    """输入为28*28图片,0代表黑，255代表白"""
    dx = [1, 1, 0, -1, -1, -1, 0, 1]
    dy = [0, 1, 1, 1, 0, -1, -1, -1]
    vis = [[False for _ in range(28)] for _ in range(28)]

    def dp(x, y):
        vis[x][y] = True
        for d in range(8):
            tmpx, tmpy = x + dx[d], y + dy[d]
            if 0 <= tmpx < 28 and 0 <= tmpy < 28 and vis[tmpx][tmpy] == False and img[tmpx][tmpy] == 255:
                dp(tmpx, tmpy)

    for i in range(28):
        for j in range(28):
            if img[i][j] == 255:
                dp(i, j)
                for q in range(28):
                    for w in range(28):
                        if vis[q][w] == False and img[q][w] == 255:
                            return False
                return True


X = read_data()
ans = 0
for i in range(len(X)):
    if cando(X[i]):
        ans += 1
print(ans)
'''
