class Solution:
    def validateCoupons(self, code: List[str], businessLine: List[str], isActive: List[bool]) -> List[str]:
        result = []
        for i in range(len(code)):
            if not isActive[i]:
                continue
            if businessLine[i] not in {"electronics", "grocery", "pharmacy", "restaurant"}:
                continue
            if len(code[i]) == 0:
                continue
            is_valid = True
            for j in code[i]:
                if not j.isalnum() and j != "_":
                    is_valid = False
                    break
            if not is_valid:
                continue
            result.append(i)
        order = {
            "electronics": 0,
            "grocery": 1,
            "pharmacy": 2,
            "restaurant": 3
        }
        result.sort(key = lambda x : (order[businessLine[x]],code[x]))
        return [code[i] for i in result]