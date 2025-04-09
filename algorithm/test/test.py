import sys
input = sys.stdin.readline

N, M = map(int, input().split())

arr = []
for _ in range(N):
    line = list(map(int, input().split()))
    arr.append(line)

for _ in range(M):
    x1, y1, x2, y2  = map(int, input().split())
    cur_sum = 0
    for j in range(x1 - 1, x2):
        cur_sum += sum(arr[j][y1 -1 : y2])
    print(cur_sum)