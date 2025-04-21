import sys
input = sys.stdin.readline
verbose = False
verboses = [False for _ in range(10)]


N, M = map(int, input().split())
arr = [list(map(int, input().split() ) ) for _ in range(M)]


INF = int(1e9)
money_arr = [ [-INF, -1] for _ in range(N+1) ]
money_arr[1][0] = 0
check = True

for i in range(N):
    for start_loc, end_loc, money_gained in arr:
        cur_money = money_arr[start_loc][0] + money_gained

        if money_arr[end_loc][0] < cur_money :
            money_arr[end_loc][0] = cur_money
            money_arr[end_loc][1] = start_loc
            if i == N-1:
                check = False
                break

answer = []

def recursive(n):
    global answer
    answer.append(n)
    if not check:
        return [-1]
    if n == 1:
        return True
    if n == -1:
        return False
    _, nextn = money_arr[n]
    if not recursive(nextn):
        return [-1]
    return answer

print(*recursive(N)[::-1])