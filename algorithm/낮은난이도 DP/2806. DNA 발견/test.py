import sys
input = sys.stdin.readline
verbose = False
verboses = [False for _ in range(10)]

N = int(input())
string = "X" + input()

dp = [0, 0]
for n in range(1, N+1):
    dp = [min(dp) +1 if string[n] == "B" else dp[0]  ,  min(dp) +1 if string[n] == "A" else dp[1]]
print(dp[0])