import sys
input = sys.stdin.readline
verbose = False
verboses = [False for _ in range(10)]


R, C = map(int, input().split())
loc = [ (-1, -1) for _ in range(int(3e5) + 1) ]
arr = []
for r in range(R):
    temp = list(map(int, input().split()))
    arr.append(temp)
    for c in range(C):
        loc[temp[c]] = (r,c)

dp = [ [1 for _ in range(C)] for _ in range(R)]

move = []

for i in range(-1, 2):
    for j in range(-1, 2):
        if i == 0 and j == 0:
            continue
        move.append((j,i))


for number in range(int(3e5), -1, -1):
# for number in range(9, -1, -1):
    y, x =  loc[number]

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

        min_number = min(min_number, arr[ny][nx])
    
    if min_number == 3e6+1:
        continue
    miny, minx = loc[min_number]

    dp[miny][minx] += dp[y][x]
    dp[y][x] = 0


for i in dp:
    print(*i)