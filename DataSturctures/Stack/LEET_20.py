# 2022-04-16
# 4:55-실패

# TODO 다시풀기

class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        table = {
            ')':'(',
            '}':'{',
            ']':'[',
        }
        
        for char in s:
            if char not in table:
                stack.append(char)
            elif not stack or table[char] != stack.pop():
                return False
        return len(stack) == 0