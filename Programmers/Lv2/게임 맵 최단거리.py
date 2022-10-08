from collections import deque
dr = [1, -1, 0, 0]
dc = [0, 0, 1, -1]
    
def solution(maps):
    n, m = len(maps), len(maps[0])
    queue = deque([(0, 0)])

    while queue:
        r, c = queue.popleft()
        for i in range(4):
            nr = r + dr[i]
            nc = c + dc[i]
            if 0 <= nr < n and 0 <= nc < m and maps[nr][nc] == 1: 
                maps[nr][nc] = maps[r][c] + 1
                queue.append((nr, nc))
    
    return maps[-1][-1] if maps[-1][-1] > 1 else -1