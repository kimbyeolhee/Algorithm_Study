# 2022-04-10
# 11:34 - 실패

# TODO: 다시풀기

import sys
def input():
  return sys.stdin.readline().rstrip()

def get_postorder(preorder, inorder):
  if not inorder:
    return 
  root = preorder.pop(0)
  idx = inorder.index(root)

  get_postorder(preorder, inorder[:idx]) # 왼쪽 서브트리
  get_postorder(preorder, inorder[idx+1:]) # 오른쪽 서브트리
  print(root, end=' ')

# 테스트 케이스 개수 입력
t = int(input())
for _ in range(t):
  # 노드의 개수
  n = int(input())
  preorder = list(map(int, input().split()))
  inorder = list(map(int, input().split()))
  get_postorder(preorder, inorder)
  print("")



