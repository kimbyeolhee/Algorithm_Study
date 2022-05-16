# 2022-05-16
# 1:30-1:51

### sol1. ### 재귀로 품
import sys
sys.setrecursionlimit(10**7)

class Solution:
    def isHappy(self, n: int) -> bool:
        # 한 자리 숫자라면 그 값이 1이면 True  
        # 한 자리 숫자인데 짝수이면 False
        if (n < 10):
            if n == 1:
                return True
            elif n == 2 or n == 4 or n == 6 or n == 8:
                return False
        
        temp = 0
        for s in str(n):
            temp += int(s)**2
        return Solution.isHappy(self,temp)


### sol2. ### two pointer
class Solution:
    def isHappy(self, n: int) -> bool:
        temp = set()

        while n not in temp:
            temp.add(n)
            n = sum([int(x)**2 for x in str(n)])

            if n == 1:
                return True
        return False