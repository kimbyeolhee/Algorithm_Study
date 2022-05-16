# 2022-05-12
# 7:00-

# TODO: 다시풀기

import sys

def input():
  return sys.stdin.readline().rstrip()

# input: N(블로그 일 수), X(특정 기간) 
# output: 'X일 동안 가장 많이 들어온 방문자 수'와 '해당 기간이 몇 개인지'

# X개씩 합을 계산해서 최대값이 몇개인지 확인

### sol1. 시간초과 ###
N, X = map(int, input().split())
views = list(map(int, input().split()))

# 기간 내 최대 조회수 
sum_view_list = []
for i in range(N - X + 1):
  sum_view_list.append(sum(views[i:i + X]))

max_view = max(sum_view_list)
cnt = sum_view_list.count(max_view)
 
if max_view == 0:
  print('SAD')
else:
  print(max_view)
  print(cnt)


### sol2. ###

# 매번 합계를 구해주면 시간이 너무 오래 걸린다.
# [i ~ i+X]의 합계를 구한 다음, 다음 구간의 합계에서는 [i]를 빼주고, [i+X+1]을 더해주면 그게 [i+1 ~ i+X+1]의 합계이다.
# 이러한 방식으로 진행하면서 합계중 최댓값을 저장해두고, 최댓값이 같은 경우 최댓값의 개수도 같이 증가

N, X = map(int, input().split())
views = list(map(int, input().split()))

if max(views) == 0:
  print('SAD')
else:
  max_view = sum(views[0:X])
  value = max_view
  cnt = 1
  for i in range(X, N):
    value -= views[i-X]
    value += views[i]
    if value > max_view:
      max_view = value
      cnt = 1
    elif value == max_view:
      cnt += 1

  print(max_view)
  print(cnt)