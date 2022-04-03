# 2022-04-03
# 08:38-실패

# TODO: 다시풀기

import sys
from collections import deque

def input():
  return sys.stdin.readline().rstrip()

# 큐의 크기, 뽑아내려는 수의 개수
N, M = map(int, input().split())
# 뽑아내려고 하는 수의 위치
pos = list(map(int, input().split()))


# 첫번째 원소만 뽑아낼 수 있다. 뽑아낼 원소를 첫번째로 보내는 작업이 필요(왼쪽/오른쪽 한칸씩 이동)
dq = deque([k for k in range(1, N+1)])
answer = 0

for i in pos:
  while True:
    if dq[0] == i:
      dq.popleft()
      break
    else:
      if dq.index(i) < len(dq)/2:
        while dq[0] != i:
          dq.append(dq.popleft())
          answer += 1
      else:
        while dq[0] != i:
          dq.appendleft(dq.pop())
          answer += 1

print(answer)