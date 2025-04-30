import sys
input = sys.stdin.readline
verbose = False
verboses = [False for _ in range(10)]


N, M = map(int, input().split())
memories = list(map(int, input().split()))
costs = list(map(int, input().split()))  

dp = [ [0 for _ in range(sum(costs) +1)] for _ in range(N+1)]

for n in range(1, N+1):
    cur_memory = memories[n-1]
    cur_cost = costs[n-1]

    cur_dp = dp[n]
    prev_dp = dp[n-1]

    for cost in range(sum(costs) +1):
        case1 = 0
        if cost >= cur_cost:
            case1 = prev_dp[cost - cur_cost] + cur_memory
        case2 = 0
        if cost>0:
            case2 = cur_dp[cost-1]

        case3 = prev_dp[cost]

        cur_dp[cost] = max(case1, case2, case3)

    # print(cur_dp)

for cost, max_memory in enumerate(dp[-1]):
    if max_memory >= M:
        print(cost)
        break