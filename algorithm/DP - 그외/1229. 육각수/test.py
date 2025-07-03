import sys
input = sys.stdin.readline
INF = float("inf")

N = int(input())
dp = [ INF for _ in range(N+1)]
dp[0] = 0
dp[1] = 1

k = 2
cur_arr = [1]

for n in range(2, N+1):
    if cur_arr[-1] + 4*k - 3 == n: 
        k +=1
        cur_arr.append(n)
    for sub_hex in cur_arr:
        dp[n] = min(dp[n], dp[n - sub_hex] + 1)

print(dp[N])
# for i in arr:
#     print(i)