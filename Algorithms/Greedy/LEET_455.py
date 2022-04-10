# 2022-4-11
# 4:10-실패

# TODO: 다시풀기

class solution:
  def findContentChildren(self, g: List[int], s: List[int]) -> int:
    answer = 0
    g.sort()
    s.sort()
    cookie_i , kid_i = 0, 0
    
    while cookie_i < len(s) and kid_i < len(g):
      if s[cookie_i] >= g[kid_i]:
        answer += 1
        kid_i += 1
      cookie_i += 1
    
    return answer