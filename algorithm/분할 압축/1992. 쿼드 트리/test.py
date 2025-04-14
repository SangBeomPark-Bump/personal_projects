import sys
input = sys.stdin.readline
verbose = False
verboses = [True for _ in range(10)]

N = int(input())

arr = [list(map(int, list(input().strip('\n')))) for _ in range(N)]

def detect(arr):
    summary = 0
    width = len(arr)
    for row in arr:
        for num in row:
            summary += num
    if summary == 0:
        return 0
    if summary == width * width:
        return 1
    else:
        return -1
    
def sliceing(arr):
    width = len(arr)//2
    arr1 = [ [ number for number in row[:width] ] for row in arr[:width] ]
    arr2 = [ [ number for number in row[width:] ] for row in arr[:width] ]
    arr3 = [ [ number for number in row[:width] ] for row in arr[width:] ]
    arr4 = [ [ number for number in row[width:] ] for row in arr[width:] ]

    return arr1, arr2, arr3, arr4

def recursive_dc(arr):
    global ans
    if len(arr) == 1:
        ans += str(arr[0][0])
        return

    detection =  detect(arr)

    if detection <0:
        ans += '('
        arrs = sliceing(arr)
        for temp_arr in arrs:
            recursive_dc(temp_arr)
        ans += ')'
    else:
        ans += str(detection)

ans = ''
recursive_dc(arr)
print(ans)