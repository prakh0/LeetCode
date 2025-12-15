class Solution:
    def getDescentPeriods(self, prices: List[int]) -> int:
        result = 1
        period = 1
        for i in range(1,len(prices)):
            if prices[i] == prices[i - 1] - 1:
                period += 1
            else:
                period = 1
            result +=  period
        return result