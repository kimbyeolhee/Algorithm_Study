# 2022-04-15
# 5:00-실패

# TODO: 다시풀기

import sys
from collections import deque

def input():
  return sys.stdin.readline().rstrip()

N = int(input()) # 피연산자 개수 입력
postfix = input() # 후위표기식 입력
oper = '+-*/'
dic = {}
stack = []
num = deque() # 피연산자 대응값 입력 숫자 저장

for i in range(N):
  num.append(int(input())) # 피연산자 대응값에 해당할 숫자 입력

for i in postfix:
  if i not in dic and i not in oper: # ABC*+DE/- 의 경우 ABCDE
    dic[i] = num.popleft() # 피연산자 대응값 딕셔너리 형태 저장

for i in postfix:
  if i not in oper:
    stack.append(dic[i])
  else:
    if i == '+':
      a = stack.pop()
      b = stack.pop()
      stack.append(a+b)
    elif i == '-':
      a = stack.pop()
      b = stack.pop()
      stack.append(b-a)
    elif i == '*':
      a = stack.pop()
      b = stack.pop()
      stack.append(a*b)
    else:
      a = stack.pop()
      b = stack.pop()
      stack.append(b/a)

print(f"{stack[0]:.2f}")