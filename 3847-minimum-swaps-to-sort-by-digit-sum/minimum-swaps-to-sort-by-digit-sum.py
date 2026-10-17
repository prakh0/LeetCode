class Solution:
    def minSwaps(self, nums: List[int]) -> int:
        result = []
        swap = 0
        for i,num in enumerate(nums):
            digit_sum = 0
            for digit in str(num):
                digit_sum += int(digit)
            result.append((digit_sum,num,i))
        result.sort()
        
        swap = 0
        visited = [False] * len(nums)
        for i in range(len(nums)):
            if visited[i] or result[i][2] == i:
                continue
            cycle = 0
            j = i 
            while not visited[j]:
                visited[j] = True
                j = result[j][2]
                cycle += 1
            swap += cycle - 1
        return swap