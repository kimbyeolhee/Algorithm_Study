# 2022-03-30
# 3:23- 3:33

import sys
def input():
  return sys.stdin.readline().rstrip()

n = int(input())

for i in range(n):
  if(i == n-1 or i == 0):
    print(' '*(n-i-1) + '*'*(2*i+1))
  else:
    print(' '*(n-i-1) +'*' + ' '*(2*i -1)  +'*')