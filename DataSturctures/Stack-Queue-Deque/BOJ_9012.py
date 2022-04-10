# 2022-04-05
# 3:52-실패

# 2022-04-06
# 6:57-7:04

import sys
def input():
  return sys.stdin.readline().rstrip()

# 입력 테스트 케이스
N = int(input())

for _ in range(N):
  ps = input()
  stack = []

  for p in ps:
    if p == '(':
      stack.append(p)
    elif p == ')':
      if len(stack) != 0 and stack[-1] == '(':
        stack.pop()
      else:
        stack.append(p)
  
  if len(stack) == 0:
    print('YES')
  else:
    print('NO')


# sol2
# import sys
# def input():
#   return sys.stdin.readline().rstrip()

# N = int(input()) # 입력 횟수
# result =""

# for i in range(N):
#   testcase = input()
#   cnt = 0
#   for c in testcase:
#     cnt += 1 if c == '(' else -1
#     if cnt < 0:
#       result += 'NO\n'
#       break
#   else:
#     result += 'YES\n' if cnt == 0 else "NO\n"

# print(result)