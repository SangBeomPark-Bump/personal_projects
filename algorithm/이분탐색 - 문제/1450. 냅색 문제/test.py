import sys
input = sys.stdin.readline
INF = float("inf")


N, C = map(int, input().split())
arr = list(map(int, input().split()))
A = arr[:N//2]
B = arr[N//2:]

sums_a = [0]
sums_b = [0]

for a in A:
    cur_len_sums = len(sums_a)

    for i in range(cur_len_sums):
        prev_sum = sums_a[i]
        sums_a.append(a + prev_sum)

for b in B:
    cur_len_sums = len(sums_b)

    for i in range(cur_len_sums):
        prev_sum = sums_b[i]
        sums_b.append(b + prev_sum)

sums_b.sort()

ans = 0

for a in sums_a:
    start = 0
    end = len(sums_b) - 1
    c = C - a
    
    result = len(sums_b)

    while start <= end :
        mid = (start + end) // 2

        if sums_b[mid] <= c :
            start = mid + 1

        elif sums_b[mid] > c  :
            result = mid
            end = mid - 1

    ans += result 

print(ans)