class Solution:
    def totalMoney(self, n: int) -> int:
        money = 1
        result = 0
        while n > 0:
            days = min(n,7)
            for i in range(days):
                result += money + i
            n = n - days 
            money+= 1
        return result