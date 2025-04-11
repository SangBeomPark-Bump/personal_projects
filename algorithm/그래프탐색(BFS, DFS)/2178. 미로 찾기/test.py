import sys
input = sys.stdin.readline
verbose = False

N, M = map(int, input().split())


arr =  [list(map(int,list(input().strip('\n')))) for _ in range(N) ]


from collections import deque
def maze_bfs(y, x, depth):
    ### 여기는 앞에와 같음
    visited = [[False] * M for _ in range(N)]
    dy = (-1, 1, 0, 0)
    dx = (0, 0, -1, 1)
    ## 초기설정
    visited[y][x] = True
    que = deque()
    ## y, x에 넣어준다
    que.append((y, x, depth))

    while que:
        y, x, depth = que.popleft()
        if verbose:
            print(y, x, depth)
        if y == N-1 and x == M-1:
            return depth
        for i in range(4):
            ny = y + dy[i]
            nx = x + dx[i]
            if not(0 <= ny < N and 0 <= nx < M):
                continue
            if arr[ny][nx] == 0:
                continue
            if not visited[ny][nx]:
                visited[ny][nx] = True
                que.append((ny, nx, depth +1))


print(maze_bfs(0, 0, 1))