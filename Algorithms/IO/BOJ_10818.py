# 2022-03-29
# 11:50-11:53

import sys
def input():
  return sys.stdin.readline().rstrip()

n = int(input())
n_list = list(map(int, input().split()))

print(f'{min(n_list)} {max(n_list)}')