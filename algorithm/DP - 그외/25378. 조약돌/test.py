import sys
input = sys.stdin.readline
verbose = False
verboses = [False for _ in range(10)]

N = int(input())

arr = [0] + list(map(int, input().split()))

dp = [ set() for _ in range(N+1) ]
cnt = 0
dp[0].add(0)
for n in range(1, N+1):
    cur_number = arr[n] # 현재 검사하고자 하는 숫자
    prev_set = dp[n-1] # 이전에 남았던 돌멩이 후보들

    dp[n].add(cur_number) ## 일단 cur_number를 집어넣는다.

    for pebble in prev_set: ## 돌멩이 후보들중 하나를 골라서
        pebble_cand = cur_number - pebble ## 이번 숫자에서 뺀다
        if pebble_cand == 0: ## 같다면!
            dp[n] = {0} ### 0으로 바꿔버리기~
            cnt +=1
            break
        else: # 다르다면!!
            dp[n].add( pebble_cand if pebble_cand >0 else 0 ) ### 차이가 0보다 크면 차이를, 작다면 0을 집어넣는는다.

print(N - cnt)