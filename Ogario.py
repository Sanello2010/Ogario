import pygame
from random import randint
from math import sin, cos
from time import time

#class Food:

#    def __init__(self, ):

pygame.init()
pygame.font.init()
sizeshow = (800, 600)
screen = pygame.display.set_mode(sizeshow)

bg = pygame.Surface(sizeshow)
bg.fill((255, 255, 255))
c = pygame.time.Clock()

x_p = 0
y_p = 0

x_c = 0
y_c = 0

# x_pp = 0
# y_pp = 0

R_p = 10
step = 5
origin_step = 5
d_step = int(step / (2 ** 0.5))

color = (randint(0, 250), randint(0, 250), randint(0, 250))
key_dict = {'w': False, 's': False, 'a': False, 'd': False}

food_count = 1000
food_list = []

scale = 1
myfont = pygame.font.SysFont('Comic Sans MS', 20)
score = 0

GO = True
while GO:
    if len(food_list) < food_count:
        food_list.append([(randint(-1500, 1500), randint(-1500, 1500)),
                          (randint(0, 250), randint(0, 250), randint(0, 250))])

    screen.blit(bg, (0, 0))
    pygame.draw.circle(screen, color, (x_p + 400, y_p + 300), int(R_p / scale))  # цацка заменить на x_pp  y_pp
    fat = myfont.render(str(score), False, (0, 0, 0))
    screen.blit(fat, (x_p + 395, y_p + 285))
    for f in food_list:
        dis = ((x_p - (f[0][0] + x_c)) ** 2 + (y_p - (f[0][1] + y_c)) ** 2) ** 0.5
        if dis < R_p:
            index = food_list.index(f)
            food_list[index] = None
            R_p += 1
            score += 1
            step = origin_step * (1 - (1 / (score + 1)))
            print(step)
        else:
            pygame.draw.circle(screen, f[1],
                               (int((f[0][0] + x_c) / scale) + 400,
                                int((f[0][1] + y_c) / scale) + 300), int(4 / scale))

    food_list = [i for i in food_list if i]

    pygame.display.update()
    c.tick(60)

    for eventy in pygame.event.get():
        if eventy.type == pygame.QUIT:
            pygame.quit()
            GO = False
            break

        if eventy.type == pygame.KEYDOWN:
            if eventy.dict['key'] == pygame.K_ESCAPE:
                pygame.quit()
                GO = False
                break

            if eventy.dict['key'] == pygame.K_w:
                key_dict['w'] = True
            if eventy.dict['key'] == pygame.K_s:
                key_dict['s'] = True
            if eventy.dict['key'] == pygame.K_a:
                key_dict['a'] = True
            if eventy.dict['key'] == pygame.K_d:
                key_dict['d'] = True

        if eventy.type == pygame.KEYUP:
            if eventy.dict['key'] == pygame.K_w:
                key_dict['w'] = False
            if eventy.dict['key'] == pygame.K_s:
                key_dict['s'] = False
            if eventy.dict['key'] == pygame.K_a:
                key_dict['a'] = False
            if eventy.dict['key'] == pygame.K_d:
                key_dict['d'] = False

        if eventy.type == pygame.MOUSEBUTTONDOWN:
            if eventy.button == 4:
                scale += 0.1
            if eventy.button == 5:
                if scale > 1:
                    scale -= 0.1

    if key_dict['w'] and key_dict['d']:
        y_c += d_step
        x_c -= d_step
    elif key_dict['d'] and key_dict['s']:
        y_c -= d_step
        x_c -= d_step
    elif key_dict['s'] and key_dict['a']:
        y_c -= d_step
        x_c += d_step
    elif key_dict['a'] and key_dict['w']:
        y_c += d_step
        x_c += d_step
    else:
        for key in key_dict:
            if key_dict[key]:
                if key == 'w':
                    y_c += step
                if key == 's':
                    y_c -= step
                if key == 'd':
                    x_c -= step
                if key == 'a':
                    x_c += step
    # x_pp = int(cos(time() * 20) * 50) + x_p  цацка
    # y_pp = int(sin(time() * 20) * 50) + y_p
