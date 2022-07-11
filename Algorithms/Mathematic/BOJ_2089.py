# 2022-07-11
# 3:11 -

import sys

def input():
  return sys.stdin.readline().rstrip()

# input: 10진수
# return: -2진수
## (-2)^0 = 1, (-2)^1 = -2, (-2)^2 = 4, (-2)^3 = -8

num = int(input())
answer = ''

while (num != 0):
  if (num % (-2) != 0):
    num = num // (-2) + 1
    answer += '1'
  else:
    num = num // (-2)
    answer += '0'

if (answer == ""):
  answer = '0'

print(answer[::-1])
