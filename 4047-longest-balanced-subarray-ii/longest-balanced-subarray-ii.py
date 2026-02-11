class SegmentTree():
    def __init__(self, n):
        self.n = n
        self.min_tree = [0 for _ in range(4*self.n)]
        self.max_tree = [0 for _ in range(4*self.n)]
        self.lazy = [0 for _ in range(4*self.n)]

    def _push(self, node, left, right):
        if self.lazy[node] != 0:
            self.min_tree[node] += self.lazy[node]
            self.max_tree[node] += self.lazy[node]
            if left != right:
                self.lazy[node<<1] += self.lazy[node]
                self.lazy[node<<1|1] += self.lazy[node]

            self.lazy[node] = 0

    def range_update(self, l, r, val):
        return self._range_update(1, 1, self.n, l, r, val)
    
    def _range_update(self, node, left, right, l, r, val):
        self._push(node, left, right)

        if l > right or r < left: return 

        if l <= left and right <= r:
            self.lazy[node] += val
            self._push(node, left, right)
            return 
        
        mid = left + (right - left)//2
        self._range_update(node<<1, left, mid, l, r, val)
        self._range_update(node<<1|1, mid+1, right, l, r, val)

        self.min_tree[node] = min(
            self.min_tree[node<<1],
            self.min_tree[node<<1|1]
        )
        self.max_tree[node] = max(
            self.max_tree[node<<1],
            self.max_tree[node<<1|1]
        )

    def query_first_zero(self, idx):
        return self._query_first_zero(1, 1, self.n, idx)
    
    def _query_first_zero(self, node, left, right, r):
        self._push(node, left, right)

        if self.min_tree[node] > 0 or self.max_tree[node] < 0:
            return -1
        if left == right:
            if self.min_tree[node] == 0 : return left
            else: return -1

        mid = left + (right - left)//2
        left_res = self._query_first_zero(node<<1, left, mid, r)
        if left_res != -1:
            return left_res

        right_res = self._query_first_zero(node<<1|1, mid+1, right, r)
        return right_res 

class Solution:
    def longestBalanced(self, nums: List[int]) -> int:
        n = len(nums)
        sg = SegmentTree(n)

        last_occurance = {}
        res = 0
        for r, e in enumerate(nums):
            l = last_occurance.get(e, -1) + 1
            last_occurance[e] = r
            if e%2 == 0:
                sg.range_update(l+1, r+1, 1)
            else:
                sg.range_update(l+1, r+1, -1)

            
            first_zero = sg.query_first_zero(r+1)
            if first_zero == -1: continue

            res = max(res, r - first_zero +2)
        return res