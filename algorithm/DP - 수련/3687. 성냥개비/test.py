import sys
input = sys.stdin.readline
verbose = False
verboses = [False for _ in range(10)]

T = int(input())
numbers = [6, 2, 5, 5, 4, 5, 6, 3, 7, 6]

INF = float("inf")

dp = [ INF for _ in range(101)]
dp[2] = 1
dp[3] = 7
dp[4] = 4
dp[5] = 2
dp[6] = 6
dp[7] = 8

for n in range(8, 101):
    for number, value in enumerate(numbers):
        prev_index = n - value
        if prev_index >1:
            prev_number_str = str(dp[prev_index])
            for i in range(len(prev_number_str) +1 ):
                if i == 0 and number == 0:
                    continue
                temp_number = int(prev_number_str[0:i] + str(number) + prev_number_str[i:])
                dp[n] = min(dp[n], temp_number)

dp2 = [-INF, -INF]

for n in range(2, 101):
    if n%2 ==1:
        temp = int('7' + "1"* ((n//2) - 1))
    else:
        temp = int("1"* ((n//2)))
    dp2.append(temp)


for _ in range(T):
    N = int(input())
    print(dp[N], dp2[N])

