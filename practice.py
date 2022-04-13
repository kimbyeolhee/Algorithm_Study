import sys

def input():
  return sys.stdin.readline().rstrip()

# 원형 연결리스트 구조 정의
class Node:
  def __init__(self, data):
    self.data = data
    self.next = None

class CircularLinkedList:
  def __init__(self):
    self.head = Node('head')
    self.head.next = self.head
    self.cur_node = self.head
  
  def insert(self, prev_data, new):
    new_node = Node(new)
    cur_node = self.find(prev_data)
    new_node.next = cur_node.next
    cur_node.next = new_node

  def find(self, elem):
    cur_node = self.head
    while cur_node.data != elem:
      cur_node = cur_node.next
    return cur_node

  def find_prev(self, elem):
    cur_node = self.head
    while cur_node.next.data != elem:
      cur_node = cur_node.next
    return cur_node

  def remove(self, gap):
    cnt = 0
    while cnt < gap:
      self.cur_node = self.cur_node.next
      if self.cur_node.data != 'head':
        cnt += 1
    
    prev_node = self.find_prev(self.cur_node.data)
    prev_node.next = prev_node.next.next
    return str(self.cur_node.data)

# 입력
#  N명의 사람이 원을 이루면서 앉아있고, K번째 사람을 제거
n, k = map(int, input().split())

# 원형 연결 리스트 생성
people_list = CircularLinkedList()
people_list.insert('head', 1)
for i in range(2, n+1):
  people_list.insert(i-1, i)

print("<", end="")
for i in range(n-1):
  print(people_list.remove(k), end=", ")
print(people_list.remove(k), end=">")


