# 2022-04-11
# 3:40-실패

# TODO: 다시풀기

import sys
sys.setrecursionlimit(10**9)
def input():
  return sys.stdin.readline().rstrip()


def get_preorder(in_start, in_end, post_start, post_end):
  # 재귀 종료 조건
  if (in_start > in_end) or (post_start > post_end):
    return
  
  # 후위 순회의 마지막 노드가 서브트리의 루트
  root = postorder[post_end]
  print(root, end=' ')

  # 중위 순회에서 루트 값의 노드가 좌/우 서브트리 구분점
  left = position[root] - in_start
  right = in_end - position[root]

  # 분할 정복
  get_preorder(in_start, in_start+left-1, post_start, post_start+left-1)
  get_preorder(in_end-right+1, in_end, post_end-right, post_end-1)


# 노드의 개수 입력
n = int(input())
inorder = list(map(int, input().split()))
postorder = list(map(int, input().split()))

# 후위 순회의 마지막 노드 값이 중위 순회의 어디에 있는지 확인하기 위해 중위 순회 값들의 인덱스를 저장 
position =[0]*(n+1)
for i in range(n):
  position[inorder[i]] = i

# 1부터 n까지의 번호의 노드로 이루어져있으므로 n-1
get_preorder(0, n-1, 0, n-1)