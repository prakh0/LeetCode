class Solution:
    def totalNumbers(self, digits: List[int]) -> int:
        unique_number = set()
        for i in range(len(digits)):
            for j in range(len(digits)):
                for k in range(len(digits)):
                    if i == j or j == k or k == i:
                        continue
                    if digits[i] == 0:
                        continue
                    if digits[k] % 2 != 0:
                        continue
                    number = digits[i]*100 +digits[j]*10 +digits[k]
                    unique_number.add(number)
        return len(unique_number) 