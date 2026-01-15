class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        carry = 1
        for i in range(len(digits)-1,-1,-1):
            current_digits = digits[i] + carry
            digits[i] = current_digits % 10
            carry = current_digits // 10
        if carry > 0:
            return [1] + digits
        return digits       