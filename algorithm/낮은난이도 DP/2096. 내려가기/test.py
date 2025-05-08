
N = int(input())

arr = [list(map(int, input().split() ) ) for _ in range(N)]

dp = [ [i,i] for i in arr[0]]

dpmax = arr[0][::]
dpmin = arr[0][::]


for n in range(1, N):
    amax, bmax, cmax =  dpmax
    amin, bmin, cmin =  dpmin
    for i in range(3):
        tempmax = bmax
        tempmin = bmin
        if i >0:
            tempmax = max(cmax, tempmax)
            tempmin = min(cmin, tempmin)

        if i<2:
            tempmax = max(tempmax, amax)
            tempmin = min(tempmin, amin)

        dpmax[i] = arr[n][i] + tempmax
        dpmin[i] = arr[n][i] + tempmin

print(max(dpmax), min(dpmin))