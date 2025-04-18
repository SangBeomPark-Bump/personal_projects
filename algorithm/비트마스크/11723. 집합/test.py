import sys
input = sys.stdin.readline
verbose = False
verboses = [False for _ in range(10)]

N = int(input())

S = set()
def test(input_str):
    global S
    if input_str == 'empty':
        S = set()
    elif input_str == 'all':
        S = set(range(1, 21))
    else:
        com, number = tuple(input_str.split())
        number = int(number)
        if com == 'add':
            S.add(number)
        elif com == 'remove' and number in S:
            S.remove(number)
        elif com == 'check':
            print(int( number in S ))
        elif com == 'toggle':
            S.add(number) if number not in S else S.remove(number)

for i in range(N):
    test(input().strip('\n'))