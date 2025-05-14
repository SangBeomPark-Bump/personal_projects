import sys
input = sys.stdin.readline
verbose = False
verboses = [False for _ in range(10)]

T = int(input())

for _ in range(T):
    N, M = map(int, input().split())
    arr = [list(map(int, input().split() ) ) for _ in range(M)]

    nodes = [ [] for _ in range(N+1)]
    degrees = [0 for _ in range(N+1)]

    for start, end, value in arr:
        nodes[start].append([end, value])
        nodes[end].append([start, value])
        degrees[start] +=1
        degrees[end] +=1

    from collections import deque
    que = deque()
    dp = [0 for _ in range(N+1)]

    degrees[1] += 2
    for i in range(N+1):
        if degrees[i] == 1:
            que.append(i)
            dp[i] += nodes[i][0][1]
            degrees[i] = 0


    while que:
        cur_node = que.popleft()

        for next_node, next_value in nodes[cur_node]:
            if degrees[next_node]:
                dp[cur_node] = min(dp[cur_node], next_value)
                dp[next_node] += dp[cur_node]
                degrees[next_node] -=1

            if degrees[next_node] == 1:
                degrees[next_node] = 0
                que.append(next_node)

    print(dp[1])