import sys
input = sys.stdin.readline
verbose = False

sys.setrecursionlimit(10000)

# N, M = map(int, input().split())
N = int(input())

arr = [0] + [ int(input()) for _ in range(N)]

from collections import deque

def simple_bfs(node):
    visited = [False] * (N+1)
    visited[node] = True
    que = deque()
    que.append(node)
    length = 1
    while que:
        cur_node = que.popleft()
        next_node = arr[cur_node]

        if not visited[next_node]:
            visited[next_node] = True
            que.append(next_node)
            if verbose:
                print(cur_node, next_node, length)
            length +=1
    return node == next_node

result = 0
nodes = []
for i in range(1, N+1):
    if simple_bfs(i):
        result +=1
        nodes.append(i)

print(result)
for node in nodes:
    print(node)