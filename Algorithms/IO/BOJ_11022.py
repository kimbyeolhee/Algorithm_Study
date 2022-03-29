# 2022-03-29
# 1:37 - 1:39

import sys

def input():
  return sys.stdin.readline().rstrip()

# 입력받는 테스트 케이스 수
n = int(input())

for i in range(n):
  a, b = map(int, input().split())
  print(f'Case #{i+1}: {a} + {b} = {a+b}')