import sys
input = sys.stdin.readline
verbose = False

N = int(input())
arr = list(map(int, input().split()))


factor =  -1 + (int(arr[0] <= arr[-1]))*2
arr = arr[::factor]

sum_arr = [0]
for i in arr:
    sum_arr.append(sum_arr[-1] + i)

sum_arr = sum_arr[1:]
end_hoeny = sum_arr[-1]

max_hoeny = -1
if verbose:
    print(arr)
    print(sum_arr)

for i in range(1, N-1):
    temp_hoeny_start = end_hoeny - arr[-1] - arr[i] + sum_arr[i-1]
    temp_hoeny_end = end_hoeny * 2 - arr[i] - sum_arr[i] - arr[0]
    temp_hoeny_middle = sum_arr[i] + sum_arr[-1] - sum_arr[i-1] - arr[-1] -arr[0]

    if verbose:
        print(f'arr : {arr[i]}')
        print(f'cumsum : {sum_arr[i]}')
        print(f'temp_hoeny_start : {temp_hoeny_start}')
        print(f'temp_hoeny_end : {temp_hoeny_end}')
        print(f'temp_hoeny_middle : {temp_hoeny_middle}')
        print('-' * 50)
    max_hoeny = max(temp_hoeny_end, temp_hoeny_middle, temp_hoeny_start, max_hoeny)

print(max_hoeny)