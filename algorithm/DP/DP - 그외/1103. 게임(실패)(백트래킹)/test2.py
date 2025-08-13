import sys
input = sys.stdin.readline
verbose = False
verboses = [False for _ in range(10)]
sys.setrecursionlimit(10000)


N, M = map(int, input().split())

arr = [list(map(int, list(input().strip('\n').replace("H", "0")))) for _ in range(N)]

### 방문 했는지 안했는지 알려줌
visited = [[False] * M for _ in range(N)]
dp = [[0] * M for _ in range(N)]

dy = (-1, 1, 0, 0)
dx = (0, 0, -1, 1)

#### dfs함수. 이동경로를 print해줌
def dfs(y, x):
    ### 일단 0번 print
    if dp[y][x]:
        return dp[y][x]
    
    if visited[y][x]:
        print(-1)
        exit()

    visited[y][x] = True
    factor = arr[y][x]
    max_num = 1
    for i in range(4):
        ### new_x, new_y
        ny = y + dy[i] * factor
        nx = x + dx[i] * factor
        ### 경계면이라면 for문 거르기
        if not(0 <= ny < N and 0 <= nx < M):
            continue
        ### 벽이라면 거르기
        if arr[ny][nx] == 0:
            continue
        ### 방문 안했다면!
        max_num = max(dfs(ny, nx)+1, max_num)
            
    visited[y][x] = False
    dp[y][x] = max_num
    return max_num

print(dfs(0,0))

