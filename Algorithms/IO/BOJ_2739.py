# 2022-03-29
# 4:34-

import sys
def input():
  return sys.stdin.readline().rstrip()

# 구구단의 단
n = int(input())

for i in range(1, 10):
  print(f'{n} * {i} = {n*i}')