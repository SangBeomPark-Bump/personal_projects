import sys
from collections import deque

T = int(input())
for _ in range(T):
    N, K= map(int, input().split())

    time_arr = [0] + list(map(int, input().split()))


    start_arr = [[] for _ in range(N + 1)]
    end_arr = [0] * (N + 1)

    for _ in range(K):
        X, Y = map(int, input().split())
        start_arr[X].append(Y)
        end_arr[Y] += 1

    W = int(input())

    que = deque()

    time_arr2 = [0] * (N + 1)

    for b_name, b_time in enumerate(end_arr[1:], start=1):
        if b_time == 0:
            que.append(b_name)
            time_arr2[b_name] = time_arr[b_name]

    while que:
        cur_building = que.popleft()

        for next_building in start_arr[cur_building]:
            time_arr2[next_building] = max(time_arr2[next_building],time_arr2[cur_building] + time_arr[next_building])
            end_arr[next_building] -=1
            if end_arr[next_building] == 0:
                que.append(next_building)

        if cur_building == W:
            break

    print(time_arr2[W])