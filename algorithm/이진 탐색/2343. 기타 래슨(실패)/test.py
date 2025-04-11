import sys
input = sys.stdin.readline
verbose = False

N, M = map(int, input().split())
arr = list(map(int, input().split()))

sum_arr = [0]
for i in range(N):
    sum_arr.append(arr[i] +sum_arr[i])

start_num = 0
end_num = sum_arr[-1]
# iter = 0

while start_num <= end_num:
    # iter +=1
    factor = 0
    cnt = 1
    cur_num = (start_num + end_num)// 2

    for i in  range(1,N+1):
        temp = sum_arr[i] - factor
        if temp > cur_num:
            factor = sum_arr[i-1]
            cnt +=1
        if verbose:
            print(f'temp, factor, cnt : {temp, factor, cnt}')
    if verbose:
        print(f'start_num, end_num, cur_num, cnt : {start_num, end_num, cur_num, cnt}')
        print('----' * 50)

    if cnt <= M:
        end_num = cur_num -1
    else:
        start_num = cur_num +1
    # if iter >100:
    #     break
print(start_num)
