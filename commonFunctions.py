### Common Functions Here

import pygame
import pygame.freetype

from commonSettings import *

# WORK IN PROGRESS of KEYBOARD CLASS
class Keyboard:
    def __init__(self):
        self.key = "10"

    def read(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    exit()
                else:
                    if event.type == pygame.KEYDOWN:
                        self.key = event.unicode
                        # Return: key
                    else:
                        # Return: key
                        break


def react_on_answer(sc, result_bul, score):

    font_result = pygame.font.Font(None, 50)

    if result_bul:
        result_yes_text = font_result.render(str("ПРАВИЛЬНО"), True, GREEN)
        tx = result_yes_text.get_width()
        ty = result_yes_text.get_height()
        tx0 = HALF_W - tx / 2
        ty0 = HALF_H + ty / 2 + 20
        sc.blit(result_yes_text, (tx0, ty0))
        print("CORRECT:", score)
    else:
        result_no_text = font_result.render(str("ОШИБКА"), True, RED)
        tx = result_no_text.get_width()
        ty = result_no_text.get_height()
        tx0 = HALF_W - tx / 2
        ty0 = HALF_H + ty / 2 + 20
        sc.blit(result_no_text, (tx0, ty0))
        print("WRONG:", score)

    pass


def print_text(sc, message, coords, font_color=(0,0,0), font_size=30, font_type=None):

    message = str(message)

    # font_type = pygame.font.Font(font_type, font_size)
    # text_surface = font_type.render(message, True, font_color).convert_alpha()
    # text_rect = text_surface.get_rect(topleft=coords)
    # sc.blit(text_surface, text_rect, special_flags=pygame.BLEND_PREMULTIPLIED)

    ff_font = pygame.freetype.Font(font_type, font_size)
    ff_text_rect = ff_font.render_to(sc, coords, message, font_color)


def react_on_round_end(sc, score):

    print_text(sc, "Ваш счет записан: " + str(score), (HALF_W - 100, HALF_H), RED, 30)
    pygame.display.update()
    pygame.time.delay(1500)

    pass


def update_standard_counter_progress(started_timer, counter_max, is_counter_active=True, growing_type=False):
    """
    ticks counter from MAX to ZERO (growing_type=False) or ZERO to MAX (growing_type=True)\n
    returns PROGRESS as %, Current Value in Seconds, and counter IS_ACTIVE state
    """
    counter_progress = 0
    counter = 0
    if counter_max:
        if is_counter_active:
            counter_delta = (pygame.time.get_ticks() - started_timer) / 1000
            counter = counter_max - counter_delta
            if counter < 0:  # If Bonus Counter runs out, reset counter and wait until new task generation
                is_counter_active = False
            counter_progress = counter / counter_max
    if growing_type:
        counter_progress = 1 - counter_progress

    return counter_progress, counter, is_counter_active
