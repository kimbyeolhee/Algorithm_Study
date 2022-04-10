# 2022-04-07
# 7:13-7:18

# TODO: 다시풀기

class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        
        strs = []
        # 문자열 전처리 (알파벳, 숫자 아닌 것 제거 및 소문자화)
        for c in s:
            if c.isalnum():
                strs.append(c.lower())
        
        # 펠린드롬 여부 확인
        return strs == strs[::-1]