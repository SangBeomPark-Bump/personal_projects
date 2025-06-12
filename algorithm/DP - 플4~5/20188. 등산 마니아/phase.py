import sys
input = sys.stdin.readline
INF = float("inf")

N = int(input())
nodes = [[] for _ in range(N+1)]
degrees = [0 for _ in range(N+1)]

for _ in range(N-1):
    n1, n2 = map(int, input().split())
    nodes[n1].append(n2)
    nodes[n2].append(n1)
    degrees[n1] += 1
    degrees[n2] += 1


from collections import deque
que = deque()
dp = [1 for _ in range(N+1)]
visited = [False for _ in range(N+1)]

for i in range(2, N+1):
    if degrees[i] == 1:
        que.append(i)
        degrees[i] = 0


visited[1] = True

while que:
    cur_node = que.popleft()
    visited[cur_node] = True
    cur_familiy = dp[cur_node]
    next_nodes = nodes[cur_node]
    for next_node in next_nodes:

        if visited[next_node]:
            continue

        dp[next_node] += dp[cur_node]
        degrees[next_node] -= 1

        if degrees[next_node] == 1:
            que.append(next_node)

ans = 0
for i in range(2, N+1):
    family = dp[i]
    ans += (N - 1) * family + (family) * (N-family)
print(ans//2)