# Imports
# import pygame_sdl2
# pygame_sdl2.import_as_pygame()
#
from os import environ
from sys import platform as _sys_platform
from gameClass import *


# import pygame.examples.freetype_misc

def platform():
    if 'ANDROID_ARGUMENT' in environ:
        return "android"
    elif _sys_platform in ('linux', 'linux2', 'linux3'):
        return "linux"
    elif _sys_platform in ('win32', 'cygwin'):
        return "win"



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
