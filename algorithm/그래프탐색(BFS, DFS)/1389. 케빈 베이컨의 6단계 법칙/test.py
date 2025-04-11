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



from collections import deque
def bfs(start):
    visited =[0] + [-1] * (N)
    que = deque()
    que.append(start)
    visited[start] = 0
    while que:
        node = que.popleft()
        for a in arr[node]:
            if visited[a] < 0:
                que.append(a)
                visited[a] =visited[node] +1

    return sum(visited)

min_number = N * M

for i in range(1,N+1):
    temp_number = bfs(i)
    if temp_number < min_number:
        min_number = temp_number
        result = i

print(result)