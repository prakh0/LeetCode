class Solution:
    def maxIceCream(self, costs: List[int], coins: int) -> int:
        mcost = max(costs)
        freq = [0] * (mcost + 1) 
        for cost in costs:
            freq[cost] += 1
        count = 0
        for cost in range(1,mcost + 1):
            if freq[cost] == 0:
                continue
            if coins < cost:
                break
            can_buy = min(freq[cost], coins // cost)
            
            count += can_buy
            coins -= can_buy * cost
        return count