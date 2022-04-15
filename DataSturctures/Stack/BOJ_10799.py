# 2022-04-06
# 5:19-실패

# TODO: 다시풀기

import sys
def input():
  return sys.stdin.readline().rstrip()

# 쇠막대기와 레이저 입력
bar_razor = input()
ans = 0
stack = []

for i in range(len(bar_razor)):
  if bar_razor[i] == "(":
    stack.append(i)

  else:
    if bar_razor[i-1] == "(":
      stack.pop()
      ans += len(stack)
    
    else:
      stack.pop()
      ans += 1

print(ans)
