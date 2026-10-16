class Solution:
    def maxSumOfSquares(self, num: int, sum: int) -> str:
        if sum > num * 9:
            return ""
        max_num = ""
        for i in range(num):
            digit = min(sum,9)
            max_num += str(digit)
            sum -= digit
        return max_num