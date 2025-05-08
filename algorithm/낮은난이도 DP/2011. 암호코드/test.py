import sys
input = sys.stdin.readline
verbose = False
verboses = [False for _ in range(10)]


string = input()
N = len(string)
div = 1000000


dp = [ 0 for _ in range(N+1)]

if string[0] == '0':
    print(0)
    exit()

dp[0] = 1
dp[1] = 1

for n in range(2, N+1):
    if string[n-1] != '0':
        dp[n] += dp[n-1] 
        dp[n] += dp[n-2] if 10 <= int(string[n-2:n]) <=26 else 0
    else:
        if 0 <= int(string[n-2:n]) <= 26:
            dp[n] += dp[n-2] if 10 <= int(string[n-2:n]) <=26 else 0
        else:
            print(0)
            exit()
    dp[n] %= div
print(dp[-1])
