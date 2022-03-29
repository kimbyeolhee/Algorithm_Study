# 2022-03-29
# 10:59-11:02

import sys

def input():
  return sys.stdin.readline().rstrip()

result = 0

for _ in range(2):
  a = int(input())
  result += a

print(result)