class Solution:
    def countCoveredBuildings(self, n: int, buildings: List[List[int]]) -> int:
        dict_x = defaultdict(list)
        dict_y = defaultdict(list)

        for x, y in buildings:
            dict_x[x].append(y)
            dict_y[y].append(x)
        for x in dict_x:
            dict_x[x].sort()
        for y in dict_y:
            dict_y[y].sort()
        res = 0
        for x, y in buildings:
            ox = dict_x[x]
            oy = dict_y[y]
            if oy[0] < x < oy[-1] and ox[0] < y < ox[-1]:
                res += 1
        return res