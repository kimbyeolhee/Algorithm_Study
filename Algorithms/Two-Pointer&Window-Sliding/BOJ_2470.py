# 2022-05-17
# 10:01- 

# TODO: 다시풀기

import sys
def input():
  return sys.stdin.readline().rstrip()

# 전체 용액의 수 N
N = int(input())
# 용액 입력
liquids = list(map(int, input().split()))

# 투포인터로 해결하기 위해 정렬
liquids.sort()
left, right = 0, N-1

ans = liquids[left] + liquids[right]
ans_l, ans_r = left, right

while left < right:
  temp = liquids[left] + liquids[right]
  if abs(temp) < abs(ans):
    ans = temp
    ans_l, ans_r = left, right

  # 정렬을 했기 때문에 두 값을 더했는데 0보다 작은 경우 left idx += 1
  if temp < 0:
    left += 1
  # 두 값을 더했는데 0이거나 0보다 큰 경우 right idx -= 1
  else:
    right -= 1

print(liquids[ans_l], liquids[ans_r])
