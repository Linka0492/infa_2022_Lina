import time

import pygame
import math as m
from pygame.draw import *
from random import *


FPS = 60
screen = pygame.display.set_mode((1200, 900))


# Цвета шаров
RED = (255, 0, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)
GREEN = (0, 255, 0)
MAGENTA = (255, 0, 255)
CYAN = (0, 255, 255)
BLACK = (0, 0, 0)
LILAC = (182, 102, 210)
AMBER = (255, 191, 0)
VINOUS = (113, 25, 25)
RED_CORAL = (255, 127, 80)
BLUE_STEEL = (80, 127, 255)
LIME = (204, 255, 0)
WHITE = (255, 255, 255)
COLORS = [RED, BLUE, YELLOW, GREEN, MAGENTA, CYAN, LILAC, AMBER, VINOUS, RED_CORAL, BLUE_STEEL, LIME]


def ballz(screen: pygame.surface, n: int, x: list, y: list, velocity_x: list, velocity_y: list, r: list,
          color: list, hit: list):
    """
        Эта функция создает цели в форме кругов и обновляет их положение на экране
    Круги движутся с постоянной скоростью и отскакивают от краев экрана
    :экран параметров: Объект класса pygame.поверхность, на которой будут нарисованы шары
    :параметр n: Количество кругов
    :параметр x: Список текущих горизонтальных координат окружностей
    :параметр y: Список текущих вертикальных координат окружностей
    :параметр velocity_x: Список текущих горизонтальных скоростей окружностей
    :параметр velocity_y: Список текущих вертикальных скоростей окружностей
    :параметр r: Список радиусов окружностей
    :цвет параметра: Список цветов кругов
    :попадание параметра: список переменных bool для каждого круга, который имеет значение True, если пользователь нажал на круг
    и False, если круг не был нажат.
    Если это верно, функция обновляет все переменные текущего круга.

    """
    for i in range(n):
        # Создание переменных круга случайным образом, если на него нажали
        if hit[i]:
            r[i] = (randint(10, 100))
            x[i] = (randint(r[i], 1200 - r[i]))
            y[i] = (randint(r[i], 900 - r[i]))
            velocity_x[i] = (randint(-100, 100))
            velocity_y[i] = (randint(-100, 100))
            color[i] = (COLORS[randint(0, 11)])
            hit[i] = False
        # Рисование круга в текущем состоянии
        circle(screen, color[i], (round(x[i]), round(y[i])), r[i])
        # Обновление координат окружностей
        x[i] += velocity_x[i] * dt
        y[i] += velocity_y[i] * dt


pygame.init()


n_1 = 10 # Количество шариков на экране
#Создание списков переменных окружностей со случайными значениями
r_1 = [randint(10, 100) for i in range(n_1)]  # List of radii of circles
x_1 = [randint(r_1[i], 1200 - r_1[i]) for i in range(n_1)]  # Текущая горизонтальная координата круга
y_1 = [randint(r_1[i], 900 - r_1[i]) for i in range(n_1)]  # Текущая вертикальная координата круга
velocity_x_1 = [randint(0, 20) for i in range(n_1)]  # Текущая горизонтальная скорость круга
velocity_y_1 = [randint(0, 20) for i in range(n_1)]  # Текущая вертикальная скорость круга
color_1 = [COLORS[randint(0, 11)] for i in range(n_1)]  # Цвета кружочков
hit_1 = [False for i in
         range(n_1)]  # Список переменных bool для каждого круга, который имеет значение True, если пользователь нажал на круг,
# и False, если круг не был нажат.
dt = 0.1  # Интервал между промежутками движения шаров

score = 0  # Score of the game
c_score = pygame.font.Font(None, 32)  # Preparing for displaying the score during game
length_of_round = 20  # Length of a game in seconds

clock = pygame.time.Clock()
finished = False

while not finished:
    clock.tick(FPS)
    screen.fill(WHITE)  # Заполнение экрана белым цветом
    # Рисование кругов на текущих позициях
    ballz(screen, n_1, x_1, y_1, velocity_x_1, velocity_y_1, r_1, color_1, hit_1)


    pygame.display.update()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True
        elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            #Проверка того, нажал ли пользователь на круг, и изменение значения hit_1[i] для нажатого круга
            for i in range(n_1):
                if (event.pos[0] - x_1[i]) ** 2 + (event.pos[1] - y_1[i]) ** 2 <= r_1[i] ** 2:
                    hit_1[i] = True
                    score += 1

# Отображение результата
screen.fill(WHITE)
f_score = pygame.font.Font(None, 100)
text2 = f_score.render("Your score is: " + str(score), 1, BLACK)
screen.blit(text2, (350, 400))
pygame.display.update()
finished = False
time.sleep(1)
