import sys
input = sys.stdin.readline
verbose = False
verboses = [True for _ in range(10)]

N, y, x = map(int, input().split())


ans = 0
def recursive(N, x, y):
    global ans
    if N == 0:
        return
    the_number =  (2 ** (N-1))
    temp = ((y // the_number) * 2 + (x // the_number )) * (the_number ** 2)
    ans += temp
    # print(f'the_number = {the_number}, x {x}, y {y}, temp {temp}, ans {ans}')
    recursive(N-1, x%the_number, y%the_number)

recursive(N, x, y)
print(ans)
