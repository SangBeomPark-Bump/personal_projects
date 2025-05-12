import sys
input = sys.stdin.readline
verbose = False
verboses = [False for _ in range(10)]


N, M = map(int, input().split())
arr = [list(map(int, input().split() ) ) for _ in range(N)]

INF = float("INF")
updp = [ [ -INF for _ in range(M)] for _ in range(N)]
downdp = [ [ -INF for _ in range(M)] for _ in range(N)]
updp[-1][0] = arr[-1][0]

for n in range(N-1, -1, -1):
    for m in range(M):
        if n - 1>=0:
            updp[n-1][m] = max(updp[n-1][m] , updp[n][m] + arr[n-1][m])
        if m+1 < M:
            updp[n][m+1] = max(updp[n][m+1], updp[n][m] + arr[n][m+1])


for n in range(N):
    for m in range(0, M):
        downdp[n][m] = max(downdp[n][m], updp[n][m] + arr[n][m]) 
        if n +1 < N:
            downdp[n+1][m] = max(downdp[n+1][m], downdp[n][m] + arr[n+1][m])
        if m +1 < M:
            downdp[n][m+1] = max(downdp[n][m+1], downdp[n][m] + arr[n][m+1])
    
print(downdp[-1][-1])