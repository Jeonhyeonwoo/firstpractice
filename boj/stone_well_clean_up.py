# 백트레킹 + BFS
# 돌 치워서 가장 최대 방문 만들기
from collections import deque

n,k,m = map(int,input().split()) 
grid = [list(map(int,input().split())) for _ in range(n)]
visited = [[0 for _ in range(n)] for _ in range(n)]
q = deque()
selecte_stone = []
stone_pos = []
s_pos = []
ans = 0
for i in range(n):
    for j in range(n):
        if grid[i][j]:
            stone_pos.append((i,j))

for _ in range(k):
    r,c = map(int,input().split())
    s_pos.append((r-1,c-1))

def in_range(x,y):
    return 0<= x < n and 0<= y < n

def can_go(x,y):
    return in_range(x,y) and not grid[x][y] and not visited[x][y]

def bfs():
    dxs, dys = [0,1,0,-1], [1,0,-1,0]

    while q:
        x,y = q.popleft()
        for dx,dy in zip(dxs,dys):
            nx,ny = x + dx, y + dy

            if can_go(nx,ny):
                visited[nx][ny] = 1
                q.append((nx,ny))

def calc():
    for x,y in selecte_stone:
        grid[x][y] = 0

    for i in range(n):
        for j in range(n):
            visited[i][j] = 0

    for x,y in s_pos:
        q.append((x,y))
        visited[x][y] = 1

    bfs()

    for x,y in selecte_stone:
        grid[x][y] = 1
    
    cnt = 0
    for i in range(n):
        for j in range(n):
            if visited[i][j]:
                cnt+=1
    
    return cnt


def find_max(idx,cnt):
    global ans
    if cnt == m:
        ans = max(ans,calc())
        return 

    if idx == len(stone_pos):
        return 

    
    selecte_stone.append(stone_pos[idx])
    find_max(idx+1,cnt+1)
    selecte_stone.pop()

    find_max(idx+1,cnt)

find_max(0,0)
print(ans)