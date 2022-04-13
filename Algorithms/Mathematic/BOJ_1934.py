# 2022-04-13
# 11:38-11:41

import sys

def input():
  return sys.stdin.readline().rstrip()

# 테스트 케이스 개수
t = int(input())

# 최대공약수 함수
def gcd(a, b):
  while b > 0:
    a, b = b, a % b
  return a

# 최소공배수 함수
def lcm(a, b):
  return a * b // gcd(a, b)

for _ in range(t):
  a, b= map(int, input().split())
  print(lcm(a,b))