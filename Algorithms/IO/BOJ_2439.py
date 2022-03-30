# 2022-03-29
# 11:59-12:03

# 2022-03-30
# 2:40-2:41

import sys
def input():
  return sys.stdin.readline().rstrip()

n = int(input())

for i in range(1, n+1):
  print(('*'*i).rjust(n))
