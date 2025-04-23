import sys
input = sys.stdin.readline
verbose = False
verboses = [False for _ in range(10)]



prob = input()
N = len(prob)

def is_pelindrom(string):
    len_str = len(string)
    a = string[:len_str//2]
    if len_str %2 ==0:
        b = string[len_str//2:]
    else:
        b = string[(len_str//2)+1:]
    return a == b[::-1]


# for i in arr:
#     print(i)