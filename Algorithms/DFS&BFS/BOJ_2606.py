# 2022-05-19
# 10:00-

# TODO: 다시풀기

import sys
def input():
  return sys.stdin.readline().rstrip()

# 컴퓨터 수
N = int(input())
# 네트워크 상에서 직접 연결되어 있는 컴퓨터 쌍의 수
M = int(input())
# 경로 저장 리스트
network = [[]*N for _ in range(N+1)]
for _ in range(M):
  a, b = map(int, input().split())
  network[a].append(b)
  network[b].append(a)

cnt = 0
visited = [0]*(N+1)
def dfs(start):
  global cnt
  visited[start] = 1
  for i in network[start]:
    if visited[i] == 0:
      dfs(i)
      cnt += 1

dfs(1)
print(cnt)