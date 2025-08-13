import sys
input = sys.stdin.readline
verbose = False
verboses = [False for _ in range(10)]

N = int(input())

arr = [list(map(int, input().split() ) ) for _ in range(N)]


ans = float('inf')
for first_color in range(3):
    dp = [ [(float('inf'))] * 3 for _ in range(N)]
    for i in range(3):
        if i == first_color:
            dp[0][i] = arr[0][i]
    for n in range(1, N):
        for i in range(3):
            for j in range(3):
                if i != j:
                    dp[n][j] = min(dp[n][j], dp[n-1][i] + arr[n][j])
    dp[-1][first_color] = float('inf')
    ans = min(ans, min(dp[-1]))
print(ans)