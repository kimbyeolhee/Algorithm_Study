# 2022-03-29
# 11:38-11:41

import sys

def input():
  return sys.stdin.readline().rstrip()

# 입력 n
n = int(input())
result = 0
for i in range(1, n+1):
  result += i
print(result)