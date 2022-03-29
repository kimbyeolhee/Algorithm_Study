# 2022-03-30
# 3:08- 3:20

import sys
def input():
  return sys.stdin.readline().rstrip()

n = int(input())

for i in range(n):
  print(' '*(n-i-1) + '*' + ' *'*i)

