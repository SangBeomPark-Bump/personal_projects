import sys
input = sys.stdin.readline
from collections import deque

N = int(input())
INF = N * N + 1

dydx = ( (1, 0), (-1, 0), (0, 1), (0, -1))

arr = [list(map(int, input().split() ) ) for _ in range(N)]

for y in range(N):
    for x in range(N):
        if arr[y][x] == 9:
            cur_loc = (y, x)
            arr[y][x] = 0


def eat(loc, size):
    visited = [[False for _ in range(N)] for _ in range(N)]
    time = 0

    que = deque()
    que.append((loc, 0))
    visited[loc[0]][loc[1]] = True

    result = (INF, INF, INF)

    while que:
        (y, x), cur_time = que.popleft()
        if cur_time < time:
            break
        if arr[y][x] and arr[y][x] < size:
            time = cur_time
            result = min(result, (cur_time, y, x))
            continue

        for dy, dx in dydx:
            ny = y + dy
            nx = x + dx

            if not( 0 <= ny < N and 0 <= nx < N):
                continue
            if visited[ny][nx]:
                continue
            if arr[ny][nx] > size:
                continue
            visited[ny][nx] = True
            que.append(((ny, nx), cur_time + 1))

    return result


spent_time = 0
eaten_fish = 0
cur_size = 2
# print(cur_loc)
while True:
    cur_time, y, x = eat(cur_loc, cur_size)
    if cur_time == INF:
        break

    arr[y][x] = 0
    cur_loc = (y, x)
    # print(cur_loc)

    spent_time += cur_time
    eaten_fish += 1

    if eaten_fish == cur_size:
        eaten_fish = 0
        cur_size +=1

print(spent_time)