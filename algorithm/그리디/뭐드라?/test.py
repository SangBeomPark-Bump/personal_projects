import sys
input = sys.stdin.readline

N = int(input())
intervals = [tuple(map(int, input().split())) for _ in range(N)]

# 1) 끝나는 시간 기준 오름차순 정렬
intervals.sort(key=lambda x: x[1])

count = 0
current_end = 0

# 2) 그리디 선택
for start, end in intervals:
    if start >= current_end:
        count += 1
        current_end = end

print(count)
