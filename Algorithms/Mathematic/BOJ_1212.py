# 2022-05-18
# 1:21-1:30

import sys
def input():
  return sys.stdin.readline().rstrip()

# 8진수가 주어졌을 때, 2진수로 변환
input = input() # 입력받는 8진수
 
def oct2bin(n):
  if n == 0:
    return 0
  else:
    return bin(int(n, 8))[2:]

print(oct2bin(input))