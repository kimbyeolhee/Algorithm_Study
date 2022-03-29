# 2022-03-29
# 3:30 - 3:32

import sys

def input():
  return sys.stdin.readline().rstrip()

# 입력 숫자 개수
n = int(input())

# 계산
result = 0
command = input()
for i in range(n):
  result += int(command[i])
print(result)

## 굳이 입력 숫자 개수를 활용할 필요가 없을 경우
# command = input()
# for c in command:
#   result += int(c)
# print(result)