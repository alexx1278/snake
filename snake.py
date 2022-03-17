# описание тут https://pythonist.ru/zmejka-na-python/
'''
Необходимые доработки:
3. Квадратики заменить картинками
7. Реализовать паузу
'''

import random
import time
from settings import *


def Your_score(score):
    value = score_font.render("Очки: " + str(score), True, yellow)
    dis.blit(value, [0, 0])

def Top_score(score):
    value = score_font.render("Лучший результат: " + str(score), True, yellow)
    dis.blit(value, [400, 0])


def messagetime(sec):
    value = score_font.render("Осталось времени: " + str(sec), True, yellow)
    dis.blit(value, [0, 570])


def our_snake(snake_block, snake_list):
    for x in snake_list:
        pygame.draw.rect(dis, black, [x[0], x[1], snake_block, snake_block])


def message(msg, color, poz):
    mesg = font_style.render(msg, True, color)
    dis.blit(mesg, [(dis_width / 6) , (dis_height / 3) + poz])


def gameLoop(top_score):
    game_over = False
    game_close = False

    x1 = dis_width / 2
    y1 = dis_height / 2

    x1_change = 0
    y1_change = 0

    snake_List = []
    Length_of_snake = 1
    superFood = 0
    dop_score = 0

    foodx = round(random.randrange(0, dis_width - snake_block) / 10.0) * 10.0
    foody = round(random.randrange(20, dis_height - snake_block) / 10.0) * 10.0

    while not game_over:

        while game_close == True:
            dis.fill(blue)
            pygame.mixer.music.pause()
            Your_score(Length_of_snake + dop_score - 1)
            Top_score(top_score)
            score = Length_of_snake + dop_score - 1
            if score > top_score:
                top_score = score
                f = open('top_skore', 'w')
                f.write(str(top_score))
                f.close()
                message(f"Ты побил рекорд! Новый рекорд: {top_score}", red, 0)
                pygame.display.update()
                time.sleep(5)
            message("Ты проиграл!", red, -15)
            message("Нажми С-чтобы играть сначала или Q-чтобы выйти", red, 15)
            pygame.display.update()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    game_over = True
                    game_close = False
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        game_over = True
                        game_close = False
                    if event.key == pygame.K_c:
                        pygame.mixer.music.unpause()
                        gameLoop(top_score)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    x1_change = -snake_block
                    y1_change = 0
                elif event.key == pygame.K_RIGHT:
                    x1_change = snake_block
                    y1_change = 0
                elif event.key == pygame.K_UP:
                    y1_change = -snake_block
                    x1_change = 0
                elif event.key == pygame.K_DOWN:
                    y1_change = snake_block
                    x1_change = 0
        if x1 >= dis_width or x1 < 0 or y1 >= dis_height or y1 < 0:
            game_close = True
        x1 += x1_change
        y1 += y1_change
        dis.fill(blue)
        pygame.draw.rect(dis, green, [foodx, foody, snake_block, snake_block])
        snake_Head = []
        snake_Head.append(x1)
        snake_Head.append(y1)
        snake_List.append(snake_Head)
        if len(snake_List) > Length_of_snake:
            del snake_List[0]

        for x in snake_List[:-1]:
            if x == snake_Head:
                game_close = True

        our_snake(snake_block, snake_List)
        Your_score(Length_of_snake + dop_score - 1)
        Top_score(top_score)
        if superFood >= 10:
            if ras == 1:
                start_time = time.time() + 20
                superFoodx = round(random.randrange(0, dis_width - snake_block) / 10.0) * 10.0
                superFoody = round(random.randrange(20, dis_height - snake_block - 30) / 10.0) * 10.0
                ras = 0
            if (start_time - time.time()) >= 0:
                sec = int(start_time - time.time())
                messagetime(sec)
            if sec <= 0:
                superFood = 0

            pygame.draw.rect(dis, red, (superFoodx, superFoody, snake_block, snake_block))
            if x1 == superFoodx and y1 == superFoody:
                sound1.play()
                superFood = 0
                dop_score += 50
        pygame.display.update()

        if x1 == foodx and y1 == foody:
            foodx = round(random.randrange(0, dis_width - snake_block) / 10.0) * 10.0
            foody = round(random.randrange(20, dis_height - snake_block - 30) / 10.0) * 10.0
            sound1.play()
            Length_of_snake += 1
            superFood += 1
            ras = 1

        clock.tick(snake_speed)

    pygame.quit()
    quit()


gameLoop(top_score)
