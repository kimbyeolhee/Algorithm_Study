# 2022-04-15
# 7:20-실패

# TODO: 다시풀기

# N: 10진법 수 , B: B진법
import sys
def input():
  return sys.stdin.readline().rstrip()

notation = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"
N, B = map(int, input().split())
answer = ''

while N != 0:
  answer += str(notation[N % B])
  N //= B

print(answer[::-1])