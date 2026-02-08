import heapq
from typing import List

class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        def distance(x, y):
            return x**2 + y**2
        
        minheap = []
        result = []
        
        for x, y in points:
            dist = distance(x, y)
            minheap.append([dist, x, y])
        
        heapq.heapify(minheap)
        
        for d in range(k):
            result.append(heapq.heappop(minheap)[1:])
        
        return result