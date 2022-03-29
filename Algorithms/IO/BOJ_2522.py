# 2022-03-30
# 02:49-2:52

import sys
def input():
  return sys.stdin.readline().rstrip()

n = int(input())
for i in range(1,n+1):
  print(('*'*i).rjust(n))
for i in range(n-1,0,-1):
  print(('*'*i).rjust(n))