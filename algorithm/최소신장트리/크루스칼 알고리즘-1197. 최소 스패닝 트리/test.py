import sys
input = sys.stdin.readline
verbose = False
verboses = [False for _ in range(10)]
sys.setrecursionlimit(int(1e7))


V, E = map(int, input().split())

arr = [list(map(int, input().split() ) ) for _ in range(E)]
arr.sort(key=lambda x : x[2])

p = list(range(V+1))

def find(a):
    if a != p[a]:
        p[a] = find(p[a])
    return p[a]

def union(a, b, value):
    pa = find(a)
    pb = find(b)

    if pa == pb:
        return 0
    if pa< pb:
        pb, pa = pa, pb

    p[pa] = pb
    return value


ans = 0
for start, end, value in arr:
    ans += union(start, end, value)
print(ans)
