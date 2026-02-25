class Solution:
    def countBits(num):
        count = 0
        while num > 0:
            count += 1
            num = num & (num-1)
        return count
    def sortByBits(self, arr: List[int]) -> List[int]:
        arr.sort(key = lambda num: (Solution.countBits(num), num))
        return arr