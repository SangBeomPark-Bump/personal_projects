import sys
input = sys.stdin.readline
INF = float("inf")

N, K = map(int, input().split())
arr = list(map(int, input().split()))

def fill(arr):
    x = min(arr)

    for i in range(len(arr)):
        if arr[i] == x:
            arr[i] +=1

def putarr(arr, U):

    for i in range(len(arr)):
        U[i][0] = arr[i]

def turn_one(U):
    for x in range(N-1, -1, -1):
        w = 0
        for y in range(N):
            if U[y][x]:
                w +=1
        if w:
            break
    h = x + 1

    for y in range(N):
        if U[y][0]:
            break
    
    starty = y
    endy = y + w

    if N - endy < h:
        return False

    for y in range(starty, endy):
        for x in range(0, h):
            ny, nx = endy + x, w - (y - starty)
            U[ny][nx], U[y][x] = U[y][x], U[ny][nx]
    return True

def turn(U):
    U[0][0] , U[1][1] = U[1][1], U[0][0]
    while turn_one(U):
        continue
    return

def level(U):
    delta = [ [0 for _ in range(N)] for _ in range(N)]
    dydx = [(0, 1), (0, -1), (1, 0), (-1, 0)]
    for y in range(N):
        for x in range(N):
            if not U[y][x]:
                continue
                
            for dy, dx in dydx:
                ny = y + dy
                nx = x + dx

                if not( 0 <= ny < N and 0 <= nx < N):
                    continue
                
                if not U[ny][nx]:
                    continue

                if U[y][x] <= U[ny][nx]:
                    continue
                factor = (U[y][x] - U[ny][nx]) // 5

                delta[ny][nx] += factor
                delta[y][x] -= factor
    
    for y in range(N):
        for x in range(N):
            U[y][x] += delta[y][x]

def flatten(U):
    result = []
    for y in range(N):
        for x in range(N):
            if not U[y][x]:
                break
            result.append(U[y][x])
            U[y][x] = 0
    
    return result

def midput(U):
    for y in range(N//2):
        nexty = N - 1 - y
        U[y][0], U[nexty][1] = U[nexty][1], U[y][0]
    
    for y in range(N//2, N//2 + N//4):
        for x in range(2):

            nexty = N - (y - N// 2) - 1
            nextx = 3 - x

            U[y][x], U[nexty][nextx] = U[nexty][nextx], U[y][x]

def cycle(arr):
    U = [ [0 for _ in range(N)] for _ in range(N)]
    fill(arr)
    putarr(arr, U)

    turn(U)
    level(U)
    arr = flatten(U)

    putarr(arr, U)

    midput(U)
    level(U)
    arr = flatten(U)

    return arr

ans = 0
while True:
    if max(arr) - min(arr) <= K:
        print(ans)
        break
    arr = cycle(arr)
    ans += 1