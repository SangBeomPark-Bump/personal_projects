import sys
input = sys.stdin.readline
verbose = False
verboses = [False for _ in range(10)]


N, M = map(int, input().split())

arr = [list(map(int, list(input().strip('\n').replace("H", "0")))) for _ in range(N)]

from collections import deque
def bfs(y, x):
    ### 여기는 앞에와 같음
    visited = [[0] * M for _ in range(N)]
    dy = (-1, 1, 0, 0)
    dx = (0, 0, -1, 1)
    ## 초기설정
    visited[y][x] = 1
    que = deque()
    ## y, x에 넣어준다
    que.append((y, x))

    ans = -1

    while que:
        y, x = que.popleft()
        factor = arr[y][x]
        for i in range(4):
            ny = y + dy[i] * factor
            nx = x + dx[i] * factor
            if not(0 <= ny < N and 0 <= nx < M):
                continue
            if arr[ny][nx] == 0:
                continue
            if not visited[ny][nx]:
                visited[ny][nx] = visited[y][x] +1
                que.append((ny, nx))
            else:
                return ans
    for row in visited:
        for num in row:
            ans = max(num, ans)
        print(row)
    return ans
print(bfs(0,0))

# for i in arr:
#     print(i)