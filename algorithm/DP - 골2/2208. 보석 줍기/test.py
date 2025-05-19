import sys
input = sys.stdin.readline
verbose = False
verboses = [False for _ in range(10)]
INF = float("inf")


N, M = map(int, input().split())

arr = [int(input()) for _ in range(N)]

window = [-INF for _ in range(M-1)]
temp = sum(arr[:M-1])

for n in range(M-1,N):
    temp += arr[n]
    window.append(temp)
    temp -= arr[n-M+1]

value = -INF
max_value = 0

for end in range(M-1,N):
    value = max(window[end], value)
    max_value = max(value, max_value)    
    if end <N-1:
        value += arr[end+1]

print(max_value)
