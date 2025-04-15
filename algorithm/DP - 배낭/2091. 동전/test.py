import sys
input = sys.stdin.readline
verbose = False
verboses = [False for _ in range(10)]

X, *arr = map(int, input().split())
coins = [1, 5, 10, 25]



dp = [ [0]* 4 for _ in range(X+1)]

for x in range(1, X+1):
    cur_max = [0, 0, 0, 0]
    for i in range(4):
        temp = [0, 0, 0, 0]
        cur_coin = coins[i]
        prev = x - cur_coin
        if prev >=0 and arr[i] >= dp[prev][i] +1 :
            if (prev == 0) or (sum(dp[prev]) > 0):
                temp = dp[prev].copy()
                temp[i] += 1
        cur_max = max(cur_max, temp, key=sum)

    dp[x] = cur_max

print(' '.join(map(str,dp[-1])))