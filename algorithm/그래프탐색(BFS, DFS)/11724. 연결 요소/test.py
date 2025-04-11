import sys
input = sys.stdin.readline
verbose = False

sys.setrecursionlimit(10000)

N, M = map(int, input().split())

arr = [[] for _ in range(N+1)]
for _ in range(M):
    u, v = map(int, input().split())
    arr[u].append(v)
    arr[v].append(u)


visited = [False] * (N+1)
def dfs(node):
    # print(node)
    visited[node] = True 
    for a in arr[node]:
        if not visited[a]:
            dfs(a)

cnt = 0
for i in range(1,N+1):
    if not visited[i]:
        dfs(i)
        cnt +=1

print(cnt)