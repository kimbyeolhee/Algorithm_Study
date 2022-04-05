# 2022-04-05
# 12:06-12:09

import sys
def input():
  return sys.stdin.readline().rstrip()

# 학생 수 입력
N = int(input())
# 이름 국어점수 영어점수 수학점수 입력
student_list = []
for _ in range(N):
  name, kor, eng, math = input().split()
  student_list.append((name, int(kor), int(eng), int(math)))

# 국어 점수가 감소하는 순서로
# 국어 점수가 같으면 영어 점수가 증가하는 순서로
# 국어 점수와 영어 점수가 같으면 수학 점수가 감소하는 순서로
# 모든 점수가 같으면 이름이 사전 순으로 증가하는 순서로 (단, 아스키 코드에서 대문자는 소문자보다 작으므로 사전순으로 앞에 온다.)
student_list.sort(key=lambda x: (-x[1], x[2], -x[3], x[0]))

for s in student_list:
  print(s[0])