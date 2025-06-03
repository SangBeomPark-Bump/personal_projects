import sys
input = sys.stdin.readline
verbose = False
verboses = [False for _ in range(10)]
INF = float("inf")


N, K = map(int, input().split())
arr = [int(input().strip('\n')) for _ in range(N)]

def bl(bitmask):
    cnt = 0
    while bitmask >0:
        if bitmask % 2 == 1:
            cnt +=1
        bitmask //=2
    return cnt

dp = [[[ 0 for _ in range(N)] for _ in range(N)] for _ in range(1<<N)]
for n in range(N):
    dp[1<<n][n][n] = 1

for n in range(1, N): 
    for bitmask in range(1,1<<N): ## 위랑 합쳐 비트마스크 번
        if bl(bitmask) != n:
            continue
        for start in range(N): # N번
            for new_number in range(N): ## (N번)
                if abs(arr[start] - arr[new_number]) <= K:
                        continue
                if bitmask & (1<<new_number):
                    continue
                for end in range(N):
                    dp[bitmask | (1<<new_number)][new_number][end] += dp[bitmask][start][end]
a = 0
for i in range(N):
    a += sum(dp[(1<<N) -1][i])
print(a)


# for i in arr:
#     print(arr)