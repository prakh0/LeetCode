class Solution:
    def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:
        result, left , currSum = 0, 0,0
        for right in range(len(arr)):
            currSum += arr[right]
            if right - left + 1 < k:
                continue
            if currSum / k >= threshold:
                result += 1
            currSum -= arr[left]
            left += 1 
        return result