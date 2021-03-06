# 2022-05-23
# 3:00-

# TODO 다시풀기

from collections import deque
# 한 단어만 변환가능
# target이 words 리스트 안에 있어야 함
# 모든 경로를 탐색하고 그 중 최소 횟수를 반환해야하므로 BFS

def solution(begin, target, words):
    if target not in words:
        return 0
    
    queue = deque()
    queue.append([begin, 0]) # [단어, 단계횟수]
    
    while queue:
        temp, cnt = queue.popleft()
        
        if temp == target:
            return cnt
        
        for i in range(len(words)):
            diff = 0
            word = words[i]
            for j in range(len(temp)):
                if temp[j] != word[j]:
                    diff += 1
            if diff == 1:
                queue.append([word, cnt+1])
    return 0