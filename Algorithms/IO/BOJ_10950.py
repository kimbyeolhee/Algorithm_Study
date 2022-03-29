# 2022-03-29
# 11:09-11:10

import sys

def input():
  return sys.stdin.readline().rstrip()

n = int(input())
for _ in range(n):
  a, b = map(int, input().split())
  print(a+b)