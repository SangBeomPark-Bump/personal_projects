import sys
import math

sys.setrecursionlimit(int(2e6))

def four_hanoy(n):
    """
    기둥이 4개인 하노이의 탑 \n
    n : 원반의 갯수
    """

    r = 4

    if n == 1 :
        return 1

    k = n - round(math.sqrt(2 * n + 1)) + 1
    return (four_hanoy(k) * 2 + 2**(n - k) - 1) % 9901


print(four_hanoy(n=int(input())))