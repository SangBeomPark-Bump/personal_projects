import sys
input = sys.stdin.readline
verbose = False
verboses = [False for _ in range(10)]


T = int(input())

INF = int(1e9)

def belman():
    N, M, W= map(int, input().split())

    arr_m = [list(map(int, input().split() ) ) for _ in range(M)]
    arr_m2 =  [(b, a, c) for a, b, c in arr_m]
    arr_w = [list(map(int, input().split() ) ) for _ in range(W)]
    arr_w = [ (a, b, -c) for a, b, c in arr_w]
    arr = arr_m + arr_m2+ arr_w
    dist = [INF] * (N+1)
    dist[1] = 0
    for i in range(1, N+1):
        for cur_loc, end_loc, spent_time in arr:
            next_dist = dist[cur_loc] + spent_time
            if dist[end_loc] > next_dist :
                dist[end_loc] = next_dist
                if i == N:
                    print("YES")
                    return
    print("NO")

for _ in range(T):
    belman()
