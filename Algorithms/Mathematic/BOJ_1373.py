# 2022-04-16
# 4:05-4:18

# 2진수 => 8진수로 출력

import sys
def input():
  return sys.stdin.readline().rstrip()

input = input()
# 입력값(2진수) => 10진수 => 8진수
def bin2oct(bin):
  temp = int(bin, 2)
  print(oct(temp)[2:])

bin2oct(input)
