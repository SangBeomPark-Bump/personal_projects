import sys
input = sys.stdin.readline
verbose = False
verboses = [False for _ in range(10)]

*arr, _ = list(map(int, input().split()))
N = len(arr)
arr = arr

INF = float("INF")
dp = [ [[ INF for _ in range(5) ] for _ in range(5) ] for _ in range(N)]

def move(start, end):
    if start == end:
        return 1
    if start == 0 or end == 0:
        return 2
    if start % 2 == 1 and end %2 ==1 :
        return 4
    if start %2 == 0 and end %2 ==0:
        return 4
    return 3

dp[0][arr[0]][0] = 2

for n in range(1, N):
    next_loc = arr[n]
    feet_arr = dp[n-1]
    for left in range(5):
        for right in range(5):
            if feet_arr[left][right] != INF:
                ### 왼쪽부터!
                cur_score = feet_arr[left][right]
                if right != next_loc:
                    dp[n][next_loc][right] = min(dp[n][next_loc][right], cur_score + move(left, next_loc))
                ### 다음 오른쪽!
                if left != next_loc:
                    dp[n][left][next_loc] = min(dp[n][left][next_loc], cur_score + move(right, next_loc))
                    
ans = INF
for left in range(5):
    for right in range(5):
        ans = min(dp[-1][left][right], ans)
print(ans)