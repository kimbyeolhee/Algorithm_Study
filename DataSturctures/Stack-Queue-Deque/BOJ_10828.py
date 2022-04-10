# 2022-04-05
# 3:37-3:45

# push X: 정수 X를 스택에 넣는 연산이다.
# pop: 스택에서 가장 위에 있는 정수를 빼고, 그 수를 출력한다. 만약 스택에 들어있는 정수가 없는 경우에는 -1을 출력한다.
# size: 스택에 들어있는 정수의 개수를 출력한다.
# empty: 스택이 비어있으면 1, 아니면 0을 출력한다.
# top: 스택의 가장 위에 있는 정수를 출력한다. 만약 스택에 들어있는 정수가 없는 경우에는 -1을 출력한다.

import sys
def input():
  return sys.stdin.readline().rstrip()

class Stack:
  def __init__(self):
    self.stack = []
  
  def push(self, x):
    self.stack.append(x)
  
  def pop(self):
    if self.empty() == 1:
      return -1
    return self.stack.pop()

  def size(self):
    return len(self.stack)

  def empty(self):
    if self.size() == 0:
      return 1
    return 0
  
  def top(self):
    if self.empty() == 1:
      return -1
    return self.stack[-1]


# 명령의 수 입력
n = int(input())

# 스택 생성
stack = Stack()

for _ in range(n):
  # 명령 입력
  command = input().split()
  
  if command[0] == 'push':
    stack.push(int(command[1]))
  elif command[0] == 'pop':
    print(stack.pop())
  elif command[0] == 'size':
    print(stack.size())
  elif command[0] == 'empty':
    print(stack.empty())
  elif command[0] == 'top':
    print(stack.top())

