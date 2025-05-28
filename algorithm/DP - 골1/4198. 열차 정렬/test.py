import sys
input = sys.stdin.readline
verbose = False
verboses = [False for _ in range(10)]
INF = float("inf")

N = int(input())

arr = [int(input()) for _ in range(N)]

incdp = [0 for _ in range(N)]
decdp = [0 for _ in range(N)]

ans = 0
for n in range(N-1, -1, -1):
    incdp[n] = 1
    decdp[n] = 1
    for i in range(n+1, N):
        if arr[i] > arr[n]:
            incdp[n] = max(incdp[n], incdp[i] + 1)
        else:
            decdp[n] = max(decdp[n], decdp[i] + 1)
    ans = max(ans, incdp[n] + decdp[n] -1)
print(ans)