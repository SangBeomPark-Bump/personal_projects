import sys
input = sys.stdin.readline
verbose = False
from collections import deque

M, N = map(int, input().split())
arr =  [list(map(int,input().split())) for _ in range(N)]

mydeq = deque()
for y in range(N):
    for x in range(M):
        if arr[y][x] ==1:
            mydeq.append((y,x))


def bfs(my_que : deque):
    ### 여기는 앞에와 같음
    dy = (-1, 1, 0, 0)
    dx = (0, 0, -1, 1)

    while my_que:
        y, x = my_que.popleft()
        # print(y, x)
        for i in range(4):
            ny = y + dy[i]
            nx = x + dx[i]
            if not(0 <= ny < N and 0 <= nx < M):
                continue
            if arr[ny][nx] == 0:
                arr[ny][nx] = arr[y][x]+1
                my_que.append((ny, nx))

bfs(mydeq)


sad = False
result = 0

for y in range(N):
    for x in range(M):
        if arr[y][x] == 0:
            sad = True
        result = max(result, arr[y][x] - 1)

if sad:
    print(-1)
else:
    print(result)
