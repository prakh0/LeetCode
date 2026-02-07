class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        result = []
        curr = []
        first = 1

        while True:
            if len(curr) == k:
                result.append(curr.copy())
                first = curr.pop() + 1
            elif first > n:
                if not curr:
                    break
                first = curr.pop() + 1
            else:
                curr.append(first)
                first += 1
        return result