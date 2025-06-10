import sys
input = sys.stdin.readline
INF = float("inf")

N = int(input())
start = list(map(int, list(input().strip('\n'))))
end = list(map(int, list(input().strip('\n'))))

dp = [ [[INF, INF, INF, INF, INF] for _ in range(10)] for _ in range(N)]
dp[0][start[0]] = [0, 0, INF, 0, 0]

for i in range(1, N):
    for j in range(10):
        if dp[i-1][j][1] == INF:
            continue

        right_shift = dp[i-1][j][1]


        start_number = (start[i-1] + right_shift % 10) % 10
        end_number = end[i-1]

        right_min = end_number - start_number
        if right_min < 0:
            right_min = 10 + right_min

        left_min = 10 - right_min

        for right_move in range(right_min, right_min + 10):
            right_move %= 10
            left_move = left_min + right_move
            left_move %= 10
            next_num = (start[i] + right_move + right_shift) %10

            temp = [ dp[i-1][start_number][0] + right_move + left_move, right_shift + right_move, j, right_move, left_move ]
            dp[i][next_num] = min( dp[i][next_num], temp, key=lambda x: x[0])


ans = []

min_index = -1
min_value = INF
min_move = INF
end_number = end[-1]
last_start_number = -1
for start_number in range(10):

    right_min = end_number - start_number
    if right_min < 0:
        right_min = 10 + right_min

    left_min = 10 - right_min
    cur_value = min(left_min, right_min) + dp[-1][start_number][0]
    
    if min_value >= cur_value:
        min_value = cur_value
        min_move = [right_min, 0] if right_min < left_min else [0, left_min]
        last_start_number = start_number

ans.append(min_move)

for n in range(N-1, -1, -1):
    ans.append([dp[n][last_start_number][3] , dp[n][last_start_number][4]])
    last_start_number = dp[n][last_start_number][2]


print(min_value)
for i in range(1, N+2):
    if ans[-i][0]:
        print(i-1, ans[-i][0])
    if ans[-i][1]:
        print(i-1, -1 * ans[-i][1])
