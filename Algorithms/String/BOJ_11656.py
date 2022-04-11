# 2022-04-11
# 6:05-6:08

import sys
def input():
  return sys.stdin.readline().rstrip()

# 문자열 입력
string = input()

# 접미사 배열
suffix = [string[i:] for i in range(len(string))]
suffix.sort()

for s in suffix:
  print(s)