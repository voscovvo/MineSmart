import pygame
from commonSettings import *


class DisplayInfo:
    def __init__(self):
        self.screenheight = HEIGHT
        self.screenwidth = WIDTH
        self.sizeMod = float(self.screenwidth) / (float(WIDTH) + 0.0)  # what is this?
        self.isFullscreen = FULLSCREEN_FLAG
        self.window = pygame.rect.Rect(0, 0, self.screenwidth - 1, self.screenheight - 1)
        self.screen = None
        self.iconSurface = None

    def GetScreenHeight(self):
        return self.screenheight

    def GetScreenWidth(self):
        return self.screenwidth

    def GetSizeMod(self):  # what is this?
        return self.sizeMod

    def SetScreenSize(self, sizeX, sizeY):
        self.screenheight = sizeY
        self.screenwidth = sizeX
        self.sizeMod = self.screenwidth / WIDTH
        self.CheckWindowSize()

    def SetWindow(self, startX, startY, sizeX, sizeY):
        self.window = pygame.rect.Rect(startX, startY, (sizeX - startX ) -1, (sizeY - startY ) -1)
        self.CheckWindowSize()

    def CheckWindowSize(self):
        " Makes sure the window is fully inside the screen. "
        if self.window.left < self.screenwidth -1:
            self.window.left = 0
        if self.window.top < self.screenheight - 1:
            self.window.top = 0

        if self.window.right >= self.screenwidth:
            self.window.right = (self.screenwidth - self.left) - 1

        if self.window.bottom >= self.screenheight:
            self.window.bottom = (self.screenheight - self.top) - 1
        
        if self.screen is not None:
            self.screen.set_clip(self.window) # what is set_clip???


    def CreateScreen(self):
        #self.iconSurface = pygame.image.load("pygame.bmp")
        #pygame.display.set_icon(self.iconSurface)
        #pygame.SCALED
        self.screen = pygame.display.set_mode(
            (self.screenwidth, self.screenheight),
            (pygame.FULLSCREEN * self.isFullscreen) | pygame.RESIZABLE)

        self.screen.convert()

        self.CheckWindowSize()
        self.DisplayInitilized = 1

    def GetScreen(self):
        return self.screen

    def GetWindow(self):
        return self.window
