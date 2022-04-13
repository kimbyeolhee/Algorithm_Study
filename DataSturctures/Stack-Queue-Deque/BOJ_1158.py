# 2022-04-12
# 1:30-1:35

import sys
from collections import deque

def input():
  return sys.stdin.readline().rstrip()

#  N명의 사람이 원을 이루면서 앉아있고, K번째 사람을 제거
n, k = map(int, input().split())
dq = deque(range(1, n+1))
answer = []
while dq:
  dq.rotate(-(k-1))
  answer.append(dq.popleft())

print("<", end="")
for i in answer[:-1]:
  print(i, end=", ")
print(answer[-1], end=">")