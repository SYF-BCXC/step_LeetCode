# string整数加法


class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
        carry = 0
        ans = ''
        a,b = num1[::-1], num2[::-1]
        a_len, b_len = len(a), len(b)
        if a_len < b_len:
            a = a + '0'*(b_len-a_len)
        elif a_len > b_len:
            b = b + '0' * (a_len - b_len)
        for i in range(max(a_len,b_len)):
            tmp = int(a[i]) + int(b[i]) + carry
            carry = tmp // 10
            tmp = tmp % 10
            ans += str(tmp)
        if carry == 1:
             ans += '1'
        return ans[::-1]