# 2022-04-06
# 10:47-실패

# TODO: 다시풀기

def solution(n, lost, reserve):
    lost.sort()
    reserve.sort()
    
    # 여벌 체육복을 가져온 학생이 도난 당한 경우 lost와 reserve에서 제거
    for i in lost[:]:
        if i in reserve[:]:
            lost.remove(i)
            reserve.remove(i)
    avail = n - len(lost) # 원래 체육이 가능한 학생 수

    for i in lost:
        if (i-1) in reserve:
            reserve.remove(i-1)
            avail+=1
        elif (i-1) not in reserve and (i+1) in reserve:
            reserve.remove(i+1)
            avail+=1

    return avail