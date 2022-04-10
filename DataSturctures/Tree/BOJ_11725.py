# 2022-04-07
# 10:45-실패

# TODO: 다시풀기

### sol1 ###

import sys
sys.setrecursionlimit(10**9)
def input():
  return sys.stdin.readline().rstrip()

# 노드의 개수
n = int(input())

# 트리
graph = [[] for i in range(n+1)]
# 부모 노드 정보 저장 리스트
visited = [0]*(n+1)

# 트리 구조 입력
for i in range(n-1):
  a, b = map(int, input().split())
  graph[a].append(b)
  graph[b].append(a)

# 깊이 우선 탐색 방식
def dfs(s):
  for i in graph[s]:
    if visited[i] == 0:
      visited[i] = s
      dfs(i)

dfs(1)
for i in range(2, n+1):
  print(visited[i])




### sol2. bfs ###
from collections import deque
import sys
sys.setrecursionlimit(10**9)
def input():
  return sys.stdin.readline().rstrip()

# 노드의 개수
n = int(input())

# 트리
graph = [[] for i in range(n+1)]
# 부모 노드 정보 저장 리스트
visited = [0]*(n+1)

# 트리 구조 입력
for i in range(n-1):
  a, b = map(int, input().split())
  graph[a].append(b)
  graph[b].append(a)

# 넓이 우선 탐색 방식
def bfs(s):
  queue = deque()
  queue.append(s)

  while queue:
    v = queue.popleft()
    for i in graph[v]:
      if visited[i] == 0:
        visited[i] = v
        queue.append(i)

bfs(1)
for i in range(2, n+1):
  print(visited[i])