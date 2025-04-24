import sys
input = sys.stdin.readline
verbose = False
verboses = [False for _ in range(10)]

N = int(input())

arr_t = [0]
arr_e = [[]]


for start in range(N):
    time, *arr, _ = map(int, input().split())
    arr_t.append(time)
    arr_e.append(arr)



arr_s = [[] for _ in range(N+1)] 
for end in range(1, N+1):
    for start in arr_e[end]:
        arr_s[start].append(end)


from collections import deque

arr_d = [len(arr) for arr in arr_e]
que = deque()


ans = [ 0 for _ in range(N+1)]

for building in range(1, N+1):
    if arr_d[building] == 0:
        que.append(building)
    ans[building] = arr_t[building]

while que:
    cur_building = que.popleft()
    cur_time = arr_t[building]
    for next_building in arr_s[cur_building]:
        arr_d[next_building] -=1
        ans[next_building] = max(ans[next_building] , ans[cur_building] + arr_t[next_building])
        if arr_d[next_building] == 0:
            que.append(next_building)


for i in ans[1:]:
    print(i)