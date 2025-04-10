import sys
input = sys.stdin.readline
verbose = False

N = int(input())
arr =  list(map(int, input().split()))

start = 0
end = N-1

opt_num = arr[start] + arr[end]
opt_start = start
opt_end = end

iter = 0
while True :
    iter +=1
    temp_num = arr[start] + arr[end]
    if verbose:
        print(f'iter : {iter}, start : {start}, end: {end}, temp_num : {temp_num}')

    if abs(temp_num) <= abs(opt_num):
        opt_start = start
        opt_end = end
        opt_num = temp_num
    if temp_num <0:
        start +=1
    elif temp_num >0:
        end -=1
    else:
        break
    if start == end:
        break

print(arr[opt_start], arr[opt_end])