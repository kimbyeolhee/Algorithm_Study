# 2022-03-30
# 12:08-12:09

import sys
def input():
  return sys.stdin.readline().rstrip()

n = int(input())

for i in range(n,0,-1):
  print(('*'*i).rjust(n))