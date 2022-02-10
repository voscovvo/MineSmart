import pygame
from commonSettings import *


def draw_solvenum_holder3(sc, coords, solveNum_1, solveNum_Action, solveNum_2, solveNum_Result, blind, timer_progress):

    blind_sq = 0
    if blind == 1:
        blind_sq = 1
    elif blind == 2:
        blind_sq = 3
    elif blind == 3:
        blind_sq = 5

    h_width = 100
    h_height = 100
    h_margin = 20

    # coord of the first holder
    hx1 = WIDTH / 2 - h_width * 2.5 - h_margin * 2
    hy1 = h_height * 1.5

    sx = coords[0]
    sy = coords[1]
    if not (sx and sy):
        sx = WIDTH / 2 - h_width * 2.5 - h_margin * 2
        sy = h_height * 1.5
        coords = (sx, sy)

    s_width = h_width * 5 + h_margin * 4
    s_height = h_height * 1.5 + 10  # Place holder + bonus timer
    solvetask_surface = pygame.Surface((s_width, s_height), pygame.SRCALPHA)
    solvetask_surface.convert_alpha()
    solvetask_surface_rect = solvetask_surface.get_rect()

    pygame.draw.rect(solvetask_surface, (0,0,0), solvetask_surface_rect, 1)

    holder_font_size = 50
    font = pygame.font.Font(None, holder_font_size)

    st_surface = [font.render(str(solveNum_1), True, SOLVENUM_COLOR),
                  font.render(str(solveNum_Action), True, SOLVENUM_COLOR),
                  font.render(str(solveNum_2), True, SOLVENUM_COLOR),
                  font.render("=", True, SOLVENUM_COLOR),
                  font.render(str(solveNum_Result), True, SOLVENUM_COLOR),
                  font.render(" ", True, SOLVENUM_COLOR)]

    for i in range(6):
        bg_color = SOLVENUM_BACKGROUND
        if blind_sq == i + 1:
            bg_color = SOLVENUM_HIDE
            st_surface[i] = st_surface[-1]

        holder_rect = pygame.Rect(h_width * i + h_margin * i, 0, h_width, h_height)
        pygame.draw.rect(solvetask_surface, bg_color, holder_rect)
        pygame.draw.rect(solvetask_surface, SOLVENUM_FRAME, holder_rect, 3)
        text_rect = st_surface[i].get_rect(center=holder_rect.center)
        solvetask_surface.blit(st_surface[i], text_rect)

    # Draw Bonus counter ... reconsider how...
    # Timer Logic
    maxtimer = h_width * 5 + h_margin * 4
    pygame.draw.rect(solvetask_surface, SOLVENUM_BACKGROUND, ((0, h_height * 1.5), (maxtimer*timer_progress, 10)))

    sc.blit(solvetask_surface, coords)
