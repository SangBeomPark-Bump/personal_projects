import sys
input = sys.stdin.readline
verbose = False
verboses = [False for _ in range(10)]

N = int(input())

X = 0

def check(number):
    global X
    return (X & 1<<number-1)

def test(input_str):
    global X
    if input_str == 'empty':
        X = 0 
    elif input_str == 'all':
        X = (2**20-1)
    else:
        com, number = tuple(input_str.split())
        number = int(number)
        if com == 'add' and not check(number):
            X += (1<< number-1)
        elif com == 'remove' and check(number):
            X -= (1<< number-1)
        elif com == 'check':
            print(1 if check(number) else 0)
        elif com == 'toggle':
            X += (-(1<< number-1)) if check(number) else (1<<number-1)


for i in range(N):
    test(input().strip('\n'))