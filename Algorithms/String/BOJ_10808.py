# 2022-04-11
# 4:52- 4:56

# sol.1
import sys
def input():
  return sys.stdin.readline().rstrip()

alphabet = 'abcdefghijklmnopqrstuvwxyz'
alpha_dict = {alphabet[i]:0 for i in range(len(alphabet))}

# 입력 문자열
string = input()

for s in string:
  if s in alpha_dict:
    alpha_dict[s] += 1

for value in alpha_dict.values():
  print(value, end=' ')


### sol.2
string=input() 
cnt=[0]*26 

# a의 아스키 코드는 97이므로 이를 기준으로 cnt의 인덱스 0을 a, 1을 b, 2를 c  ... z를 25로 처리
for i in string: 
  cnt[ord(i)-97] += 1 

print(*cnt)
