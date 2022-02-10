""" User Interface Elements module """

import pygame
import math

from commonSettings import *
from commonFunctions import print_text
from database_functions import db_get_players_scores, db_get_player_name, db_get_level_name


def active_player_selection():

    pass

def draw_user_interface_layer(sc, coords):
    """Draw UI"""

    #return ui_surface


def draw_players_score_table_for_level(sc, coords, level):
    """Draw Players Records placeholder"""

    db_result = db_get_players_scores(level)

    sx = coords[0]
    sy = coords[1]
    s_width = 230
    s_height = 200
    records_table_surface = pygame.Surface((s_width, s_height), pygame.SRCALPHA)
    records_table_surface.convert_alpha()
    record_table_rect = records_table_surface.get_rect()

    pygame.draw.rect(records_table_surface, (0,0,0), record_table_rect, 1)

    font_fixed = pygame.font.match_font('couriernew')

    print_text(records_table_surface, 'Игрок   Прошлый    Рекорд', (0, 0), BLACK, 15, font_fixed)
    print_text(records_table_surface, '-------------------------', (0, 20), BLACK, 15, font_fixed)

    y = 40
    for row in db_result:
        print_text(records_table_surface, str(row[0]), (0, y), BLACK, 15, font_fixed)
        print_text(records_table_surface, str(row[1]), (20, y), BLACK, 15, font_fixed)
        print_text(records_table_surface, str(row[2]), (100, y), BLACK, 15, font_fixed)
        print_text(records_table_surface, str(row[3]), (180, y), BLACK, 15, font_fixed)
        y += 20

    sc.blit(records_table_surface, coords)


def draw_keyboard_holder_0_9(sc, coords, mcoords, key_num_solution):

    mx, my = mcoords

    kb_width = 70
    kb_height = 70
    kb_margin = 6

    sx = coords[0]
    sy = coords[1]
    if not (sx and sy):
        sx = WIDTH / 2 - kb_width * 5 - kb_margin * 4.5
        sy = HEIGHT / 2 - kb_height
        coords = (sx, sy)

    s_width = kb_width * 10 + kb_margin * 9
    s_height = kb_height
    kb0_9_surface = pygame.Surface((s_width, s_height), pygame.SRCALPHA)
    kb0_9_surface.convert_alpha()
    kb0_9_surface_rect = kb0_9_surface.get_rect()

    pygame.draw.rect(kb0_9_surface, (0, 0, 0), kb0_9_surface_rect, 1)

    kb_font_size = 50
    font = pygame.font.Font(None, kb_font_size)

    key = 0
    while key < 10:
        button_color = KEYBOARD_BACKGROUND
        if key_num_solution == key:
            button_color = KEYBOARD_BACKGROUND_PRESSED

        button_rect = pygame.Rect(sx + kb_width * key + kb_margin * key, sy + 0, kb_width, kb_height)
        if button_rect.collidepoint((mx, my)):
            button_color = KEYBOARD_BACKGROUND_PRESSED
            key_num_solution = key
        button_rect.x -= sx
        button_rect.y -= sy

        pygame.draw.rect(kb0_9_surface, button_color, button_rect)
        pygame.draw.rect(kb0_9_surface, KEYBOARD_FRAME, button_rect, 3)
        text_surf = font.render(str(key), True, KEYBOARD_COLOR)
        text_rect = text_surf.get_rect(center=button_rect.center)
        kb0_9_surface.blit(text_surf, text_rect)

        key += 1

    sc.blit(kb0_9_surface, coords)

    return key_num_solution


def draw_timer(sc, coords, timer_progress, curtimer):

    sx = coords[0]
    sy = coords[1]
    if not (sx and sy):
        sx = 50
        sy = 50
        coords = (sx, sy)
    s_width = 100
    s_height = 100
    round_timer_surface = pygame.Surface((s_width, s_height), pygame.SRCALPHA)
    round_timer_surface.convert_alpha()
    record_table_rect = round_timer_surface.get_rect()

    pygame.draw.rect(round_timer_surface, (0,0,0), record_table_rect, 1)

    font_timer = pygame.font.Font(None, 40)

    # Timer Logic
    timer_circle_rect = pygame.Rect((0, 0, 100, 100))
    pygame.draw.arc(round_timer_surface, WHITE, timer_circle_rect, 0, math.pi * 2 * timer_progress, 5)

    timer_text_surface = font_timer.render(str(int(curtimer)), True, WHITE)
    timer_text_surface_rect = timer_text_surface.get_rect(center=timer_circle_rect.center)
    round_timer_surface.blit(timer_text_surface, timer_text_surface_rect)

    sc.blit(round_timer_surface, coords)


