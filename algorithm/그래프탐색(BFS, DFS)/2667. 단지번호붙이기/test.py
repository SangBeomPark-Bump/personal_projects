import sys
input = sys.stdin.readline
verbose = False

N = int(input())
arr =  [list(map(int,list(input().strip('\n')))) for _ in range(N) ]



### 방문 했는지 안했는지 알려줌
visited = [[False] * N for _ in range(N)]
### 이동방향(4개 - 굳이 4개나 쓸이유는 없긴한데 그냥 멋있자낭)
dy = (-1, 1, 0, 0)
dx = (0, 0, -1, 1)

#### dfs함수. 이동경로를 print해줌
def dfs(y, x, depth):
    visited[y][x] = True
    ### 이동메커니즘
    for i in range(4):
        ### new_x, new_y
        ny = y + dy[i]
        nx = x + dx[i]
        ### 경계면이라면 for문 거르기
        if not(0 <= ny < N and 0 <= nx < N):
            continue
        ### 벽이라면 거르기
        if arr[ny][nx] == 0:
            continue
        ### 방문 안했다면!
        if not visited[ny][nx]:
            depth = dfs(ny, nx, depth +1)
    return depth

danjis = []
for y in range(N):
    for x in range(N):
        if (not visited[y][x]) and (arr[y][x] == 1):
            danjis.append(dfs(y, x, 1))


danjis.sort()
print(len(danjis))
for danji in danjis:
    print(danji)