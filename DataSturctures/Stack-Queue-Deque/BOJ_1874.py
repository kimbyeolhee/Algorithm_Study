# 2022-04-12
# 2:32-실패

# TODO: 다시풀기

# 첫 줄에 n (1 ≤ n ≤ 100,000)이 주어진다. 
# 둘째 줄부터 n개의 줄에는 수열을 이루는 1이상 n이하의 정수가 하나씩 순서대로 주어진다.

import sys
def input():
  return sys.stdin.readline().rstrip()

N = int(input())
stack = []
answer = []
flag = 0
cur = 1

for i in range(N):
  num = int(input())
  while cur <= num:
    # 원하는 수를 pop하기 위해 push 
    stack.append(cur)
    answer.append('+')
    cur += 1
  
  if stack[-1] == num:
    stack.pop()
    answer.append('-')
  else: # stack의 TOP이 num이 아니라면 원하는 수열을 만들 수 없다.
    print("NO")
    flag = 1
    break

if flag == 0:
  for i in answer:
    print(i) 
