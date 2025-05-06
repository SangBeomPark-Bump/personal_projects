import sys
input = sys.stdin.readline
verbose = False
verboses = [False for _ in range(10)]

N = int(input())
M = int(input())

arr = [list(map(int, input().split() ) ) for _ in range(M)]

node = [ [] for _ in range(N+1)]

for start, end, value in arr:
    node[start].append((end, value))
    node[end].append((start, value))

import heapq
visited = [False for _ in range(N+1)]
pq = []
visited[1] = True

ans = 0
for end, value in node[1]:
    heapq.heappush(pq, (value, end))


while pq:
    value, end =  heapq.heappop(pq)
    if not visited[end] :
        ans += value
        visited[end] = True
        for new_end, new_value in node[end]:
            heapq.heappush(pq, (new_value, new_end))

print(ans)