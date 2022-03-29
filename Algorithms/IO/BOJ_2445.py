# 2022-03-30
# 2:38-2:48

import sys
def input():
  return sys.stdin.readline().rstrip()

n = int(input())

for i in range(1,n+1):
  print('*'*i + ' '*(2*n-2*i) + '*'*i)
for i in range(n-1,0,-1):
  print('*'*i + ' '*(2*n-2*i) + '*'*i)