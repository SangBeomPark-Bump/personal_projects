import sys
input = sys.stdin.readline
verbose = False
verboses = [False for _ in range(10)]
INF = float("inf")

N = int(input())
# arr = [input().strip('\n') for _ in range(N)]
MOD = int(1e9) + 7

dp = [ [0 for _ in range(6) ] for _ in range(6)]
dp[0][0] = 1

for _ in range(N):
    word = input().strip('\n')
    print(f'이번 단어 : {word}')
    for i in range(1,6):
        for j in range(i, 6):
            if word[: j - i +1] == "UNIST"[i-1:j]:
                for k in range(i):
                    dp[i][j] += dp[k][i-1]
            dp[i][j] %= MOD

for i in range(1, 6):
    ans += dp[i][-1]
ans %= MOD
print(ans)