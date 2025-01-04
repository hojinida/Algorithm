from collections import deque

class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        # 이동 패턴: 오른쪽, 아래, 위, 왼쪽
        directions = [(0, 1), (1, 0), (-1, 0), (0, -1)]
        rows = len(grid)
        cols = len(grid[0])
        visited = set()

        # 첫 번째 육지를 찾기 위한 플래그
        found = False

        # 큐 초기화
        q = deque()

        # 첫 번째 육지를 찾아 큐에 추가
        for i in range(rows):
            if found:
                break
            for j in range(cols):
                if grid[i][j] == 1:
                    visited.add((i, j))
                    q.append((i, j))
                    found = True
                    break

        perimeter = 0

        # BFS를 통해 주변을 탐색
        while q:
            x, y = q.popleft()
            for dx, dy in directions:
                nx, ny = x + dx, y + dy
                # 다음 좌표가 그리드 내부에 있고 방문하지 않았으며 육지인 경우
                if 0 <= nx < rows and 0 <= ny < cols:
                    if grid[nx][ny] == 1 and (nx, ny) not in visited:
                        visited.add((nx, ny))
                        q.append((nx, ny))
                    elif grid[nx][ny] == 0:
                        perimeter += 1
                else:
                    perimeter += 1

        return perimeter
