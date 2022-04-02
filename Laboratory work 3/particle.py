import pygame
from support import import_folder


class ParticleEffect(pygame.sprite.Sprite):
    def __init__(self, pos, type):
        super().__init__()
        self.frame_index = 0
        self.animation_speed = 0.5
        if type == 'jump':
            self.frame = import_folder('/PyCharm/Ознакомление/pygame/graphics/character/dust_particles/jump')
        if type == 'land':
            self.frame = import_folder('/PyCharm/Ознакомление/pygame/graphics/character/dust_particles/land')
        if type == 'explosion':
            self.frame = import_folder('/PyCharm/Ознакомление/pygame/graphics/enemy/explosion')
        self.image = self.frame[self.frame_index]
        self.rect = self.image.get_rect(center=pos)

    def animate(self):
        self.frame_index += self.animation_speed
        if self.frame_index >= len(self.frame):
            self.kill()
        else:
            self.image = self.frame[int(self.frame_index)]

    def update(self, x_shift):
        self.animate()
        self.rect.x += x_shift
