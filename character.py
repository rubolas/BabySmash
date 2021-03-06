import pygame as pg
from utils import rand_color


class Character:
    def __init__(self, char=" ", size=3, pos=(0, 0), color=None):
        self.char = char[0]
        self.font = pg.font.SysFont("ubuntumono", size, bold=1)
        self.color = color or rand_color()
        self.origsurf = self.font.render(self.char, True, self.color)
        self.textsurf = self.origsurf.copy()
        self.alphasurf = pg.Surface(self.textsurf.get_size(), pg.SRCALPHA)
        self.alpha = 255
        self.fade_speed = 0
        self.pos = pos

    def resize(self, new_size):
        self.font = pg.font.Font("ubuntumono", new_size, bold=1)
        self.origsurf = self.font.render(self.char, True, self.color)
        self.textsurf = self.origsurf.copy()
        self.alphasurf = pg.Surface(self.textsurf.get_size(), pg.SRCALPHA)

    def set_alpha(self, num):
        self.alpha = num
        if num < 0:
            self.alpha = 0
        if num > 255:
            self.alpha = 255

    def set_fade_speed(self, num):
        self.fade_speed = num

    def move(self, new_pos):
        self.pos = new_pos

    def get_rect(self):
        return pg.Rect(self.pos, self.textsurf.get_size())

    def __str__(self):
        return self.char

    def draw(self, screen):
        self.textsurf = self.origsurf.copy()
        self.alphasurf.fill((255, 255, 255, self.alpha))
        self.textsurf.blit(self.alphasurf, (0, 0), special_flags=pg.BLEND_RGBA_MULT)
        self.alpha = max(self.alpha - self.fade_speed, 0)
        screen.blit(self.textsurf, self.pos)
