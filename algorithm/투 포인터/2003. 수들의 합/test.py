import sys
input = sys.stdin.readline
verbose = False

N, M = map(int, input().split())
arr =  list(map(int, input().split())) + [0]

start = 0
end = 0

sum = arr[end]
result = 0

iter = 0
while start != N and end != N:
    iter +=1
    if sum < M:
        end +=1
        sum += arr[end]
    elif sum > M :
        sum -= arr[start]
        start +=1
    else:
        result +=1
        end +=1
        sum +=arr[end]
    if verbose:
        print(f'start: {start}, end : {end}, sum : {sum}')
        print('-' * 100)
if verbose:
    print(f'반복횟수 : {iter}')
print(result)