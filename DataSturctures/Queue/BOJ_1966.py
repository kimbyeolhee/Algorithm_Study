# 2022-04-13
# 12:31-실패

# TODO: 다시풀기

import sys
from collections import deque
def input():
  return sys.stdin.readline().rstrip()

# 테스트 케이스 수 입력
test = int(input())

# 테스트 케이스 첫번째 줄: 문서의 개수, 몇 번째로 인쇄되었는지 궁금한 문서의 Queue idx
# 테스트 케이스 두번째 줄: N개 문서의 중요도들 (중요도가 같은 문서가 있을 수도 있음)
for i in range(test):
  N, M = map(int, input().split())
  importance = deque(list(map(int, input().split())))
  idx = deque(range(0, N)) # 문서의 idx
  
  cnt = 0
  
  while True:
    if importance[0] == max(importance):
      cnt += 1
      importance.popleft()

      if idx.popleft() == M:
        print(cnt)
        break
    
    else:
      importance.rotate(-1)
      idx.rotate(-1)
