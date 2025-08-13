import sys
input = sys.stdin.readline
verbose = False
verboses = [False for _ in range(10)]
INF = float("inf")

N = int(input())
arr = list(map(int, input().split()))

value_to_index = dict()

for index, value in enumerate(arr):
    value_to_index[value] = index

dp = [[0 for _ in range(N)] for _ in range(N)]


max_score = 0
for first in range(N-1):
    for second in range(first+1, N):
        if dp[first][second]:
            continue
        d = arr[second] - arr[first]
        dp[first][second] = arr[first] + arr[second]
        third_number = arr[second] + d
        if third_number not in value_to_index.keys():
            continue

        cur_score = arr[first] + arr[second] + third_number
        start, end = second, value_to_index[third_number]
        dp[start][end] = cur_score
        next_number = third_number + d

        while True:
            if next_number not in value_to_index.keys():
                break
            cur_score += next_number
            start, end = end, value_to_index[next_number]
            dp[start][end] = cur_score
            next_number += d
        # print(arr[first], arr[second], cur_score)
        max_score = max(cur_score, max_score)
print(max_score)