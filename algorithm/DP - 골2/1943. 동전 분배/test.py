import sys
input = sys.stdin.readline
verbose = False
verboses = [False for _ in range(10)]
INF = float("inf")

for _ in range(3):
    N = int(input())
    arr = [list(map(int, input().split() ) ) for _ in range(N)]

    dp = [set() for _ in range(N+1)]
    dp[0].add(0)
    for n in range(1, N+1):
        coin, many = arr[n-1]
        for number in dp[n-1]:
            for i in range(many // 2 + 1):
                plus = number + coin * i * 2 + coin * (many % 2) 
                minus = abs(number - (coin * i*2 + coin * (many % 2) ) )
                dp[n].add(plus)
                dp[n].add(minus)
    print(1 if 0 in dp[-1] else 0)
