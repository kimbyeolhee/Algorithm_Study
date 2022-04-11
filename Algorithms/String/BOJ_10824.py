# 2022-04-11
# 6:00-6:03

import sys
def input():
  return sys.stdin.readline().rstrip()

# 네가지 수 입력
A, B, C, D = map(int, input().split())

num1 = int(str(A)+str(B))
num2 = int(str(C)+str(D))

print(num1+num2)