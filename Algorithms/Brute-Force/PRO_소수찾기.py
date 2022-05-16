# 2022-05-10
# 11:00-11:15

from itertools import permutations
# 입력: 종이 조각에 적힌 숫자 문자열
# 출력: 만들어지는 소수 개수

## test case: 002인 경우는 2로 판별해야함

def is_prime_number(x):
    if x == 0:
        return
    if x == 1:
        return
    else:
        for i in range(2,x):
            if x % i == 0:
                return
        return x

def solution(numbers):
    # 종이 조각에 적힌 숫자를 담은 배열
    num_list = list(numbers)

    # 종이 조각으로 만든 순열 리스트
    answer = []
    for j in range(1,len(numbers)+1):
        temps = list(permutations(num_list, j))
        for temp in temps:
            number = ""
            for v in temp:
                number += v
            if(number):
                answer.append(int(number))
    
    # 중복 제거
    answer = list(set(answer))
    # 소수 판별
    return len([i for i in answer if is_prime_number(i) != None])