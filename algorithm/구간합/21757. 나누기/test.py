import sys
input = sys.stdin.readline

N = int(input())
array = [0] + list(map(int, input().split()))

sum_arr = [0 for _ in range(N+1)]

for i in range(1, N+1):
    sum_arr[i] += array[i] + sum_arr[i-1]

result = 0
sum_arr = sum_arr[1:]
dp = [0, 0, 0]

if sum_arr[-1] % 4 == 0:
    fund_num =  sum_arr[-1] // 4
    if fund_num !=0:
        for i in sum_arr:
            if i == fund_num:
                dp[0] +=1
            if i == fund_num * 2:
                dp[1] += dp[0]
            if i == fund_num * 3:
                dp[2] += dp[1]
        result = dp[-1]
        
    else:
        cnt = sum_arr.count(0)
        result = (cnt-1) * (cnt-2) * (cnt -3)// 6

print(result)