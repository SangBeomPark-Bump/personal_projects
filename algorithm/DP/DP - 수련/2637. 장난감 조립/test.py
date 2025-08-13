import sys
input = sys.stdin.readline
verbose = False
verboses = [False for _ in range(10)]

N = int(input())
M = int(input())

arr = [list(map(int, input().split() ) ) for _ in range(M)]

node = [ [] for _ in range(N+1)]
degree = [0 for _ in range(N+1)]
make = [ [0 for _ in range(N+1)] for _ in range(N+1)]

for end, start, many in arr:
    node[start].append(end)
    make[end][start] += many
    degree[end] +=1


from collections import deque
que = deque()
for toy in range(1, N+1):
    if degree[toy] == 0:
        que.append(toy)
if verbose:
    print(que)

while que:
    toy = que.popleft()
    if max(make[toy]) == 0:
        fundamental = True
    else:
        fundamental = False
    for next_toy in node[toy]:
        degree[next_toy] -=1
        if degree[next_toy] ==0:
            que.append(next_toy)
        if not fundamental:
            for i in range(1,N):
                make[next_toy][i] +=make[toy][i] * make[next_toy][toy] 
            make[next_toy][toy] = 0
    if verbose:
        print(toy, fundamental, que, make[toy])


for toy, many in enumerate(make[N][1:], start=1):
    if many != 0:
        print(toy, many)