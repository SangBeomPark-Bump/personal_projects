import sys
input = sys.stdin.readline
verbose = False
verboses = [False for _ in range(10)]

N = int(input())

arr = [ list(input().strip('\n')) for _ in range(N)]



arr_row_reduced = [[-1 for _ in range(N)] for _ in range(N)]
arr_column_reduced = [[-1 for _ in range(N)] for _ in range(N)]

for column in range(N):
    for row in range(1, N-1):
        center = arr[row][column]
        up = arr[row+1][column]
        down =  arr[row-1][column]
        arr_row_reduced[row][column] = -1 if center == '1' or up == '1' or down == '1' else 0
        if center == "B" and up == "B"  and down == "B":
            start = (row, column)
            is_stand = True
        if center == "E" and up == "E" and down == "E":
            end = (row, column)
            is_end_stand = True

for column in range(1, N-1):
    for row in range(N):
        center = arr[row][column]
        right = arr[row][column+1] 
        left = arr[row][column-1] 
        arr_column_reduced[row][column] = -1 if center == '1' or right == '1' or left == '1' else 0
        if center == "B" and right == "B" and left == "B":
            start = (row, column)
            is_stand = False
        if center == "E" and right == "E" and left == "E":
            end = (row, column)
            is_end_stand = False



arr_can_chainge = [ [False for _ in range(N)] for _ in range(N)]
for row in range(1, N-1):
    for column in range(1, N-1):
        check = True
        for dy in (-1, 0, 1):
            for dx in (-1, 0, 1):
                if arr[ row + dy][ column+ dx] == '1':
                    check = False
        if check:
            arr_can_chainge[row][column] = True


from collections import deque
def dfs(start, is_stand):
    global end, is_end_stand
    y, x = start
    que = deque()

    que.append((y, x, is_stand))

    if is_stand:
        temp = arr_row_reduced
    else:
        temp = arr_column_reduced

    temp[y][x] = 1

    while que:
        y, x, is_stand = que.popleft()
        if is_stand:
            temp = arr_row_reduced
        else:
            temp = arr_column_reduced

        if (y, x) == end and is_stand == is_end_stand:
            return(temp[y][x]-1)
        dy = (-1, 1, 0, 0)
        dx = (0, 0, -1, 1)
        cur_num = temp[y][x]
        for i in range(4):
            ny = y + dy[i]
            nx = x + dx[i]
            if not(0 <= ny < N and 0 <= nx < N):
                continue
            ### 벽이라면 거르기
            if arr[ny][nx] == -1:
                continue
            if not temp[ny][nx]:
                temp[ny][nx] = cur_num + 1 
                que.append((ny, nx, is_stand))
        if arr_can_chainge[y][x]:
            if not is_stand:
                temp = arr_row_reduced
            else:
                temp = arr_column_reduced
        if not temp[y][x]:
            temp[y][x] = cur_num + 1 
            que.append((y, x, not is_stand))
    return 0


print(dfs(start, is_stand))