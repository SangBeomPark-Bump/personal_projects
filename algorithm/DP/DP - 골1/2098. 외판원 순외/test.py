import sys
input = sys.stdin.readline
INF = float("inf")
def bitrank(n):
    cnt = 0
    while n >0:
        if n%2:
            cnt +=1
        n //=2
    return cnt

N = int(input())

arr = [list(map(int, input().split() ) ) for _ in range(N)]

ans = INF

for cur_start in range(N):
    bits = [ [] for _ in range(N)]

    dp = [ [INF for _ in range(1<<N)]for _ in range(N)]

    for bit in range(1<<N):
        if 1<<cur_start & bit:
            continue
        bits[bitrank(bit)].append(bit)

    temp = list(range(N))
    temp.remove(cur_start)

    for x in range(N):
        if not (arr[cur_start][x]):
            continue
        dp[x][1<<x] = arr[cur_start][x]

    for i in range(1, N):
        for bit in bits[i]: ### 1<<(N-1) 번
            for cur_last in temp: ## N번
                if not (bit & 1<< cur_last):
                    continue
                for next_last in temp: ## N번
                    if ((1<< next_last) & bit) or arr[cur_last][next_last] == 0:
                        continue
                    dp[next_last][bit | (1 <<next_last)] = min(dp[next_last][bit | (1<<next_last)], dp[cur_last][bit] + arr[cur_last][next_last])

    for n in range(N):
        if not (arr[i][cur_start]):
            continue
        ans = min(ans, dp[i][bits[-1][0]] + arr[i][cur_start])

print(ans)