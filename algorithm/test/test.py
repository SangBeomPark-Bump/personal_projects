import sys
input = sys.stdin.readline

t = int(input())

arr_p =  [int(input()) for _ in range(t)]

for i in arr_p:
    if i == 1:
        print('1')
    else:
        if i %2 == 0:
            print(-1)
        else:
            print(' '.join(['1', f'{i}'] + list(map(str, range(2, i)))))