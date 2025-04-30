import sys
input = sys.stdin.readline
verbose = False
verboses = [False for _ in range(10)]
sys.setrecursionlimit(int(1e8))

N = int(input())
arr_p = [0] + list(map(int, input().split()))

arr_r = [list(map(int, input().split() ) ) for _ in range(N-1)]

nodes = [ [] for _ in range(N+1)]
if N>1:
    for bil1, bil2 in arr_r:
        nodes[bil1].append(bil2)
        nodes[bil2].append(bil1)
else:
    print(arr_p[1])
    exit()

visited = [True for _ in range(N+1)]
cnt = 0
def recursive(node, value, visited):
    global cnt
    if node >N:
        return value
    cnt +=1
    value = recursive(node+1, value, visited)
    if not visited[node]:
        pass
    else:
        visited[node] = False
        for loc in nodes[node]:
            visited[loc] = False
        
        cur_value = recursive(node +1, value + arr_p[node], visited)
        value = max(cur_value, value)
    return value

print(recursive(1, 0, visited))