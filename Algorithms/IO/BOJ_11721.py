# 2022-03-29
# 3:53 -3:57

# TODO: 한번 더 풀어보기

import sys

def input():
  return sys.stdin.readline().rstrip()

# 입력 문자열
s = input()

## 10개씩 끊어서 출력
for i in range(0, len(s)//10 + 1):
  print(s[i*10:(i+1)*10])

## pythonic 한 방법
for i in range(0, len(s), 10):
  print(s[i:i+10])