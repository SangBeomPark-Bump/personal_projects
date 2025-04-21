import sys
input = sys.stdin.readline
verbose = False

sys.setrecursionlimit(10000)

N, M = map(int, input().split())

arr = [list(map(int, list(input().strip('\n')))) for _ in range(N)]

from collections import deque
def bfs(y, x):
    ### 여기는 앞에와 같음
    visited = [[False] * M for _ in range(N)]
    visited_later = [[False] * M for _ in range(N)]
    dy = (-1, 1, 0, 0)
    dx = (0, 0, -1, 1)
    dist = 0
    ## 초기설정
    
    que = deque()
    ## y, x에 넣어준다
    if arr[y][x] == 1:
        que.append((y, x, True, 0))
    else:
        que.append((y, x, False, 0))
    while que:
        y, x, used, dist= que.popleft()
        dist +=1
        if y == (N-1) and x == (M-1):
            return dist
        for i in range(4):
            ny = y + dy[i]
            nx = x + dx[i]
            if not(0 <= ny < N and 0 <= nx < M):
                continue
            if not visited[ny][nx]:
                if arr[ny][nx] == 1:
                    if not used:
                        visited[ny][nx] = True
                        visited_later[ny][nx] = True
                        que.append((ny, nx, True, dist))
                    else:
                        continue
                else:
                    visited[ny][nx] = True
                    if not used:
                        visited_later[ny][nx] = True
                    que.append((ny, nx, used, dist))
            elif not visited_later[ny][nx] and not used:
                if arr[ny][nx] == 1:
                    visited[ny][nx] = True
                    que.append((ny, nx, True, dist))
                else:
                    visited[ny][nx] = True
                    visited_later[ny][nx] = True
                    if not used:
                        visited_later[ny]
                    que.append((ny, nx, used, dist))
    return -1

print(bfs(0, 0))
