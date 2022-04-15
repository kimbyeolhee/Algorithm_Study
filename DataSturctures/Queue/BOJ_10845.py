# 2022-04-06
# 5:43- 5:54

import sys
def input():
  return sys.stdin.readline().rstrip()

class Queue:
  def __init__(self):
    self.queue = []
  
  def push(self, x):
    self.queue.append(x)

  def pop(self):
    if self.empty() == 1:
      return -1
    out = self.queue[0]
    self.queue = self.queue[1:]
    return out

  def size(self):
    return len(self.queue)
  
  def empty(self):
    if self.size() == 0:
      return 1
    else:
      return 0
  
  def front(self):
    if self.empty() == 1:
      return -1
    return self.queue[0]
  
  def back(self):
    if self.empty() == 1:
      return -1
    return self.queue[-1]

# 명령 입력 개수
N = int(input())
q = Queue()

for _ in range(N):
  command = input().split()
  if command[0] == "push":
    q.push(int(command[1]))
  elif command[0] == "pop":
    print(q.pop())
  elif command[0] == "size":
    print(q.size())
  elif command[0] == "empty":
    print(q.empty())
  elif command[0] == "front":
    print(q.front())
  elif command[0] == "back":
    print(q.back())