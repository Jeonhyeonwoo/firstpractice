# 코드트리 숫자가 가장 큰 인접한 곳으로 동시에 이동 
# 1이하 100이상의 숫자로 이루어진 n * n 크기의 격자판 정보가 주어집니다. 
# 이때 m개 구슬이 서로 다른 위치에서 시작하여 1초에 한 번씩 상하좌우로 인접한 곳에 있는 숫자들 중 가장 큰 값이 적혀있는 숫자가 있는 위치로 동시에 이동합니다. 
# 만약 그러한 위치가 여러개 있는 경우, 상하좌우 방향 순서대로 우선순위를 매겨 가능한 곳 중 우선순위가 더 높은 곳으로 이동합니다. 
# 단, 이때 격자를 벗어나서는 안됩니다.

# 예를 들어, 다음 그림의 경우를 살펴봅시다. 
# 처음에 3개의 구슬이 각각 2행 2열, 3행 4열, 4행 2열에 놓여있었다고 생각해봅시다.
# 이때, 각 구슬이 움직인 이후의 위치가 동일하지 않다면 구슬은 절대 서로 충돌하지 않습니다.
# 하지만, 이동한 이후 2개 이상의 구슬 위치가 동일하다면, 해당 위치에 있는 구슬들은 전부 사라지게 됩니다.
# 격자판의 정보와 초기 구슬들의 위치가 주어졌을 때, t초 후 남아있는 구슬의 수를 출력하는 프로그램을 작성해보세요.

# 변수 선언 및 입력 
n,m,t = map(int,input().split()) 
arr = [list(map(int,input().split())) for _ in range(n)]
ball = [[0 for _ in range(n)] for _ in range(n)] # 공 위치 저장 
next_ball = [[0 for _ in range(n)] for _ in range(n)] # 공 위치 임시저장 

dxs,dys = [-1,1,0,0],[0,0,-1,1]

for i in range(m): # 첫 번째 공 위치 받기
    r,c = map(int,input().split())
    ball[r-1][c-1] = 1

for _ in range(t):  # t번 공 이동
    for i in range(n): # 임시저장 공간 초기화
        for j in range(n):
            next_ball[i][j] = 0

    for i in range(n):
        for j in range(n):
            max_num,max_pos = 0, (0,0)
            if ball[i][j] == 1:
                for dx,dy in zip(dxs,dys):
                    nx,ny = i + dx, j + dy
                    if 0<= nx < n and 0<= ny < n and arr[nx][ny] > max_num:
                        max_num = arr[nx][ny]
                        max_pos = (nx,ny)
                next_ball[max_pos[0]][max_pos[1]]+=1 #이동 한 곳에 공 개수 늘리기 
    
    for i in range(n):
        for j in range(n):
            ball[i][j] = next_ball[i][j] #임시저장한거 저장 

    for i in range(n):
        for j in range(n):
            if ball[i][j] >=2: #공 2개 있으면 파괴
                ball[i][j] = 0
            
cnt = 0
for i in range(n):
    for j in range(n):
        cnt += ball[i][j]

print(cnt)
    

