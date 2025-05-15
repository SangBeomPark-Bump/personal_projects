import sys
input = sys.stdin.readline
verbose = False
verboses = [False for _ in range(10)]


R, C = map(int, input().split())
# loc = [ (-1, -1) for _ in range(int(3e5) + 1) ]
arr = []


from heapq import heappop, heappush
hq = []

for r in range(R):
    temp = list(map(int, input().split()))
    arr.append(temp)
    for c in range(C):
        heappush(hq,( -temp[c], r, c))

dp = [ [1 for _ in range(C)] for _ in range(R)]

move = []

for i in range(-1, 2):
    for j in range(-1, 2):
        if i == 0 and j == 0:
            continue
        move.append((j,i))



while hq:
    number, y, x = heappop(hq)
    number *= -1

    if y<0:
        continue
    min_number = 3e6 + 1
    for dy, dx in move:
        ny = y + dy
        nx = x + dx
        if ny <0 or ny>= R or nx < 0 or nx >=C:
            continue

        if dp[ny][nx] == 0:
            continue

        if min_number >arr[ny][nx]:
            min_number = arr[ny][nx]
            miny, minx = ny, nx

    if min_number == 3e6+1:
        continue

    dp[miny][minx] += dp[y][x]
    dp[y][x] = 0


for i in dp:
    print(*i)