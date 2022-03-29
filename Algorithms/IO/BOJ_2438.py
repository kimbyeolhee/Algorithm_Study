# 2022-03-29
# 11:56-11:58

import sys
def input():
  return sys.stdin.readline().rstrip()

# 별의 개수
n = int(input())

for i in range(1,n+1):
  print('*'*i)