# 2022-04-13
# 11:28-실패

# TODO: 다시풀기

import sys

def input():
  return sys.stdin.readline().rstrip()

a, b = map(int, input().split())

# 최대공약수
def gcd(a, b):
  while b > 0:
    a, b = b, a%b
  return a

print(gcd(a,b))

# 최소공배수
def lcm(a, b):
  return a*b//gcd(a,b)

print(lcm(a,b))