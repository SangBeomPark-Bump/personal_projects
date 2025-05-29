import sys
input = sys.stdin.readline
verbose = False
verboses = [False for _ in range(10)]
INF = float("inf")

N = int(input())
K = int(input())
K -= 1

fibonachi = [1, 1]
for _ in range(2, N+1):
    fibonachi.append( fibonachi[-2] + fibonachi[-1])

ans = 0
for x in range(N):
    if x < K:
        for y in range(K):
            x, y = sorted((x, y))
            ans += fibonachi[x] * fibonachi[K - y -1] * fibonachi[N - K -1]
    elif x == K:
        ans += fibonachi[K] * fibonachi[N-K-1]
    else:
        for y in range(K+1, N):
            y, x = sorted((y, x))
            ans += fibonachi[K] * fibonachi[y - K - 1] * fibonachi[N - x -1]

print(ans)