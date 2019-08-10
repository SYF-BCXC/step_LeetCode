def flowerNum(num):
	pre = num
	all = 0
	while num!=0:
		all += ((num % 10)**3)
		num = num // 10
	if all == pre:
		return True
	else:
		return False

a, b = map(int, input().split())
time = 0
for i in range(a,b+1):
	if flowerNum(i):
		time += 1
		print(i, end=' ')
if time == 0:
	print('no')
else:
	print()

'''
# 又中间值确认，如例中的5/3,大于3/2小于2/1,此时求中则为所求
# 需要中间值求几次就是第几行

class node:
    def __init__(self, x, y):
        self.a = x
        self.b = y

    def getVal(self):
        if self.b == 0:
            return 0x7fffffff
        return self.a / self.b

    def getA(self):
        return self.a

    def getB(self):
        return self.b


def getMid(n1, n2):
    tmpa, tmpb = (n1.getA() + n2.getA()), (n1.getB() + n2.getB())
    tmp = node(tmpa, tmpb)
    return tmp


def isEqual(n1, n2):
    if n1.b == n2.b == 0 and n1.a == n2.a:
        return True
    else:
        if n1.a / n1.b == n2.a / n2.b:
            return True
        else:
            return False


left = node(0, 1)
right = node(1, 0)

tmpa, tmpb = input().split()
tmpa = int(tmpa)
tmpb = int(tmpb)
target = node(tmpa, tmpb)

mid = left
level = 0
track = ""

while not isEqual(mid, target):
    mid = getMid(left, right)
    level += 1
    if mid.getVal() > target.getVal():
        track += "0"
        right = mid
    else:
        track += "1"
        left = mid

ansa = level
tmp = track[:-1]
ansb = 0
if tmp == "":
    ansb = 1
else:
    ansb = int(tmp, 2) + 1
print(ansa,end=" ")
print(ansb)
'''

"""class Solution:
    def __init__(self):
        self.ans = False

    def solution(self, arr, item):
        if len(arr) == 1:
            if not item:
                if arr[0][0] == arr[0][-1]:
                    self.ans = True
            else:
                if item[0][0] == arr[0][-1] and item[-1][-1] == arr[0][0]:
                    self.ans = True
            return
        for i in range(len(arr)):
            if arr[i][0] == item[-1][-1]:
                self.solution(arr[0:i] + arr[i + 1:], item + [arr[i]])

    def p(self):
        if self.ans:
            print('true')
        else:
            print('false')


if __name__ == '__main__':
    s = Solution()
    words = list(input().split())
    if len(words) == 1:
        if words[0][0] == words[0][-1]:
            print('true')
        else:
            print('false')
    elif len(words) == 0:
        print('true')
    else:
        s.solution(words[:-1], [words[-1]])
        s.p()
"""
'''
# 不满足的数据，一定是同时大于两边或者同时小于两边
while True:
    try:
        A = [-10000000] + list(map(int, list(input().split())))
        A.append(10000000)
        B = list(map(int, list(input().split())))
        count = 0
        flag = False
        question = False
        if len(A) <= 3:
            for k in range(1, len(A) - 1):
                print(A[k], end=' ')
            print()
        else:
            for i in range(1, len(A) - 1):
                if (A[i] < A[i + 1] and A[i] < A[i - 1]) or (A[i] > A[i - 1] and A[i] > A[i + 1]):
                    question = True
                    for j in range(len(B)):
                        if A[i - 1] < B[j] < A[i + 1]:
                            A[i] = max(B[j], A[i])
                            flag = True
                    if flag:
                        count += 1
                        flag = False
            if count > 1 or (count == 0 and question == True):
                print("NO")
            else:
                for k in range(1, len(A) - 1):
                    print(A[k], end=' ')
                print()
    except:
        break
'''
