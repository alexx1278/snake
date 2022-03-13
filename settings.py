import pygame
pygame.init()
white = (255, 255, 255)
yellow = (255, 255, 102)
black = (0, 0, 0)
red = (213, 50, 80)
green = (0, 255, 0)
blue = (50, 153, 213)
#Розмеры окна игры, должно быть кратно 100
dis_width = 800
dis_height = 600
dis = pygame.display.set_mode((dis_width, dis_height))
pygame.display.set_caption('Игра Змейка, Даник учится')
clock = pygame.time.Clock()
pygame.mixer.music.load('./music/fount.mp3')
pygame.mixer.music.set_volume(0.3)
pygame.mixer.music.play()
sound1 = pygame.mixer.Sound('./music/am.mp3')
snake_block = 10
snake_speed = 10
font_style = pygame.font.SysFont("bahnschrift", 25)
score_font = pygame.font.SysFont("comicsansms", 35)
f = open('top_skore','r')
top_score = int(f.read())
f.close()