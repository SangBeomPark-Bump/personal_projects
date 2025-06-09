import sys
input = sys.stdin.readline
INF = float("inf")

N = int(input())
arr = [list(map(int, input().split() ) ) for _ in range(N)]

def temp(number, start):
    return number - start if number>start else number - start +100

ans = 1
for start in range(1, 101): ## 100번

    test = [ sorted([temp(a, start), temp(b, start)]) for a, b in arr] # 50번
    test.sort( key= lambda x: x[0]) # 50log50번
    test = [ end for _, end in sorted(test, key = lambda x: x[0])] # 50log50번

    
    dp = [1 for _ in range(N)] # 50번

    for i in range(N): # 50번 * 50번
        for j in range(i): # 50/2번
            if test[j] > test[i]:
                dp[i] = max(dp[i], dp[j] + 1)
    ans = max(max(dp), ans)

print(ans)