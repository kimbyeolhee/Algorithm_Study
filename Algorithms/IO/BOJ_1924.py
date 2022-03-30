# 2022-03-29
# 4:45- 4:55

# 2022-03-30
# 12:00- 12:05

# 2017년 1월 1일 -> MON
# 2007년에는 1, 3, 5, 7, 8, 10, 12월은 31일까지, 
# 4, 6, 9, 11월은 30일까지, 
# 2월은 28일까지 있다.

import sys
def input():
  return sys.stdin.readline().rstrip()

m, d = map(int, input().split())

month_days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
day = ['SUN', 'MON', 'TUE', 'WED', 'THU', 'FRI', 'SAT']

days = sum(month_days[:m-1]) + d
print(day[days%7])

