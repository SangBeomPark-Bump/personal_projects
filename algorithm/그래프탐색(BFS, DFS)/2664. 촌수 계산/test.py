import sys
input = sys.stdin.readline
verbose = False

N = int(input())
x, y = map(int, input().split())
M = int(input())

arr = [[] for _ in range(N+1)]
for _ in range(M):
    u, v = map(int, input().split())
    arr[u].append(v)
    arr[v].append(u)


from collections import deque
def bfs(start, end):
    visited = [-1] * (N + 1)
    que = deque()
    que.append(start)
    visited[start] = 0

    while que:
        node = que.popleft()
        for a in arr[node]:
            if visited[a] < 0:
                que.append(a)
                visited[a] = visited[node] +1
            if a == end:
                return visited[a]
    
    return -1

print(bfs(x, y))