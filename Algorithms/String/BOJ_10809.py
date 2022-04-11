# 2022-04-11
# 5:02-5:10

import sys
def input():
  return sys.stdin.readline().rstrip()

# 각각의 알파벳에 대해서, 단어에 포함되어 있는 경우에는 '처음 등장'하는 위치를, 포함되어 있지 않은 경우에는 -1을 출력

# 입력 문자열
string = input()

# alphabet 딕셔너리 초기값 : -1
alphabet = "abcdefghijklmnopqrstuvwxyz"
alpha_dict = {alphabet[i]:-1 for i in range(len(alphabet))}

for s in string:
  if alpha_dict[s] == -1:
    alpha_dict[s] = string.index(s)

print(*alpha_dict.values())
