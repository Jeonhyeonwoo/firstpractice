import pygame
from random import *
#############################################################
# 기본 초기화(반드시 해야 하는 것들)
pygame.init() 

#화면크기 설정
screen_width = 480 #가로크기
screen_height = 640 #세로크기
screen = pygame.display.set_mode((screen_width,screen_height))

#화면 타이틀 설정
pygame.display.set_caption("QUIZ") 
#FPS
clock = pygame.time.Clock()
#############################################################


# 1.사용자 게임 초기화 (배경화면, 게임 이미지, 좌표, 속도, 폰트 등)
# 배경 만들기
backaground = pygame.image.load("C:/Users/전현우/Desktop/python workspace/pygame_basic/background.png")

# 캐릭터 만들기
character = pygame.image.load("C:/Users/전현우/Desktop/python workspace/pygame_basic/character.png")
character_size = character.get_rect().size #이미지의 크기를 구해옴
character_width = character_size[0] #캐릭터의 가로크기
character_height = character_size[1] #캐릭터의 새로크기
character_x_pos = (screen_width/2) - (character_width/2) #화면 가로의 절반에 해당하는 곳에 위치
character_y_pos = screen_height - character_height # 화면 세로 크기의 가장 아래에 해당하는 곳에 위치

to_x = 0
character_speed = 0.6

# 적 만들기 
enemy = pygame.image.load("C:/Users/전현우/Desktop/python workspace/pygame_basic/enemy.png")
enemy_size = enemy.get_rect().size #이미지의 크기를 구해옴
enemy_width = enemy_size[0] #캐릭터의 가로크기
enemy_height = enemy_size[1] #캐릭터의 새로크기
enemy_x_pos = randint(enemy_width, screen_width - enemy_width) #화면 가로의 절반에 해당하는 곳에 위치
enemy_y_pos = 0 # 화면 세로 크기의 가장 아래에 해당하는 곳에 위치
enemy_speed = 10

#이벤트 루프
running = True #게임이 진행중인가?
while running:
    dt = clock.tick(30) #게임화면의 초당 프레임 수를 설정 

    # 2.이벤트 처리(키보드, 마우스 등)
    for event in pygame.event.get(): 
        if event.type == pygame.QUIT: 
            running = False 

    if event.type == pygame.KEYDOWN: #키가 눌렸는지 확인 
            if event.key == pygame.K_LEFT: #캐릭터 왼쪽으로
                to_x -= character_speed
            elif event.key == pygame.K_RIGHT: #캐릭터 오른쪽으로
                to_x += character_speed

    if event.type == pygame.KEYUP: # 방향키를 때면 멈춤
            if event.key == pygame.K_LEFT or pygame.K_RIGHT:
                to_x = 0
 
    # 게임 캐릭터 위치 정의
    character_x_pos += to_x *dt

    #가로 경계값 처리 
    if character_x_pos < 0:
        character_x_pos = 0
    elif character_x_pos > screen_width - character_width:
        character_x_pos = screen_width - character_width

    enemy_y_pos += enemy_speed

    if enemy_y_pos > screen_height:
        enemy_y_pos = 0
        enemy_x_pos = randint(0, screen_width - enemy_width)
    #충동 처리를 위한 rect 정보 업데이트 
    character_rect = character.get_rect()
    character_rect.left = character_x_pos
    character_rect.top = character_y_pos

    enemy_rect = enemy.get_rect()
    enemy_rect.left = enemy_x_pos
    enemy_rect.top = enemy_y_pos

    #충돌 체크 
    if character_rect.colliderect(enemy_rect):
        print("충돌했어요")
        running = False
    
    # 화면에 그리기 
    screen.blit(backaground, (0,0)) #배경그리기 
    screen.blit(character, (character_x_pos,character_y_pos)) #캐릭터 그리기 
    screen.blit(enemy, (enemy_x_pos,enemy_y_pos)) #enemy 캐릭터 그리기 

    #타이머 집어 넣기 
    #경과 시간 계산
    
    pygame.display.update()         

pygame.quit() 