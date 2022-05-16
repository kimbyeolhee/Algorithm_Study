# 2022-05-11
# 10:00 - 

# TODO: 다시 풀기

# input: brown: 갈색 격자의 수 / yellow: 노랑 격자의 수
# output: 카펫의 가로,세로 크기

# 테두리 1줄은 갈색, 중앙은 노랑
# 카펫의 가로 길이 >= 세로 길이

def solution(brown, yellow):
    # 전체 격자 개수 = brown + yellow = 가로(a)X세로(b)
    total = brown + yellow
    
    # 1. 가로(a)X세로(b) = total을 만족하는 가로,세로 값
    for a in range(1,total+1):
        if total % a == 0:
            b = total / a
            if a >= b:  # 2. 가로길이>=세로길이
                if 2*a + 2*b - 4 == brown:  # 3. brown 갯수는 테두리 격자의 개수
                    return [a,b]