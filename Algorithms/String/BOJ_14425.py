# 2022-04-15
# 04:05-04:06

import sys

def input():
  return sys.stdin.readline().rstrip()

# N개의 문자열로 이루어진 집합 S, 확인할 문자열 수 M
N, M = map(int, input().split())
S = []
ans = 0

for _ in range(N):
  S.append(input())

for _ in range(M):
  s = input()
  if s in S:
    ans += 1

print(ans)