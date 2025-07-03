import sys
input = sys.stdin.readline
INF = float("inf")
MOD = int(1e9) + 7

X = 9999
dp = [ [0 for _ in range(3)] for _ in range(X//3 +1)]
dp[0][0] = 1
for n in range(1, X//3 + 1):
    a, b, c = dp[n-1]
    dp[n] = [(3*a + 2 * b + 2 * c) % MOD , (a+b)% MOD, (a+b+c) % MOD]


T = int(input())

for _ in range(T):
    n = int(input())
    if n % 3 :
        print(0)
    else:
        print(dp[n//3][0])

# for i in arr:
#     print(i)