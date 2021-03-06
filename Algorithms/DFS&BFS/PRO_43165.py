# 2022-05-18
# 12:00-

# TODO: 다시풀기


def solution(numbers, target):
  cnt = 0

  def dfs(idx, result):
    """
    Args:
        idx: 계산 횟수
        result: 계산값
    Return:
        계산 횟수가 numbers의 길이와 일치할 경우 계산결과값이 target값과 같은 경우 cnt에 1을 더하고 아무것도 return 하지 않는다.
        numbers의 모든 숫자를 아직 사용하지 않을 경우 조건을 만족시킬때 까지 재귀함수 반복
    """
    if idx == len(numbers):
      if result == target:
        nonlocal cnt
        cnt += 1
      return
    else:
      dfs(idx+1, result + numbers[idx])
      dfs(idx+1, result - numbers[idx])
  dfs(0, 0)
  return cnt
