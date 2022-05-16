# 2022-04-16
# 3:22-3:44

import sys
def input():
  return sys.stdin.readline().rstrip()

## solution 1. ##
# 진법
notation = "1234556789ABCDEFGHIJKLMNOPQRSTUVWXYZ"

# 입력
N, B = input().split()
N = list(N)
B = int(B)

# 10진법 변환
answer = 0
for i, val in enumerate(N[::-1]):
  if val.isalpha():
    answer += (notation.index(val) * (B ** i))
  else:
    answer += int(val) * (B ** i)

print(answer)



## solution 2 ##
N, B = input().split()

print(int(N, int(B)))