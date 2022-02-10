# Imports
from gameClass import *

# import pygame.examples.freetype_misc

pygame.init()

if __name__ == "__main__":

    # Console Message when game start
    print("Default Font: %s" % (pygame.font.get_default_font()))
    print("All fonts:\n-------------")
    print(pygame.font.get_fonts())

    # pygame.examples.freetype_misc.run()

    game = GameClass()
    game.main_loop()

    #pygame.display.init()
    #modes = pygame.display.list_modes(32)
    #print(modes)

    pygame.quit()
    quit()
    exit()
