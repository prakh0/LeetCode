class DSU:
    def __init__(self, n: int):
        self.parent = list(range(n))
        self.rank = [0]*n

    def find(self, x: int) -> int:
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def union(self, u: int, v: int) -> bool:
        pu, pv = self.find(u), self.find(v)
        if pu == pv:
            return False
        
        if self.rank[pu] > self.rank[pv]:
            self.parent[pv] = pu
        elif self.rank[pv] > self.rank[pu]:
            self.parent[pu] = pv
        else:
            self.parent[pv] = pu
            self.rank[pu] += 1
        
        return True


class Solution:
    def maxStability(self, n: int, edges: List[List[int]], k: int) -> int:

        def can(x):
            dsu = DSU(n)
            used = 0
            upgrades = 0

            free_edges = []
            upgrade_edges = []

            for u, v, s, must in edges:
                if must == 1:
                    if s < x:
                        return False
                    if not dsu.union(u, v):
                        return False
                    used += 1
                else:
                    if s >= x:
                        free_edges.append((u, v))
                    elif 2*s >= x:
                        upgrade_edges.append((u, v))

            for u, v in free_edges:
                if used == n - 1:
                    break
                if dsu.union(u, v):
                    used += 1

            for u, v in upgrade_edges:
                if used == n - 1:
                    break
                if dsu.union(u, v):
                    upgrades += 1
                    used += 1
                    if upgrades > k:
                        return False

            return used == n - 1

        lo, hi = 0, max(s*2 for _,_,s,_ in edges)
        ans = -1

        while lo <= hi:
            mid = (lo + hi)//2
            if can(mid):
                ans = mid
                lo = mid + 1
            else:
                hi = mid - 1

        return ans