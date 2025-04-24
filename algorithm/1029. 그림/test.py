import sys
input = sys.stdin.readline
verbose = False
verboses = [False for _ in range(10)]

N = int(input())

arr = [list(map(int, list(input().strip('\n')))) for _ in range(N)]

dp = [ [11 for _ in range((1<<(N)))] for _ in range(N)]
dp[0][1<<0] = 0

cnt =1

for n in range(N-1):
    next = [ [11 for _ in range((1<<N))] for _ in range(N)]
    changed = False
    for cur_loc in range(N):
        for hist in range((1<<(n+1)) -1, (1<<(n+2)) - 1):
            if dp[cur_loc][hist] < 10:
                # print(cur_loc, hist)
                for next_loc in range(N):
                    if arr[cur_loc][next_loc] >= dp[cur_loc][hist] and not (1 << next_loc) & hist:
                        # print(cur_loc, next_loc)
                        changed = True
                        next[next_loc][hist | (1<<next_loc)] = min(arr[cur_loc][next_loc], next[next_loc][hist | (1<<next_loc)])
    if not changed:
        break
    cnt +=1
    dp = next

print(cnt)
