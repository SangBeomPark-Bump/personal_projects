import sys
input = sys.stdin.readline
verbose = False
verboses = [False for _ in range(10)]
INF = float('inf')

T = int(input())

total = 0
line = []

for _ in range(T):
    N = int(input())

    arr = list(map(int, input().split()))

    start = 0
    end = 0
    value = 0

    max_value = -INF
    max_start = 0
    max_end = 0

    while end<N:
        value += arr[end]

        if value> max_value or (value == max_value and max_end - max_start > end-start):
            max_value = value
            max_start = start
            max_end = end

        if value <=0:
            start = end+1
            value = 0
        end+=1

    total += max_value
    line.append([max_start+1, max_end+1])

print(total)
for i in line:
    print(*i)