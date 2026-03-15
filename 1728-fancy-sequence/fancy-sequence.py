class Fancy:

    def __init__(self):
        self.seq = []
        self.mul = 1
        self.add = 0
        self.mod = 10**9 + 7

    def append(self, val: int) -> None:
        stored = (val - self.add) % self.mod
        mulInv = pow(self.mul, self.mod - 2, self.mod)
        stored = (stored * mulInv) % self.mod
        self.seq.append(stored)

    def addAll(self, inc: int) -> None:
        self.add = (self.add + inc) % self.mod 
        
    def multAll(self, m: int) -> None:
        self.add = (self.add * m) % self.mod
        self.mul = (self.mul * m) % self.mod

    def getIndex(self, idx: int) -> int:
        if len(self.seq) <= idx:
            return -1
        return (self.seq[idx] * self.mul + self.add) % self.mod
# Your Fancy object will be instantiated and called as such:
# obj = Fancy()
# obj.append(val)
# obj.addAll(inc)
# obj.multAll(m)
# param_4 = obj.getIndex(idx)