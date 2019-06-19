# 最快解答全是用int()直接转换的，不值得参考



class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        """模拟整数乘法过程。
        每位乘，最后add string
        """
        
        a, b = num1[::-1], num2[::-1]
        mid = []    # 存每位乘法的结果
        for i in range(len(a)):
            mid.append('0' * i + self.singleMul(b,a[i]))    # 不同位记得补0
        ans = '0'
        #print(mid)
        for i in mid:
            ans = self.add(i[::-1],ans)
        return ans
        
    def singleMul(self,num, single):
        carry = 0
        ans = ''
        for j in range(len(num)):
            tmp = int(single) * int(num[j]) + carry
            carry = tmp // 10
            tmp = tmp % 10
            ans += str(tmp)
        if carry != 0:
            ans += str(carry)
        return ans
        
    def add(self, num1, num2):
        #print(num1,num2)
        ans = ''
        carry = 0
        a, b = num1[::-1], num2[::-1]
        a_len, b_len = len(a), len(b)
        if a_len < b_len:
            a += '0' * (b_len - a_len)
        elif a_len > b_len:
            b += '0' * (a_len - b_len)
        for i in range(max(a_len, b_len)):
            tmp = int(a[i]) + int(b[i]) + carry
            carry = tmp // 10
            tmp = tmp % 10
            ans += str(tmp)
        if carry == 1:
            ans += '1'
        ans = ans[::-1]
        k = 0
        while ans[k] == '0' and k < len(ans)-1:
            k += 1
        return ans[k:]
            