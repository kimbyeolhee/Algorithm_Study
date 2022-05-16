# 2022-04-15
# 7:20-7:33

import sys
def input():
  return sys.stdin.readline().rstrip()

def gcd(a, b):
  if b == 0:
    return a
  return gcd(b, a % b)

# 테스트 케이스 개수 t
t = int(input())

# 테스트 케이스 개수 n과 n개의 수가 주어짐
for _ in range(t):
  gcd_list = []
  temp = list(map(int, input().split()))
  n = temp[0]
  nums = temp[1:]

  for i in range(n):
    for j in range(i+1, n):
      gcd_list.append(gcd(nums[i], nums[j]))

  print(gcd_list)
