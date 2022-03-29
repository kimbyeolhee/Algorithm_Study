# 2022-03-29
# 1:11 - 1:13

import sys

def input():
  return sys.stdin.readline().rstrip()

# 테스트 케이스 수
n = int(input())

for _ in range(n):
  a, b = map(int, input().split(','))
  print(a+b)