def draw_current_score_player_level(sc, coords, score, player, level):

    sx = coords[0]
    sy = coords[1]
    if not (sx and sy):
        sx = WIDTH / 2 - 290
        sy = 80
        coords = (sx, sy)
    s_width = 580
    s_height = 60
    header_score_surface = pygame.Surface((s_width, s_height), pygame.SRCALPHA)
    header_score_surface.convert_alpha()
    header_score_rect = header_score_surface.get_rect()

    pygame.draw.rect(header_score_surface, (0,0,0), header_score_rect, 1)

    font_score = pygame.font.Font(None, 40)
    header_score_text_surface = font_score.render("СЧЕТ: " + str(score), True, GOLD)
    header_score_text_surface_rect = header_score_text_surface.get_rect(centerx=header_score_rect.centerx)
    header_score_surface.blit(header_score_text_surface, header_score_text_surface_rect)

    font_player_level = pygame.font.Font(None, 30)
    header_score_text2_surface = font_player_level.render(" " + str(player) + ". " +
                                                          str(level), True, PURPLE)
    header_score_text2_surface_rect = header_score_text2_surface.get_rect(centerx=header_score_rect.centerx, centery=40)
    header_score_surface.blit(header_score_text2_surface, header_score_text2_surface_rect)

    sc.blit(header_score_surface, coords)

    pass


def draw_player_switch_buttons(sc, coords, mcoords, player_id):
    mx, my = mcoords

    b_width = 100
    b_height = 40
    b_margin = 6

    sx = coords[0]
    sy = coords[1]
    if not (sx and sy):
        sx = WIDTH / 2 - b_width * 2 - b_margin * 1.5
        sy = HEIGHT / 2 + 100
        coords = (sx, sy)

    s_width = b_width * 4 + b_margin * 3
    s_height = b_height
    b_surface = pygame.Surface((s_width, s_height), pygame.SRCALPHA)
    b_surface.convert_alpha()
    b_surface_rect = b_surface.get_rect()

    pygame.draw.rect(b_surface, (0, 0, 0), b_surface_rect, 1)

    b_font_size = 30
    font = pygame.font.Font(None, b_font_size)

    key = 0
    while key < 4:
        button_color = KEYBOARD_BACKGROUND
        if player_id == key + 1:
            button_color = KEYBOARD_BACKGROUND_PRESSED

        button_rect = pygame.Rect(sx + b_width * key + b_margin * key, sy + 0, b_width, b_height)
        if button_rect.collidepoint((mx, my)):
            button_color = KEYBOARD_BACKGROUND_PRESSED
            player_id = key + 1
        button_rect.x -= sx
        button_rect.y -= sy

        pygame.draw.rect(b_surface, button_color, button_rect)
        pygame.draw.rect(b_surface, KEYBOARD_FRAME, button_rect, 3)
        text_surf = font.render(str(db_get_player_name(key + 1)), True, KEYBOARD_COLOR)
        text_rect = text_surf.get_rect(center=button_rect.center)
        b_surface.blit(text_surf, text_rect)

        key += 1

    sc.blit(b_surface, coords)

    return player_id

def draw_level_switch_buttons(sc, coords, mcoords, level_id):
    mx, my = mcoords

    b_width = 170
    b_height = 40
    b_margin = 6

    sx = coords[0]
    sy = coords[1]
    if not (sx and sy):
        sx = WIDTH / 2 - b_width * 1.5 - b_margin * 1
        sy = HEIGHT / 2 + 160
        coords = (sx, sy)

    s_width = b_width * 3 + b_margin * 2
    s_height = b_height
    b_surface = pygame.Surface((s_width, s_height), pygame.SRCALPHA)
    b_surface.convert_alpha()
    b_surface_rect = b_surface.get_rect()

    pygame.draw.rect(b_surface, (0, 0, 0), b_surface_rect, 1)

    b_font_size = 20
    font = pygame.font.Font(None, b_font_size)

    key = 0
    while key < 3:
        button_color = KEYBOARD_BACKGROUND
        if level_id == key + 1:
            button_color = KEYBOARD_BACKGROUND_PRESSED

        button_rect = pygame.Rect(sx + b_width * key + b_margin * key, sy + 0, b_width, b_height)
        if button_rect.collidepoint((mx, my)):
            button_color = KEYBOARD_BACKGROUND_PRESSED
            level_id = key + 1
        button_rect.x -= sx
        button_rect.y -= sy

        pygame.draw.rect(b_surface, button_color, button_rect)
        pygame.draw.rect(b_surface, KEYBOARD_FRAME, button_rect, 2)
        text_surf = font.render(str(db_get_level_name(key + 1)), True, KEYBOARD_COLOR)
        text_rect = text_surf.get_rect(center=button_rect.center)
        b_surface.blit(text_surf, text_rect)

        key += 1

    sc.blit(b_surface, coords)

    return level_id
