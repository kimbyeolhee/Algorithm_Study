# 2022-04-03
# 10:50-실패

# 2022-04-04
# 3:43-실패

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

  def remove(self, t_node):
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
  string = list(input())
  editor = LinkedList()
  for s in string:
    editor.insert(editor.tail, s)
  
  for _ in range(int(input())):
    command = list(input().split())
    if command[0] == "L":
      if editor.cur_node.prev.prev != None:
        editor.cur_node = editor.cur_node.prev
    elif command[0] == "D":
      if editor.cur_node.next != None:
        editor.cur_node = editor.cur_node.next
    elif command[0] == "B":
      if editor.cur_node.prev.prev != None:
        editor.remove(editor.cur_node.prev)
    else:
      editor.insert(editor.cur_node, command[1])

editor.print()
