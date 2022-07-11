# 2022-05-21
# 6:30-

# TODO: 다시풀기

### dfs ###
# 방문하지않았다면 DFS를 돌려서 방문처리
# 방문처리하지 않은 컴퓨터를 찾으면 cnt += 1
def solution(n, computers):
  def dfs(i):
    visited[i] = 1
    for a in range(n):
      if computers[i][a] and not visited[a]:
        dfs(a)
  
  cnt = 0
  visited = [0 for i in range(len(computers))]

  for i in range(n):
    if not visited[i]:
      dfs(i)
      cnt += 1
  return cnt


### bfs ###
from collections import deque

def solution(n, computers):
  def bfs(i):
    queue = deque()
    queue.append(i)
    
    while queue:
      temp = queue.popleft()
      visited[temp] = 1
      for a in range(n):
        if computers[temp][a] and not visited[a]:
          queue.append(a)

  cnt = 0
  visited = [0 for i in range(len(computers))]

  for i in range(n):
    if not visited[i]:
      bfs(i)
      cnt += 1
  return cnt