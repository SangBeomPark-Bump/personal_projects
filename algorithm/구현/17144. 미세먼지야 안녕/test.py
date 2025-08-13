import sys
input = sys.stdin.readline
INF = float("inf")


N, M, T = map(int, input().split())
arr = [list(map(int, input().split() ) ) for _ in range(N)]


for y in range(N):
    if arr[y][0] == -1:
        upper = y
        break

dydx = [(1, 0), (-1, 0), (0, 1), (0, -1)]
def diffusion():
    delta = [ [0 for _ in range(M)] for _ in range(N)]

    for y in range(N):
        for x in range(M):
            if arr[y][x] <= 4:
                continue

            for dy, dx in dydx:
                ny = y + dy
                nx = x + dx

                if not(0 <= ny < N and 0 <= nx < M):
                    continue

                if arr[ny][nx] < 0:
                    continue

                delta[ny][nx] += arr[y][x] // 5
                delta[y][x] -= arr[y][x] // 5
    
    for y in range(N):
        for x in range(M):
            arr[y][x] += delta[y][x]

def circulate(is_upper):
    x = -1 if is_upper else 1
    cir_mode = [(0, 1), (x, 0), (0, -1), (-x, 0)]

    mode_idx = 0

    cury, curx = upper, 1
    cury += 1 if not is_upper else 0

    last_value = 0

    while True:
        if arr[cury][curx] < 0:
            break

        arr[cury][curx], last_value = last_value, arr[cury][curx]

        dy, dx = cir_mode[mode_idx]

        ny, nx = cury + dy, curx + dx

        while not( 0 <= ny < N and 0 <= nx < M):
                mode_idx +=1
                dy, dx = cir_mode[mode_idx]
                ny, nx = cury + dy, curx + dx
        
        cury, curx = ny, nx

for t in range(T):
    diffusion()
    circulate(True)
    circulate(False)

result = 0
for y in range(N):
    for x in range(M):
        result +=arr[y][x]
print(result + 2)