# 2022-04-04
# 10:50- 10:54

import sys
def input():
  return sys.stdin.readline().rstrip()

# 회원 수 입력
N = int(input())
# 각 회원의 나이와 이름이 공백으로 구분되어 주어짐
people_list = []
for idx in range(N):
  age, name = input().split()
  people_list.append((idx, int(age), name))

people_list.sort(key=lambda x : (x[1], x[0]))

for p in people_list:
  print(f'{p[1]} {p[2]}')