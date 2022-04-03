# 2022-04-03
# 10:50-실패

# TODO: 다시풀기

import sys
def input():
  return sys.stdin.readline().rstrip()

class Node:
  def __init__(self, item, prev, next):
    self.item = item
    self.prev = prev
    self.next = next

class LinkedList():
  def __init__(self):
    self.head = Node(None, None, None)
    self.tail = Node(None, self.head, None)
    self.head.next = self.tail
    self.cur_node = self.tail

  def insert(self, t_node, item):
    p_node = t_node.prev
    new_node = Node(item, p_node, t_node)
    t_node.prev = new_node
    p_node.next = new_node

  def delete(self, t_node):
    f_node = t_node.prev
    r_node = t_node.next
    f_node.next = r_node
    r_node.prev = f_node

  def print(self):
    cur_node = self.head.next
    while cur_node != self.tail:
      if cur_node.next != self.tail:
        print(cur_node.item, end="")
      else:
        print(cur_node.item)
      cur_node = cur_node.next


if __name__ == "__main__":
  command = list(input())
  memos = LinkedList()
  for i in range(len(command)):
    memos.insert(memos.tail, command[i])
  
  for i in range(int(input())):
    order = input()
    if order[0] == "L":
      if memos.cur_node.prev.prev != None:
        memos.cur_node = memos.cur_node.prev
    elif order[0] == "D":
      if memos.cur_node.next != None:
        memos.cur_node = memos.cur_node.next
    elif order[0] == "B":
      if memos.cur_node.prev.prev != None:
        memos.delete(memos.cur_node.prev)
    else:
      memos.insert(memos.cur_node, order[2])

memos.print()
