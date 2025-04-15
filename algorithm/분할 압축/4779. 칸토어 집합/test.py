import sys
input = sys.stdin.readline
verbose = False
verboses = [True for _ in range(10)]

while True:
    try:
        N = int(input())
        def cantore(n : int = N):
            if n == 0:
                return '-'
            tn = 3 ** (n - 1)
            return cantore(n-1) + ' ' * tn + cantore(n-1)

        cantore(N)
        print(cantore(N))
    except :
        break