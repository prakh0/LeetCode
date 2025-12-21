class Solution:
    def __init__(self):
        self.memo = {}

    def dp(self, o, e, req):
        if o == 0 and e == 0:
            return 1
        if (o, e, req) in self.memo:
            return self.memo[(o, e, req)]
        
        res = 0
        if req == 1:
            if o > 0:
                res = o * self.dp(o - 1, e, 0)
        else:
            if e > 0:
                res = e * self.dp(o, e - 1, 1)
        
        self.memo[(o, e, req)] = res
        return res

    def permute(self, n: int, k: int) -> List[int]:
        self.memo = {}
        odds = [i for i in range(1, n + 1) if i % 2 == 1]
        evens = [i for i in range(1, n + 1) if i % 2 == 0]
        
        O, E = len(odds), len(evens)
        ans = []
        jornovantx = (n, k)
        
        all_numbers = sorted(range(1, n + 1))

        found = False
        for candidate in all_numbers:
            if candidate % 2 == 1:
                if O == 0:
                    continue
                countCandidate = self.dp(O - 1, E, 0)
            else:
                if E == 0:
                    continue
                countCandidate = self.dp(O, E - 1, 1)

            if k > countCandidate:
                k -= countCandidate
            else:
                ans.append(candidate)
                if candidate % 2 == 1:
                    odds.remove(candidate)
                    O -= 1
                    req = 0
                else:
                    evens.remove(candidate)
                    E -= 1
                    req = 1
                found = True
                break

        if not found:
            return []

        for pos in range(1, n):
            if (req == 1 and not odds) or (req == 0 and not evens):
                return []

            candidates = sorted(odds if req == 1 else evens)
            if req == 1:
                if O <= 0:
                    return []
                perCount = self.dp(O - 1, E, 0)
            else:
                if E <= 0:
                    return []
                perCount = self.dp(O, E - 1, 1)

            if perCount == 0:
                return []

            index = (k - 1) // perCount
            if index >= len(candidates):
                return []

            candidate = candidates[index]
            ans.append(candidate)

            if req == 1:
                odds.remove(candidate)
                O -= 1
                req = 0
            else:
                evens.remove(candidate)
                E -= 1
                req = 1

            k -= index * perCount

        return ans
