# 코드 트리 - 핀볼 게임 1-> / 2-> \ 모양임
# 변수 선언 및 입력:

n = int(input())
grid = [
    list(map(int, input().split()))
    for _ in range(n)
]


def in_range(x, y):
    return 0 <= x and x < n and 0 <= y and y < n


def calc(x, y, move_dir):
    dxs, dys = [-1, 1, 0, 0], [0, 0, -1, 1]
	# 1번 블럭에서는 방향이 다음과 같이 변합니다 : 0<->3 1<->2
	# 2번 블럭에서는 방향이 다음과 같이 변합니다 : 0<->2 1<->3
    
    elapsed_time = 1
    
    while in_range(x, y):
        if grid[x][y] == 1:
            move_dir = 3 - move_dir
        elif grid[x][y] == 2:
            move_dir = (move_dir + 2) if move_dir < 2 else (move_dir - 2)
        
        x, y = x + dxs[move_dir], y + dys[move_dir]
        elapsed_time += 1
    
    return elapsed_time


# 각각의 상하좌우 방향에 대해
# 가능한 모든 위치에서 걸리는 시간을 계산한 후,
# 그 중 최댓값을 구합니다.
ans = 0
for i in range(n):
    ans = max(ans, calc(n - 1, i, 0))
    ans = max(ans, calc(0, i, 1))
    ans = max(ans, calc(i, n - 1, 2))
    ans = max(ans, calc(i, 0, 3))
	
print(ans)