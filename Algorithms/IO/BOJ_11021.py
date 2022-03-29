# 2022-03-29
# 1:24 - 1:28

import sys

def input():
  return sys.stdin.readline().rstrip()

# 테스트 케이스 수
n = int(input())

for i in range(n):
  a, b = map(int, input().split())
  print(f'Case #{i+1}: {a+b}')
