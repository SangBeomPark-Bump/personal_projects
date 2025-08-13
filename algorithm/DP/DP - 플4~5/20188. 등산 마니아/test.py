import sys
input = sys.stdin.readline
INF = float("inf")

N = int(input())
nodes = [[] for _ in range(N+1)]



# arr = [list(map(int, input().split() ) ) for _ in range(N-1)]

for _ in range(N-1):
    n1, n2 = map(int, input().split())
    nodes[n1].append(n2)
    nodes[n2].append(n1)


visited = [False for _ in range(N+1)]
dp = [0 for _ in range(N+1)]

def dfs(node):
    visited[node] = True
    cur_next_nodes = nodes[node]


    value = 1
    for next_node in cur_next_nodes:
        if visited[next_node]:
            continue
        value += dfs(next_node)
    
    dp[node] = value
    return value


visited[1] = True
for second_node in nodes[1]:
    dfs(second_node)

ans = 0
for i in range(2, N+1):
    family = dp[i]
    ans += (N - 1) * family + (family) * (N-family)
print(ans//2)