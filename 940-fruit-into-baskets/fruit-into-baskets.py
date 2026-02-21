class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        freq = {}
        left = 0
        result = 0
        for right in range(len(fruits)):
            fruit = fruits[right]
            if fruit in freq:
                freq[fruit] += 1
            else:
                freq[fruit] = 1
            while len(freq) > 2:
                left_fruit = fruits[left]
                freq[left_fruit] -= 1
                if freq[left_fruit] == 0:
                    freq.pop(left_fruit)
                left += 1
            total_fruits = right - left + 1
            result = max(result,total_fruits)
        return result