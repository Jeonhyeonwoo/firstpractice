n,m,q = map(int,input().split())
arr = [list(map(int,input().split())) for _ in range(n)]

def move_left(row):
    tmp = 0
    if m!= 1:
        for i in range(m):
            if i == 0:
                tmp = arr[row][i]
                arr[row][i] = arr[row][i+1]
            elif i == m-1:
                arr[row][i] = tmp
            else:
                arr[row][i] = arr[row][i+1]

def move_right(row):
    tmp = 0
    if m!= 1:
        for i in range(m-1,-1,-1):
            if i == m-1:
                tmp = arr[row][i]
                arr[row][i] = arr[row][i-1]
            elif i == 0:
                arr[row][i] = tmp
            else:
                arr[row][i] = arr[row][i-1]

def check_up(row): 
    for i in range(m):
        if arr[row][i] == arr[row-1][i]:
            return True
    return False

def check_down(row):
    for i in range(m):
        if arr[row][i] == arr[row+1][i]:
            return True
    return False

def spread(row,v):
    if v == 'L':
        move_left(row)
    else:
        move_right(row)
    

for _ in range(q):
    r,cmd = input().split()
    r = int(r) - 1
    row_down,row_up = r,r
    cmd_down,cmd_up = cmd,cmd
    if cmd == 'L':
        move_right(r)
        if r<n-1:
            while row_down<n-1:
                if check_down(row_down):
                    spread(row_down+1,cmd_down)
                    row_down +=1
                    if cmd_down == 'L':
                        cmd_down = 'R'
                    else:
                        cmd_down = 'L'
                else:
                    break
        if r>0:
            while row_up>0:
                if check_up(row_up):
                    spread(row_up-1,cmd_up)
                    row_up-=1
                    if cmd_up == 'L':
                        cmd_up = 'R'
                    else:
                        cmd_up = 'L'
                else:
                    break
    else:
        move_left(r)
        if r<n-1:
            while row_down<n-1:
                if check_down(row_down):
                    spread(row_down+1,cmd_down)
                    row_down +=1
                    if cmd_down == 'L':
                        cmd_down = 'R'
                    else:
                        cmd_down = 'L'
                else:
                    break
        if r>0:
            while row_up>0:
                if check_up(row_up):
                    spread(row_up-1,cmd_up)
                    row_up-=1
                    if cmd_up == 'L':
                        cmd_up = 'R'
                    else:
                        cmd_up = 'L'
                else:
                    break

for i in arr:
    print(*i)