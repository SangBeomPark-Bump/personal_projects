import sys
input = sys.stdin.readline
verbose = False

K, N = map(int, input().split())
arr = [int(input()) for _ in range(K)]

end_num = sum(arr)// N
start_num = 1 

while start_num <= end_num:
    cur_sum = 0
    cur_num = (start_num + end_num)//2
    if verbose:
        print(start_num, end_num, cur_num)
    for i in arr:
        cur_sum += i//cur_num
    if cur_sum < N:
        end_num = cur_num - 1
    else:
        start_num = cur_num +1
    if verbose:
        print(cur_sum)
        print('-' * 40)

print(end_num)