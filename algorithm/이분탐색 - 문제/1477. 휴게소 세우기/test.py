import sys
input = sys.stdin.readline
INF = float("inf")


N, M, L = map(int, input().split())

arr = []
arr = list(map(int, input().split()))
arr.sort()

def calc(x):
    temp = 0
    aridx = 0

    result = 0
    for n in range(1, L):
        temp +=1
        if aridx < N:
            if n == arr[aridx]:
                temp = 0
                aridx += 1
        
        if temp == x:
            result +=1
            temp = 0
    
    return result

start = 1
end = L - 1

result = 0
while start <= end:
    mid = (start + end) // 2

    cur_x = calc(mid)
    if cur_x <= M:
        end = mid - 1
    else :
        start = mid + 1

    if cur_x == M:
        result = mid
    
        

print(result)