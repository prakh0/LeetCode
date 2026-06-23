def magneticForce(position,m,mid):
  count = 1
  last_position = position[0]
  for i in position[1:]:
    if i - last_position >= mid:
      count += 1
      last_position = i
    if count >= m:
      return True
  return False
class Solution:
    def maxDistance(self, position: List[int], m: int) -> int:
      position.sort()
      start,end = 0 , position[-1] -position[0]
      result = 0
      while start <= end:
        mid = (start + end)//2
        if magneticForce(position,m,mid):
          result = mid
          start = mid + 1
        else:
          end = mid - 1
      return result
    