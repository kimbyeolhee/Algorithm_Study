# 2022-04-03
# 10:20-실패

# TODO: 다시풀기

from collections import deque
import sys

def input():
  return sys.stdin.readline().rstrip()

N = int(input())
dq = deque(enumerate(map(int, input().split())))
result = []

while dq:
  idx, paper = dq.popleft()
  result.append(idx+1)

  if paper > 0:
    dq.rotate(-(paper-1)) # 반시계
  elif paper < 0:
    dq.rotate(-paper) # 시계

print(' '.join(map(str, result)))



  