# 2022-04-04
# 5:24-실패

# 2022-04-04
# 10:30-10:34

import sys
def input():
  return sys.stdin.readline().rstrip()


# sol1
board = input() 
result = []
i = 0

while i < len(board):
  if board[i:i+4] == 'XXXX':
    result.append('AAAA')
    i += 4
  elif board[i:i+2] == 'XX':
    result.append('BB')
    i += 2
  elif board[i] == '.':
    result.append('.')
    i += 1
  else:
    break

result = ''.join(result)
if len(board) == len(result):
  print(result)
else:
  print(-1)


# sol2
# board = input() 
# board = board.replace("XXXX", "AAAA") 
# board = board.replace("XX", "BB") 

# if 'X' in board: 
#   print(-1) 
# else: 
#   print(board)

