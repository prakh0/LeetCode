class Solution:
    def findKthBit(self, n: int, k: int) -> str:
        def helper(n, k):
            if n == 1:
                return '0'
            mid = (1 << (n - 1))
            if k == mid:
                return '1'
            elif k < mid:
                return helper(n - 1, k)
            else:
                corresponding_pos = mid - (k - mid)
                return '1' if helper(n - 1, corresponding_pos) == '0' else '0'
        return helper(n, k)
  