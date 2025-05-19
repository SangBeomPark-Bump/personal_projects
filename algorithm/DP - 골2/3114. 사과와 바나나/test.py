import sys
input = sys.stdin.readline
verbose = False
verboses = [False for _ in range(10)]
INF = float("inf")


N, M = map(int, input().split())
arr = [input().strip('\n').split() for _ in range(N)]


apples = [[ 0 for _ in range(M)] for _ in range(N)]
bananas = [[ 0 for _ in range(M)] for _ in range(N)]
for n in range(N):
    apple = 0
    banana = 0
    for applem in range(M):
        bananam = M - applem - 1
        if arr[n][applem][0] == "A":
            apple += int(arr[n][applem][1:])
        if arr[n][bananam][0] == 'B':
            banana += int(arr[n][bananam][1:])
        apples[n][applem] = apple
        bananas[n][bananam] = banana


dp = [[ 0 for _ in range(M)] for _ in range(N)]
dp[0][0] = bananas[0][0] 
dp[0][0] -= int(arr[0][0][1:]) if arr[0][0][0] == "B" else 0


for n in range(N):
    for m in range(M):
        if n == 0 and m == 0:
            continue
        # gained = apples[n][m] + bananas[n][m]
        factor = int(arr[n][m][1:])
        letter = arr[n][m][0]

        case1 = 0
        case2 = 0
        case3 = 0

        ### 왼쪽에서 넘어온 경우: case1
        if m>=1:
            case1 = dp[n][m-1]
            if letter == 'B':
                case1 -= factor
        
        #### 위에서 아래로 내려온경우: case2
        if n>=1:
            case2 = dp[n-1][m] + apples[n][m] + bananas[n][m] - factor

        #### 대각선 아래로 내려온 경우 : case3
        if n>=1 and m>=1:
            case3 = dp[n-1][m-1] + apples[n][m] +bananas[n][m] - factor
        dp[n][m] = max(case1, case2, case3)

print(dp[-1][-1])