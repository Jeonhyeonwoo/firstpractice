import pygame
#############################################################
# 기본 초기화(반드시 해야 하는 것들)
pygame.init() 

#화면크기 설정
screen_width = 480 #가로크기
screen_height = 640 #세로크기
screen = pygame.display.set_mode((screen_width,screen_height))

#화면 타이틀 설정
pygame.display.set_caption("게임 이름") 
#FPS
clock = pygame.time.Clock()
#############################################################


# 1.사용자 게임 초기화 (배경화면, 게임 이미지, 좌표, 속도, 폰트 등)


#이벤트 루프
running = True #게임이 진행중인가?
while running:
    dt = clock.tick(60) #게임화면의 초당 프레임 수를 설정 

    # 2.이벤트 처리(키보드, 마우스 등)
    for event in pygame.event.get(): 
        if event.type == pygame.QUIT: 
            running = False 

    # 3. 게임 캐릭터 위치 정의
    
    
    # 4. 충돌 처리 

    
    # 5. 화면에 그리기 

    screen.blit(backaground, (0,0)) #배경그리기 
    screen.blit(character, (character_x_pos,character_y_pos)) #캐릭터 그리기 
    screen.blit(enemy, (enemy_x_pos,enemy_y_pos)) #enemy 캐릭터 그리기 

    #타이머 집어 넣기 
    #경과 시간 계산
    
    pygame.display.update()         

pygame.quit() 