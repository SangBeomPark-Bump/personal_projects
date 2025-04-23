import sys
input = sys.stdin.readline
verbose = False
verboses = [False for _ in range(10)]

N = int(input())

arr = [list(map(int, list(input().strip('\n')))) for _ in range(N)]

dp = [ [11 for _ in range((1<<(N)))] for _ in range(N)]
dp[0][1<<0] = 0


for n in range(N-1):
    changed = False
    # print((1<<(n+1)) -1, (1<<(n+2)) - 1)
    for cur_loc in range(N):
        for hist in range((1<<(n+1)) -1, (1<<(n+2)) - 1):
            if dp[cur_loc][hist] >= 0:
                for next_loc in range(N):
                    if arr[cur_loc][next_loc] >= dp[cur_loc][hist] and not (1 << next_loc) & hist:
                        changed = True
                        dp[next_loc][hist | (1<<next_loc)] = min(arr[cur_loc][next_loc], dp[next_loc][hist | (1<<next_loc)])
    if not changed:
        n -= 1
        break

print(n+2)