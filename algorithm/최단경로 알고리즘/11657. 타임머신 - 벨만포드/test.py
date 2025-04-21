import sys
input = sys.stdin.readline
verbose = False
verboses = [False for _ in range(10)]


N, M = map(int, input().split())

arr = [list(map(int, input().split() ) ) for _ in range(M)]

nodes = [ [] for _ in range(N+1) ]
for start, end, time in arr:
    nodes[start].append((end, time))

from collections import deque
INF = float("INF")
dp = [[INF] * (N+1) for _ in range(N+1)]
dp[0][1] = 0

for n in range(1, N+1):
    dp[n][1] = 0
    # visited = [False] * (N+1)
    # visited[1] = True
    que = deque([1])
    while que:
        cur_node = que.popleft()
        # print(nodes[cur_node])
        for next_node, next_time in nodes[cur_node]:
            cur_time = dp[n-1][cur_node] + next_time
            # print(cur_node, next_node, cur_time, next_time)

            if dp[n][next_node] > cur_time :
                # visited[next_node] = True
                dp[n][next_node] = cur_time
                que.append(next_node)
        # print('-' * 50)
        # print(dp)

if dp[-1] != dp[-2] :
    print(-1)
else:
    for time in dp[-1][2:]:
        if time == float('inf'):
            print(-1)
        else:
            print(time)