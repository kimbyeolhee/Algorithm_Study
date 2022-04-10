# 2022-04-07
# 6:50-실패

# TODO: 다시풀기

# sol1. deque 이용
from collections import deque

class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        strs = deque([i for i in str(x)])

        while len(strs) > 1:
          if strs.popleft() != strs.pop():
            return False
        
        return True

# sol2. 슬라이싱
class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        strs = str(x)
        strs_head = strs[:len(strs)//2]
        strs_tail = strs[len(strs)//2:] if len(strs)%2 == 0 else strs[len(strs)//2+1:]
        return strs_head == strs_tail[::-1]