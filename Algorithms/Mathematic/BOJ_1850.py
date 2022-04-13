# 2022-04-13
# 11:41-실패

# TODO: 다시풀기

import sys
def input():
  return sys.stdin.readline().rstrip()

A, B = map(int, input().split())

# 최대공약수
def gcd(a, b):
  while b > 0:
    a, b = b, a % b
  return a

print(gcd(A, B)*'1')

# A와 B의 1의 개수가 a, b인 경우 A, B의 최대 공약수는 1이 a,b의 최대공약수 개수만큼 구성된 수와 같다.