import sys
input = sys.stdin.readline
verbose = False
verboses = [False for _ in range(10)]
from heapq import heappop, heappush

prob_num = 0
while True:
    N = int(input())

    if N == 0:
        break
    prob_num +=1

    arr = [list(map(int, input().split() ) ) for _ in range(N)]

    INF = float("INF")
    arr2 = [ [INF for _ in range(N)] for _ in range(N)]
    arr2[0][0] = arr[0][0]

    dx = (0, 0,1,  -1)
    dy = (1, -1, 0, 0)
    que = []
    heappush(que, (arr[0][0], (0, 0)))
    while que:
        dist, (y, x) =  heappop(que)
        for i in range(4):
            ny = y + dy[i]
            nx = x + dx[i]
            if not(0 <= ny < N and 0 <= nx < N):
                continue
            else:
                next_dist = dist + arr[ny][nx]
                if next_dist < arr2[ny][nx]:
                    arr2[ny][nx] = next_dist
                    heappush(que, (next_dist,(ny, nx)))

    print(f'Problem {prob_num}: {arr2[N-1][N-1]}')