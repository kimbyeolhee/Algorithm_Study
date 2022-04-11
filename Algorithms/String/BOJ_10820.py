# 2022-04-11
# 5:12-5:18

# 소문자, 대문자, 숫자, 공백의 개수를 세어서 출력
while True:
  try:
    string = input()
    lower, upper, number, space = 0, 0, 0, 0
    
    for s in string:
      if s.islower():
        lower += 1
      elif s.isupper():
        upper += 1
      elif s.isdigit():
        number += 1
      elif s == ' ':
        space += 1

    print(lower, upper, number, space)
  except EOFError:
    break