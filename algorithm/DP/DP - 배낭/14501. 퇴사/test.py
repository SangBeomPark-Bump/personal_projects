import sys
input = sys.stdin.readline
verbose = False
verboses = [False for _ in range(10)]

N = int(input())


arr = [tuple(map(int, input().split()) ) for _ in range(N)]
arr = [(0,0)] + arr



dp = [0] * (N+1)

def test(n):
    global dp
    day, wage = arr[n]
    next = n + day - 1
    for i in range(1, N+1):
        prev = i - day
        case1= 0
        if i == next and prev >= 0:
            case1 = dp[prev] + wage
        case2 = dp[i-1]

        dp[i] = max(case1, case2, dp[i])


for i in range(1,N+1):
    test(i)

print(dp[-1])