# 2022-03-30
# 2:52-2:57

# 2022-03-30
# 14:56- 15:03

import sys
def input():
  return sys.stdin.readline().rstrip()

n = int(input())

# 빈칸: 0 -> 1 -> 2 -> 3 -> 4    -> 3 -> 2 -> 1 -> 0
# 별:   9 -> 7 -> 5 -> 3 -> 1    -> 3 -> 5 -> 7 -> 9

for i in range(n):
  print(' '*(i) + '*'*(2*n - 2*i - 1))
for j in range(1, n):
  print(' '*(n-j-1) + '*'*(2*j+1))
