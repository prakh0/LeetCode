class Solution:
    def robotSim(self, commands: List[int], obstacles: List[List[int]]) -> int:
        directions = [(0,1), (1,0), (0,-1), (-1,0)]
        dir_idx = 0
        x = y = 0
        max_distance = 0
        obstacles = set(map(tuple,obstacles))

        for cmd in commands:
            if cmd == -2:
                dir_idx = (dir_idx + 3) % 4
            elif cmd == -1:
                dir_idx = (dir_idx + 1) % 4
            else:
                dx,dy = directions[dir_idx]
                for _ in range(cmd):
                    nx = x + dx
                    ny = y + dy
                    if(nx,ny) in obstacles:
                        break
                    x = nx
                    y = ny
                    max_distance = max(max_distance, x*x + y*y)
        return max_distance