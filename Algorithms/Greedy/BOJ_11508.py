# 2022-04-04
# 4:21-4:33

import sys
def input():
  return sys.stdin.readline().rstrip()

# N: 유제품 개수
N = int(input())

price_list = []
final_list = []
for _ in range(N):
  price_list.append(int(input()))

price_list = sorted(price_list, reverse=True)

for i in range(0, len(price_list), 3):
  final_list += price_list[i:i+3][:2]

print(sum(final_list))