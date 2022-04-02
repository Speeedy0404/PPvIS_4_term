import pygame
import sys
from settings import *
from level import Level
from overworld import Overworld
from ui import UI
from menu import Menu, About, Records
from parser import XmlParser, root


class Game:
    def __init__(self):
        # game attributes
        self.max_level = 4
        self.max_health = 100
        self.cur_health = 100
        self.coins = 0
        self.score = 0

        # audio
        self.level_bg_music = pygame.mixer.Sound('/PyCharm/Ознакомление/pygame_level/audio/level_music.wav')
        self.level_bg_music.set_volume(0.2)
        self.overworld_bg_music = pygame.mixer.Sound('/PyCharm/Ознакомление/pygame_level/audio/overworld_music.wav')
        self.overworld_bg_music.set_volume(0.2)

        # user interface
        self.ui = UI(screen)

        # menu creation
        self.menu = Menu(0, 3, screen, self.create_overworld, self.create_menu, self.create_records)
        self.status = 'menu'
        self.overworld_bg_music.play(loops=-1)

        # overworld creation
        self.overworld = Overworld(0, self.max_level, screen, self.create_level, self.create_menu)

    def create_level(self, current_level):
        self.level = Level(current_level, screen, self.create_overworld, self.change_coins, self.change_health,
                           self.level_passed, self.change_score)
        self.status = 'level'
        self.overworld_bg_music.stop()
        self.level_bg_music.play(loops=-1)

    def create_overworld(self, current_level, new_max_level):
        if new_max_level > self.max_level:
            self.max_level = new_max_level
        self.overworld = Overworld(current_level, self.max_level, screen, self.create_level, self.create_menu)
        self.status = 'overworld'
        self.level_bg_music.stop()
        self.overworld_bg_music.stop()
        self.overworld_bg_music.play(loops=-1)

    def create_menu(self):
        self.menu = Menu(0, 3, screen, self.create_overworld, self.create_about, self.create_records)
        self.status = 'menu'
        self.overworld_bg_music.stop()
        self.overworld_bg_music.play(loops=-1)

    def create_about(self):
        info = ['Movement : -> (right), <- (left)', 'Jump : space', 'Choice level : space', 'Close about : escape ',
                'Close choice of level : escape']
        self.about = About(screen, info, self.create_menu)
        self.status = 'about'
        self.overworld_bg_music.stop()
        self.overworld_bg_music.play(loops=-1)

    def create_records(self):
        global root
        info = XmlParser.find_score(root)
        name = XmlParser.find_name(root)
        self.records = Records(screen, info, self.create_menu, name)
        self.status = 'records'
        self.overworld_bg_music.stop()
        self.overworld_bg_music.play(loops=-1)

    def change_coins(self, amount):
        self.coins += amount

    def change_health(self, amount):
        self.cur_health += amount

    def change_score(self, amount):
        self.score += amount

    def level_passed(self, current_level):
        global root
        list_score = XmlParser.find_score(root)
        if self.score > int(list_score[current_level]):
            number = self.score
            XmlParser.change_score(current_level, number)
        self.cur_health = 100
        self.score = 0

    def check_game_over(self):
        if self.cur_health <= 0:
            self.cur_health = 100
            self.coins = 0
            self.score = 0
            self.overworld = Overworld(0, self.max_level, screen, self.create_level, self.create_menu)
            self.status = 'overworld'
            self.level_bg_music.stop()
            self.overworld_bg_music.play(loops=-1)

    def run(self):
        if self.status == 'overworld':
            self.overworld.run()
        elif self.status == 'level':
            self.level.run()
            self.ui.show_health(self.cur_health, self.max_health)
            self.ui.show_coins(self.coins)
            self.ui.show_score(self.score)
            self.check_game_over()
        elif self.status == 'menu':
            self.menu.run()
        elif self.status == 'about':
            self.about.run()
        elif self.status == 'records':
            self.records.run()


# Pygame setup
pygame.init()
screen = pygame.display.set_mode((screen_width, screen_height))
clock = pygame.time.Clock()
game = Game()
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    screen.fill('grey')
    game.run()

    pygame.display.update()
    clock.tick(60)
