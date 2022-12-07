import pygame
import sys
import random


class pipe:
    def create_pipe():
        random_pipe_position = random.choice(pipe_height)
        bottom_pipe = pipe_surface.get_rect(midtop=(700, random_pipe_position))
        top_pipe = pipe_surface.\
            get_rect(midbottom=(700, random_pipe_position - 300))
        return bottom_pipe, top_pipe

    def move_pipes(pipes):
        for pipe in pipes:
            pipe.centerx -= 5
        return pipes

    def draw_pipes(pipes):
        for pipe in pipes:
            if pipe.bottom >= 1024:
                screen.blit(pipe_surface, pipe)
            else:
                flip_pipe = pygame.transform.flip(pipe_surface, False, True)
                screen.blit(flip_pipe, pipe)

    def check_collision(pipes):
        for pipe in pipes:
            if bird_rectangle.colliderect(pipe):
                death_sound.play()
                return False

        if bird_rectangle.top <= 100 or bird_rectangle.bottom >= 900:
            return False

        return True


class bird:
    def rotate_bird(bird):
        new_bird = pygame.transform.rotozoom(bird, -bird_movement * 3, 1)
        return new_bird

    def bird_animation():
        new_bird = bird_frames[bird_index]
        new_bird_rectangle = \
            new_bird.get_rect(center=(100, bird_rectangle.centery))
        return new_bird, new_bird_rectangle


def score_display(game_state):
    if game_state == 'main_game':
        score_surface = \
            game_font.render(f'Score: {int(score)}', True, (0, 0, 139))
        score_rectangle = score_surface.get_rect(center=(288, 100))
        screen.blit(score_surface, score_rectangle)

    if game_state == 'game_over':
        font_score_surface = \
            game_font.render(f'Your score: {int(score)}',
                             False, (135, 206, 235), (255, 255, 255))
        font_score_rectangle = font_score_surface.get_rect(center=(288, 230))
        high_score_surface = \
            game_font.render(f'High Score: {int(high_score)}',
                             True, (30, 144, 255), (255, 255, 255))
        high_score_rectangle = high_score_surface.get_rect(center=(288, 185))
        screen.blit(high_score_surface, high_score_rectangle)
        screen.blit(font_score_surface, font_score_rectangle)


def update_score(score, high_score):
    if score > high_score:
        high_score = score
    return high_score


def background(score):
    global changed
    global background_surface
    if 5 <= score < 10 and changed != 2:
        background_surface = pygame.image.load('assets/b4.png').convert()
        background_surface = pygame.transform.scale2x(background_surface)
        changed = 2
    if 15 > score >= 10 and changed != 3:
        background_surface = pygame.image.load('assets/b3.png').convert()
        background_surface = pygame.transform.scale2x(background_surface)
        changed = 3
    if 20 > score >= 15 and changed != 4:
        background_surface = pygame.image.load('assets/b5.png').convert()
        background_surface = pygame.transform.scale2x(background_surface)
        changed = 4
    if score >= 20 and changed != 5:
        background_surface = pygame.image.load('assets/b1.png').convert()
        background_surface = pygame.transform.scale2x(background_surface)
        changed = 5

    elif score < 5 and changed != 1:
        background_surface = pygame.image.load('assets/b2.png').convert()
        background_surface = pygame.transform.scale2x(background_surface)
        changed = 1


pygame.mixer.pre_init(frequency=44100, size=16, channels=10, buffer=512)
pygame.init()

screen = pygame.display.set_mode((576, 1024))
clock = pygame.time.Clock()
game_font = pygame.font.Font('assets/04B_19.TTF', 40)

gravity = 0.25
bird_movement = 0
game_active = True
score = 0
high_score = 0
font_score = score

background_surface = pygame.image.load('assets/b2.png').convert()
background_surface = pygame.transform.scale2x(background_surface)
changed = 1

bird_downflap = pygame.transform.scale2x(pygame.image.load
                                         ('assets/bluebird-midflap.png').
                                         convert_alpha())
bird_midflap = pygame.transform.scale2x(pygame.image.load
                                        ('assets/bluebird-midflap.png').
                                        convert_alpha())
bird_upflap = pygame.transform.scale2x(pygame.image.load
                                       ('assets/bluebird-midflap.png').
                                       convert_alpha())
bird_frames = [bird_downflap, bird_midflap, bird_upflap]
bird_index = 0
bird_surface = bird_frames[bird_index]
bird_rectangle = bird_surface.get_rect(center=(100, 512))

BIRDFLAP = pygame.USEREVENT

bird_surface = pygame.image.load('assets/bluebird-midflap.png').\
    convert_alpha()
bird_surface = pygame.transform.scale2x(bird_surface)
bird_rectangle = bird_surface.get_rect(center=(100, 512))

pipe_surface = pygame.image.load('assets/pipe-green.png')
pipe_surface = pygame.transform.scale2x(pipe_surface)
pipe_list = []
SPAWNPIPE = pygame.USEREVENT
pygame.time.set_timer(SPAWNPIPE, 1000)
pipe_height = range(400, 800, 50)

game_over_surface = pygame.transform.\
    scale2x(pygame.image.load('assets/message.png').convert_alpha())
game_over_rectangle = game_over_surface.get_rect(center=(288, 512))

flap_sound = pygame.mixer.Sound('sound/sfx_wing.wav')
death_sound = pygame.mixer.Sound('sound/sfx_hit.wav')
score_sound = pygame.mixer.Sound('sound/sfx_point.wav')
score_sound_countdown = 100

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT or \
                (event.type == pygame.KEYDOWN and
                 event.key == pygame.K_ESCAPE):
            pygame.quit()
            sys.exit()

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE and game_active:
                bird_movement = 0
                bird_movement -= 8
                flap_sound.play()
            if event.key == pygame.K_SPACE and game_active is False:
                game_active = True
                pipe_list.clear()
                bird_rectangle.center = (100, 512)
                bird_movement = 0
                score = 0

        if event.type == SPAWNPIPE:
            pipe_list.extend(pipe.create_pipe())

        if event.type == BIRDFLAP:
            if bird_index < 2:
                bird_index += 1
            else:
                bird_index = 0

            bird_surface, bird_rectangle = bird.bird_animation()

    screen.blit(background_surface, (0, 0))

    if game_active:
        bird_movement += gravity
        rotated_bird = bird.rotate_bird(bird_surface)
        bird_rectangle.centery += bird_movement
        screen.blit(rotated_bird, bird_rectangle)
        game_active = pipe.check_collision(pipe_list)

        pipe_list = pipe.move_pipes(pipe_list)
        pipe.draw_pipes(pipe_list)

        score += 0.007
        score_display('main_game')
        score_sound_countdown -= 1
        background(score)

        if score_sound_countdown <= 0:
            score_sound.play()
            score_sound_countdown = 100

    else:
        screen.blit(game_over_surface, game_over_rectangle)
        high_score = update_score(score, high_score)
        score_display('game_over')

    pygame.display.update()
    clock.tick(120)

    
