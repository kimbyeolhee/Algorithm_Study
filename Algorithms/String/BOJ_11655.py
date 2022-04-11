# 2022-04-11
# 5:44-실패

# TODO: 다시풀기

import sys
def input():
  return sys.stdin.readline().rstrip()

string = [s for s in input()]
for i in range(len(string)):
  # 대문자
  if string[i].isupper():
    if ord(string[i])+13 <= ord('Z'):
      string[i] = chr(ord(string[i])+13)
    else:
      string[i] = chr(ord(string[i])-13)
  
  # 소문자
  elif string[i].islower():
    if ord(string[i])+13 <= ord('z'):
      string[i] = chr(ord(string[i])+13)
    else:
      string[i] = chr(ord(string[i])-13)

for s in string:
  print(s, end='')

