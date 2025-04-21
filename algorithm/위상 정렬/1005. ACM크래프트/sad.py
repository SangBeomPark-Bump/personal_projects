from collections import deque

T = int(input())

for _ in range(T):
    N, K = map(int, input().split())
    D = [0] + list(map(int, input().split()))## timearr

    arr = [[] for _ in range(N + 1)]
    degree = [0] * (N + 1)
    for _ in range(K):
        X, Y = map(int, input().split())
        arr[X].append(Y)
        degree[Y] += 1

    W = int(input())

    que = deque()
    time = [0] * (N + 1)

    for i in range(1, N + 1):
        if degree[i] == 0:
            que.append(i)
            time[i] = D[i]

    while que:
        idx = que.popleft()

        for a in arr[idx]:
            degree[a] -= 1
            time[a] = max(time[idx] + D[a], time[a])
            if degree[a] == 0:
                que.append(a)

        if idx == W:
            break

    print(time[W])