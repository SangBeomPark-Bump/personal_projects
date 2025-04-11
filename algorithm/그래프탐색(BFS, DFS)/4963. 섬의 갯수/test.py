import sys
input = sys.stdin.readline
verbose = False

sys.setrecursionlimit(30000)

while True:
    w, h = map(int, input().split())
    if (w, h) == (0, 0):
        break

    arr =  [list(map(int,input().split())) for _ in range(h)]
    ### 방문 했는지 안했는지 알려줌
    visited = [[False] * w for _ in range(h)]
    ### 이동방향(4개 - 굳이 4개나 쓸이유는 없긴한데 그냥 멋있자낭)
    dy = (1, 1, 1, 0, 0,-1,-1,-1)
    dx = (1, 0,-1, 1,-1, 1, 0,-1)

    def island_dfs(y, x):
        # if verbose:
        #     print(y, x)
        ### visited에 넣기 (y, x임에 주의!)
        visited[y][x] = True
        ### 이동메커니즘
        for i in range(8):
            ### new_x, new_y
            ny = y + dy[i]
            nx = x + dx[i]
            ### 경계면이라면 for문 거르기
            if not(0 <= ny < h and 0 <= nx < w):
                continue
            ### 벽이라면 거르기
            if arr[ny][nx] == 0:
                continue
            ### 방문 안했다면!
            if not visited[ny][nx]:
                ### 얘로 재귀함수돌리기
                island_dfs(ny, nx)
                #### 재귀함수라서 깊이기반 탐색이 된다. 재귀함수의 특징이야!


    cnt = 0
    for y in range(h):
        for x in range(w):
            if (not visited[y][x]) and (arr[y][x] == 1):
                island_dfs(y, x)
                cnt +=1
    print(cnt)