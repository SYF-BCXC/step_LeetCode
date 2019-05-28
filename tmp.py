class Solution:
    def isahead(self, a, b):
        n, m = len(a), len(b)
        x, y = 0, 0
        count = 1
        while x < n and y < m:
            if a[x] != b[y]:
                if count == 1:
                    if n < m:
                        x -= 1
                    else:
                        y -= 1
                    count -= 1
                else:
                    return False
            x += 1
            y += 1
        return True

    def longestStrChain(self, words):
        """动态规划
        1. 原文题：长度为n能组成的最大长度;子问题：长度为n-1 能组成的最大长度
        2. 状态：dp[i]以i为最长单词能组成的最大词链
        3. 初始化：长度最小的word为1
        4. 动态转移方程：dp[i] = max(dp[j])+1,j指长度为k-1且为其前身的单词,k=len(words[i])
        """
        mywords = sorted(words, key=lambda x: len(x))
        n = len(mywords)
        dp = [1 for _ in range(n)]
        ans = 1
        base = len(mywords[0])

        for i in range(n):
            if len(mywords[i]) == base:
                dp[i] = 1
            elif len(mywords[i]) > base:
                for j in range(i - 1, -1, -1):
                    if 0 <= j < n and len(mywords[j]) == (len(mywords[i]) - 1) and self.isahead(mywords[i], mywords[j]):
                        dp[i] = max(dp[j] + 1, dp[i])
                        ans = max(ans, dp[i])
                    elif 0 <= j < n and len(mywords[j]) < (len(mywords[i]) - 1):
                        break
        return ans


s = Solution()
words = ["ksqvsyq", "ks", "kss", "czvh", "zczpzvdhx", "zczpzvh", "zczpzvhx", "zcpzvh", "zczvh", "gr", "grukmj",
         "ksqvsq", "gruj", "kssq", "ksqsq", "grukkmj", "grukj", "zczpzfvdhx", "gru"]
print(s.longestStrChain(words))
print(s.isahead("kss", "czvh"))
