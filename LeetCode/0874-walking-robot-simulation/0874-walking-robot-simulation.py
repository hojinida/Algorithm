class Solution:
    def robotSim(self, commands: List[int], obstacles: List[List[int]]) -> int:
        direction = [[0, 1], [1, 0], [0, -1], [-1, 0]]
        obstacles = set(map(tuple, obstacles))

        point = 0
        x,y = 0,0
        answer = 0
        for command in commands:
            if command == -2:
                point = (point-1)%4
            elif command == -1:
                point = (point+1)%4
            else:
                for _ in range(command):
                    next_x = x + direction[point][0]
                    next_y = y + direction[point][1]
                    if (next_x, next_y) in obstacles:
                        break  
                    x = next_x
                    y = next_y
                    answer = max(answer,x**2+y**2)
      
        return answer
                    