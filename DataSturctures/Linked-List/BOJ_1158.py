# 2022-03-31
# 2:00 - 실패

# 2022-04-03
# 8:00 - 실패
# TODO 다시풀기

# 원형 연결리스트 

class Node:
  def __init__(self, element):
    self.element = element
    self.next = None

class CircularLinkedList:
  def __init__(self):
    self.head = Node('head')
    self.head.next = self.head
    self.cur_node = self.head

  def insert(self, item, new):
    new_node = Node(new)
    cur_node = self.find(item)
    new_node.next = cur_node.next
    cur_node.next = new_node

  def find(self, item):
    cur_node = self.head
    while cur_node.element != item:
      cur_node = cur_node.next
    return cur_node

  def find_previous(self, item):
    cur_node = self.head
    while cur_node.next.element != item:
      cur_node = cur_node.next
    return cur_node

  def print(self):
    cur_node = self.head
    while cur_node.next.element != 'head':
      print(cur_node.element, end=' -> ')
      cur_node = cur_node.next
    print(cur_node.element)

  def remove(self, gap):
    cnt = 0
    while cnt < gap:
      self.cur_node = self.cur_node.next
      if self.cur_node.element != 'head':
        cnt += 1
    prev_node = self.find_previous(self.cur_node.element)
    prev_node.next = prev_node.next.next
    return str(self.cur_node.element)

if __name__ == '__main__':
  N, K = map(int, input().split())

  people_list = CircularLinkedList()
  people_list.insert('head', 1)
  for i in range(2, N+1):
    people_list.insert(i-1, i)

  print("<", end='')
  for i in range(N -1):
    print(people_list.remove(K), end=', ')
  print(people_list.remove(K), end='>')