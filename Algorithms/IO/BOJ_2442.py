# 2022-03-30
# 2:30-2:35

# 2022-03-30
# 14:50-14:55

import sys
def input():
  return sys.stdin.readline().rstrip()

# 빈칸은 4 -> 3 -> 2 -> 1 -> 0
# 별은 1 -> 3 -> 5 -> 7 -> 9

n = int(input())

for i in range(n):
  print(' '*(n-i-1) + '*'*(2*i+1))
