# 2022-03-29
# 11:41-11:43

import sys

def input():
  return sys.stdin.readline().rstrip()

while True:
  a, b = map(int, input().split())
  if a == 0 and b == 0:
    break
  print(a+b)