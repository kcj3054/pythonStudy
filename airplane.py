import sys
from random import randint


pygame.init()
#키설정

VIEW = pygame.display.set_mode((800, 600))
FPS = pygame.time.Clock()


def main():
    blocks = 80
    pos_y = 250
    speed = 0
    score = 0
    grt = randint(1, 6)
    sysfont = pygame.font.SysFont(None, 36)
    char_image = pygame.image.load("car.PNG")
    maps[]  # 블럭 저장하기 위한 리스트 

    for xpos in range(blocks):                     #80개의 블록을 추가 해 놓는다 
        maps.append(Rect(xpos * 10, 100, 10, 400)) #왼쪽, 위쪽, 너비, 높이 
    end = False

    while True:
        is_space_down = False
        for event in pygame.event.get():   #윈도우 창을 띄우는 부분
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == KEYDOWN:
                if event.key == k_SPACE:
                    is_space_down = True

        if not end:
            score += 10
            speed += 3 if is_space_down else 3
            pos_y += speed

            edge = maps[-1].copy()
            test = edge.move(0, grt)  #맵을 이동시킨다 , x축은 0, y축은 grt만큼 이동 

            if test.top <= 0 or test.bottom >= 600:  #맵을 생성하는 부분,   범위를 초과한 것 아닌가 ?  ? ??  ?  ,,, 600이라는 것은 바닥에 닿았다는 것이다
                grt = randint(1, 6) * (-1 if grt > 0 else 1)
                edge.inflate_ip(0, -20)  # inflate_ip 호출한 대상의 크기를 늘이거나 줄인다 (x, y)
            edge.move_ip(10, grt)
            maps.append(edge)
            del maps[0] #앞 map를 지우고 다시 생성, 지우는 부분 
            maps = [x.move(-10, 0) for x in maps]

            if maps[0].top > pos_y or maps[0].bottom < pos_y + 80:   #충돌처리 
                end = True


        VIEW.fill((0, 50, 50))   #배경의 색깔을 나타나낸다 
        for mp in maps:
            pygame.draw.rect(VIEW, (0, 0, 0), mp)
        VIEW.blit(char_image, (0, pos_y)) # char_iamge를 0, pos_y에 그려준다 

        score_image = sysfont.render("score: []".format(score), True, (255, 255, 255))
        VIEW.blit(score_image, (600, 20))  # blit 화면에 뿌려준다 

        pygame.display.update()
        FPS.tick(15)    #

if __name__ == "__main__":
    main()
    
            
            