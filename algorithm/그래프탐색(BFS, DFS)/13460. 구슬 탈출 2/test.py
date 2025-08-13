import sys
input = sys.stdin.readline
INF = float("inf")


N, M = map(int, input().split())

arr = [list(input().strip('\n')) for _ in range(N)]

dydx = [(0, -1), (0, 1), (1, 0), (-1, 0)]

for n in range(N):
    for m in range(M):
        if arr[n][m] == "R":
            loc_r = (n, m)
            arr[n][m] = "."
        if arr[n][m] == "B":
            loc_b = (n, m)
            arr[n][m] = "."
        if arr[n][m] == "O":
            loc_o = (n, m)

def move(loc_r, loc_b, kind):
    ry, rx = loc_r
    by, bx = loc_b

    arr[ry][rx] = "R"
    arr[by][bx] = "B"

    dy, dx = dydx[kind]
    r_hole = False
    b_hole = False
    while True:
        rny, rnx = ry + dy, rx + dx
        bny, bnx = by + dy, bx + dx

        move_red, move_blue = not r_hole, not b_hole
        if arr[rny][rnx] in ("#", "B"):
            move_red = False
        
        if arr[bny][bnx] in ("#", "R"):
            move_blue = False
        
        if move_red:
            arr[ry][rx] = "."
            ry, rx = rny, rnx
            arr[ry][rx] = "R"
            if (ry, rx) == loc_o:
                r_hole = True
                arr[ry][rx] = "O"
        
        if move_blue:
            arr[by][bx] = "."
            by, bx = bny, bnx
            arr[by][bx] = "B"

            if (by, bx) == loc_o:
                b_hole = True
                arr[by][bx] = "O"

        if not (move_red or move_blue):
            break

    arr[ry][rx] = "." if arr[ry][rx] != "O" else "O"
    arr[by][bx] = "." if arr[by][bx] != "O" else "O"
    return (ry, rx), (by, bx)

from collections import deque

def bfs(loc_r, loc_b, loc_o):
    que = deque()
    que.append((loc_r, loc_b, 0))
    visited = [ [ [ [False for _ in range(M)] for _ in range(N) ] for _ in range(M)  ] for _ in range(N) ]

    ry, rx = loc_r
    by, bx = loc_b

    visited[ry][rx][by][bx] = True

    while que:
        cur_r, cur_b, deg = que.popleft()
        ### 10회 초과한 경우
        if deg == 10:
            return  -1

        for k in range(4):
            new_r, new_b = move(cur_r, cur_b, k)
            
            nry, nrx = new_r
            nby, nbx = new_b

            if visited[nry][nrx][nby][nbx]:
                continue

            if new_b == loc_o:
                continue

            if new_r == loc_o:
                return deg + 1
            
            visited[nry][nrx][nby][nbx] = True
            que.append((new_r, new_b, deg + 1))
    ## 가능한 경우의 수를 모두 조사한 경우
    return -1

print(bfs(loc_r, loc_b, loc_o))


