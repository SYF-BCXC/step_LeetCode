"""
很好的题。
1. 长度不对的直接返回空
2. 除了判断在0到255之内以外，还得注意考虑长度大于1时首位不能为0的情况
"""


class Solution:
    def achieve(self, s):
        """判断s是否是一个符合规则的整数字符串
        1. 范围处于[0,255]
        2. 若长度大于1，则首位不呢为0
        """
        if 0 <= int(s) <= 255:
            if len(s) > 1 and s[0] != '0':
                return True
            elif len(s) == 1:
                return True
        return False
    
    def restoreIpAddresses(self, s: str) -> List[str]:
        """四个切分点，切分完成后如果每个都满足在0到255内则是一种解
        注意考虑每块第一位不能是0
        """
        if (len(s) > 12 or len(s) < 4):
            return []
        ans = []
        for a in range(1,len(s)-2):
            for b in range(a+1,len(s)-1):
                for c in range(b+1,len(s)):
                    sa, sb, sc, sd = s[0:a], s[a:b], s[b:c], s[c:]
                    if  self.achieve(sa) and self.achieve(sb) and self.achieve(sc) and self.achieve(sd):
                        ans.append(sa+'.'+ sb + '.' + sc + '.' + sd)
        return ans